playlist = {
    "Ching Chang Hon Chi": {"artist": "Dehao Zhang", "genre": "Hip Hop"},
    "Flight Of The Bumblebee": {"artist": "Rimsky Korsakov", "genre": "Classical"},
    "Aishite Aishite Aishite": {"artist": "Kikuo", "genre": "Vocaloid"},
    "We Didn't Start The Fire": {"artist": "Billy Joel", "genre": "Pop Rock"}
}

def add_song(title, artist, genre):
    playlist[title] = {"artist": artist, "genre": genre}
    print(f"Song '{title}' by {artist} added to the playlist.")

def view_playlist():
    if not playlist:
        print("Your playlist is empty.")
    else:
        print("Current Playlist:")
        for title, details in playlist.items():
            print(f"Title: {title} | Artist: {details['artist']} | Genre: {details['genre']}")

def update_song(title, artist=None, genre=None):
    if title in playlist:
        if artist:
            playlist[title]["artist"] = artist
        if genre:
            playlist[title]["genre"] = genre
        print(f"Song '{title}' updated.")
    else:
        print(f"Song '{title}' not found in the playlist.")

def delete_song(title):
    if title in playlist:
        del playlist[title]
        print(f"Song '{title}' has been deleted from the playlist.")
    else:
        print(f"Song '{title}' not found in the playlist.")

add_song("Cupid", "Fifty Fifty", "K-pop")
view_playlist()
update_song("Cupid", artist="Fifty Fifty", genre="Pop")
delete_song("Flight Of The Bumblebee")
view_playlist()