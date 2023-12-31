import os.path

import requests

from custom_exceptions import TrackExistsException


class Track:
    def __init__(self, track):
        self.location = track.find("location")
        self.url_download = self.location.text.strip()
        self.track_name = self.__get_text(track.find("title"))

    def __get_text(self, bs_el):
        return bs_el.text.strip()

    def get_track_name(self) -> str:
        return self.track_name

    def __check_file_exist(self, path):
        check_file = os.path.isfile(path)
        return check_file

    def download(self):
        file_name = "nhac/" + self.track_name + ".mp3"
        if self.__check_file_exist(file_name):
            raise TrackExistsException(self.track_name)

        try:
            r = requests.get(self.url_download)
        except Exception as e:
            print(f"> Lỗi khi tải {self.track_name} - error: ", e)
            raise Exception(f"> Lỗi khi tải {self.track_name}", e)

        try:
            open(file_name, "wb").write(r.content)
        except Exception as e:
            print(f"> Lỗi khi lưu file {self.track_name} - - error: {e}")
            raise Exception(f"> Lỗi khi lưu file {self.track_name}")
