def make_album(artist_name, album_title, number_of_songs_on_album=None):
    """Return a dictionary of album information"""
    album = { "artist_name": artist_name, "album_title": album_title}

    if number_of_songs_on_album:
        album["number_of_songs_on_album"] = number_of_songs_on_album

    return album

while True:
    artist = input("artist name: ")
    if artist == 'q':
        break
    title = input("album title: ")
    if title == 'q':
        break
    number_songs = input("how many song on this album: ")
    if number_songs == 'q':
        break
    some_album = make_album(artist, title, number_songs)
    print(some_album)

# some_album = make_album("me", "little taco")
# print(some_album)
