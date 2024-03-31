import csv
import requests
from bs4 import BeautifulSoup

album_class_name = "ListItem__Link-sc-122yj9e-1"
song_class_name = "u-display_block"
lyrics_class_name = "Lyrics__Container-sc-1ynbvzw-1"

all_songs_data = []
# artists = ["Dunsin Oyekan", "Mercy Chinwo", "Nathaniel Bassey", "Sinach", "Frank Edwards", "Ada Ehi", "Lara George", "Ebennig", "Moses Bliss", "Judikay", "Minister GUC"]
artists = ["Hillsong Worship", "Hillsong United", "Maverick City Music", "Ron Kenoly", "Integrity's Hosanna Music", "Donnie McClurkin", "Tasha Cobbs", "Chris Tomlin", "William McDowell", "Cece Winans", "Todd Dulaney", "Travis Greene", "Israel Houghton", "Micah Stampley", "Don Moen", "Bethel Music", "Planetshakers", "Jesus Culture", "Phil Wickham", "Elevation Worship", "TY Bello"]

# album_urls = [
#     # Nathaniel Bassey
#     "https://genius.com/albums/Nathaniel-bassey/The-names-of-god",
#     "https://genius.com/albums/Nathaniel-bassey/The-king-is-coming",
#     "https://genius.com/albums/Nathaniel-bassey/Jesus-the-resurrection-the-life",
#     "https://genius.com/albums/Nathaniel-bassey/Someones-at-the-door",
#     "https://genius.com/albums/Nathaniel-bassey/The-son-of-god-imela",
#     "https://genius.com/albums/Nathaniel-bassey/Hallelujah-again-revelation-19-3",
#     # Mercy Chinwo
#     "https://genius.com/albums/Mercy-chinwo/Elevated-ep"
#     "https://genius.com/albums/Mercy-chinwo/Satisfied",
#     "https://genius.com/albums/Mercy-chinwo/Overwhelming-victory"
# ]

# Write to file
# with open('song-titles.txt', 'w') as file:
#     file.write(lyrics)

def get_album_titles_from_artist_page (url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        album_objects = []
        albums = soup.find_all(name="a", class_=album_class_name)
        for album in albums:
            album_obj = {"cover": "","title": "", "url": ""}
            album_obj["cover"] = album.div.img["src"].replace("\xa0", " ").strip()
            album_obj["title"] = album.h3.text.replace("\xa0", " ").strip()
            album_obj["url"] = album['href']
            album_objects.append(album_obj)
        return album_objects
    except:
        print("No albums found for: ", url.replace("https://genius.com/artists/", ""))
        return []

def get_song_titles_from_album_page (url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        song_objects = []
        songs = soup.find_all(name="a", class_=song_class_name)
        for song in songs:
            song_obj = {"title": "", "url": ""}
            song_obj["title"] = song.text.replace("Lyrics", "").replace("\xa0", " ").strip()
            song_obj["url"] = song['href']
            song_objects.append(song_obj)
        return song_objects
    except:
        print("No song titles found for: ", url.replace("https://genius.com/albums/", ""))
        return []

def get_lyrics_from_song_page (url):
    # url = "https://genius.com/Nathaniel-bassey-carry-me-lyrics"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        lyrics = soup.find(name="div", class_=lyrics_class_name).get_text(separator='\n')
        return lyrics
    except:
        print("No lyrics found for: ", url.replace("https://genius.com/", ""))
        return "No lyrics here"

def get_all_lyrics_data_from_artists ():
    for artist in artists:
        formattedArtist = artist.lower().replace(' ', '-').replace("'", "")
        albums = get_album_titles_from_artist_page("https://genius.com/artists/" + formattedArtist + "/albums")
        for album in albums:
            songs = get_song_titles_from_album_page(album["url"])
            for song in songs:
                temp_song_data = {
                    "lyrics": "",
                    "title": song["title"],
                    "album": album["title"],
                    "cover": album["cover"],
                    "artist": artist
                }
                lyrics = get_lyrics_from_song_page(song["url"])
                temp_song_data["lyrics"] = lyrics
                all_songs_data.append(temp_song_data)


get_all_lyrics_data_from_artists()

# Write lyrics data to CSV file
data = [
    ["lyrics", "title", "album", "cover", "artist"]
]
for row in all_songs_data:
    data.append(list(row.values()))

with open("lyrics_data_foreign.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV data written")

