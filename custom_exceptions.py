class TrackExistsException(Exception):
    def __init__(self, track_name: str):
        self.message = f"Bài hát {track_name} đã tồn tại, bỏ qua..."
        super().__init__(self.message)

class TrackExistsWithSlugifyNameException(Exception):
    def __init__(self, track_name: str, slugify_track_name: str):
        self.message = f"Bài hát {track_name} đã tồn tại dưới tên {slugify_track_name}, bỏ qua..."
        super().__init__(self.message)
