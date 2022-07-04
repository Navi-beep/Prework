def make_album(artist_name,album_title,number_of_songs=None):
    """return a dictionary containing album name and title"""
    if number_of_songs:
        album = {'name': artist_name, 'title': album_title, 'songs': number_of_songs}
    else:
        album = {'name': artist_name, 'title': album_title}
    return album


complete_album = make_album('Pink Floyd', 'Dark Side of the Moon')
print(complete_album)
complete_album = make_album('Black Sabbath','Master of Reality')
print(complete_album)
complete_album = make_album('Boards of Canada','The Campfire Headphase', 15)
print(complete_album)


