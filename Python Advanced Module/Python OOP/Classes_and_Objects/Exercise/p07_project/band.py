from p07_project.album import Album


class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        for band_album in self.albums:
            if band_album.name == album.name:
                return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for band_album in self.albums:
            if band_album.name == album_name:
                if band_album.published:
                    return f"Album has been published. It cannot be removed."
                self.albums.remove(band_album)
                return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        result = ''
        result += f"Band {self.name}\n"
        for album in self.albums:
            result += album.details()
        return result
