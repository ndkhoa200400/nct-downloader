import os.path
from slugify import slugify
import requests

from custom_exceptions import TrackExistsException, TrackExistsWithSlugifyNameException


class Track:
    def __init__(self, track):
        self.location = track.find("location")
        self.locationHQ = track.find("locationHQ")
        self.url_download = self.location.text.strip()
        self.url_download_hq = self.locationHQ.text.strip()
        self.track_name = self.__get_text(track.find("title"))

    def __get_text(self, bs_el):
        return bs_el.text.strip()

    def get_track_name(self) -> str:
        return self.track_name

    def __check_file_exist(self, path):
        check_file = os.path.isfile(path)
        return check_file

    def _try_download_hq(self):
        is_high_quality_downloaded = False
        try:
            r = requests.get(self.url_download_hq)
            is_high_quality_downloaded = True
        except Exception as e:
            try:
                r = requests.get(self.url_download)
            except:
                print(f"> Lỗi khi tải {self.track_name} - error: ", e)
                raise Exception(f"> Lỗi khi tải {self.track_name}", e)

        return r, is_high_quality_downloaded

    def download(self):
        slugify_track_name = slugify(self.track_name)
        file_name = "nhac/" + self.track_name + ".mp3"
        slugify_file_name = "nhac/" + slugify_track_name + ".mp3"
        if self.__check_file_exist(file_name):
            raise TrackExistsException(self.track_name)
        if self.__check_file_exist(slugify_file_name):
            raise TrackExistsWithSlugifyNameException(self.track_name, slugify_track_name)

        r, is_high_quality_downloaded = self._try_download_hq()

        try:
            open(file_name, "wb").write(r.content)
            if is_high_quality_downloaded:
                print(f"+ Đã tải xong bài hát {self.track_name} với chất lượng cao")
            else:
                print(f"+ Đã tải xong bài hát {self.track_name}")
        # Code Error because file_name contains special characters
        # Slugify file_name and try again
        except OSError as e:
            if e.errno == 22:
                print(f"> Đổi tên bài hát {self.track_name} => {slugify_track_name}")
                open(slugify_file_name, "wb").write(r.content)
                if is_high_quality_downloaded:
                    print(f"+ Đã tải xong bài hát {slugify_track_name} với chất lượng cao")
                else:
                    print(f"+ Đã tải xong bài hát {slugify_track_name}")
        except Exception as e:
            print(f"> Lỗi khi lưu file {self.track_name} - error: {e}")
            raise Exception(f"> Lỗi khi lưu file {self.track_name}")    
        