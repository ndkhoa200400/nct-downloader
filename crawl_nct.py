import json
import os.path
import re
import sys
import time
import urllib
import urllib.request

import requests
from bs4 import BeautifulSoup
from lxml.html import fromstring

from custom_exceptions import TrackExistsException
from track import Track
from typing import List


def get_api_url(web_url):
    res = requests.get(
        url=web_url,
        headers={
            "Content-Type": "application/json;charset=UTF-8",
            "Vary": "Accept-Encoding",
        },
    )
    s = BeautifulSoup(res.text, "html.parser")

    match = re.search(r'player\.peConfig\.xmlURL\s*=\s*"([^"]+)"', res.text)

    if match:
        api_url = match.group(1)
        return api_url
    raise Exception("Không tìm thấy api url")


def get_tracks_from_web(web_url) -> List[Track]:
    api = get_api_url(web_url)
    r = requests.get(
        url=api,
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            "Referer": "https://www.nhaccuatui.com/",
            "Content-Type": "application/json;charset=UTF-8",
            "Vary": "Accept-Encoding",
        },
    )
    s = BeautifulSoup(r.text, "xml")

    tracks = s.find_all("track")
    _tracks = []
    for track in tracks:
        _tracks.append(Track(track))
    return _tracks


def download_tracks(tracks: List[Track]):
    count = 0
    for track in tracks:
        try:
            print(f"Đang tải bài hát {track.get_track_name()}")
            track.download()
        except TrackExistsException as e:
            print(e)
            continue
        except Exception as e:
            print(e)
            continue
        count += 1
        time.sleep(0.1)
    return count


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Vui lòng truyền đường dẫn bài hát")

    web_urls = sys.argv[1:]
    count = 0
    for web_url in web_urls:
        tracks = get_tracks_from_web(web_url)

        count += download_tracks(tracks)

    print(f"\nĐã xong. Đã tải {count} bài hát")
