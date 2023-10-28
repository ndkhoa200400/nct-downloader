class TrackExistsException(Exception):
    def __init__(self, track_name: str):
        self.message = f"Bài hát {track_name} đã tồn tại, bỏ qua..."
        super().__init__(self.message)
