def make_album(artist_name,album_title, number_of_songs=None):
    """return a dictionary containing album name and title"""
    full_album = {
        'artist': artist_name.title(), 
        'title': album_title.title()}

    if number_of_songs:
        full_album['number_of_songs'] = number_of_songs
    return full_album

title_prompt = "\nWhich album is your favorite?: "
artist_prompt = "What's the artist of the album?:"

print("You can press 'q' to quit at any time")

while True:
    artist = input(artist_prompt)
    if artist == 'q':
        break

    title = input(title_prompt)
    if title == 'q':
        break

    full_album = make_album(artist,title)
    print(full_album)

