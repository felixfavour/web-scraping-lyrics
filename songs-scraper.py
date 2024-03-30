import csv
import requests
from bs4 import BeautifulSoup

album_class_name = "ListItem__Link-sc-122yj9e-1"
song_class_name = "u-display_block"
lyrics_class_name = "Lyrics__Container-sc-1ynbvzw-1"

artist_name = "Dunsin Oyekan"
all_songs_data = [
    {
        "title": "Imole De",
        "url": "https://genius.com/Dunsin-oyekan-imole-de-lyrics"
    },
    {
        "title": "Fragrance to fire",
        "url": "https://genius.com/Dunsin-oyekan-fragrance-to-fire-lyrics"
    },
    {
        "title": "IBA",
        "url": "https://genius.com/Nathaniel-bassey-iba-lyrics"
    },
    {
        "title": "BREATHE",
        "url": "https://genius.com/Dunsin-oyekan-breathe-lyrics"
    },
    {
        "title": "Yah",
        "url": "https://genius.com/Dunsin-oyekan-yah-lyrics"
    },
    {
        "title": "OGO",
        "url": "https://genius.com/Dunsin-oyekan-ogo-lyrics"
    },
    {
        "title": "When God Walks In",
        "url": "https://genius.com/Dunsin-oyekan-when-god-walks-in-lyrics"
    },
    {
        "title": "Most High",
        "url": "https://genius.com/Dunsin-oyekan-most-high-lyrics"
    },
    {
        "title": "City of God (live)",
        "url": "https://genius.com/Dunsin-oyekan-city-of-god-live-lyrics"
    },
    {
        "title": "Those Who Will Win",
        "url": "https://genius.com/Dunsin-oyekan-those-who-will-win-lyrics"
    },
    {
        "title": "Ascend",
        "url": "https://genius.com/Dunsin-oyekan-ascend-lyrics"
    },
    {
        "title": "To Know You",
        "url": "https://genius.com/Dunsin-oyekan-to-know-you-lyrics"
    },
    {
        "title": "God of All Possibilities",
        "url": "https://genius.com/Dunsin-oyekan-god-of-all-possibilities-lyrics"
    },
    {
        "title": "Absolutely Nothing",
        "url": "https://genius.com/Dunsin-oyekan-absolutely-nothing-lyrics"
    },
    {
        "title": "Before The Lord our God",
        "url": "https://genius.com/Dunsin-oyekan-before-the-lord-our-god-lyrics"
    },
    {
        "title": "Roar",
        "url": "https://genius.com/Dunsin-oyekan-roar-lyrics"
    },
    {
        "title": "You Remain the Same",
        "url": "https://genius.com/Dunsin-oyekan-you-remain-the-same-lyrics"
    },
    {
        "title": "I Will Stay",
        "url": "https://genius.com/Dunsin-oyekan-i-will-stay-lyrics"
    },
    {
        "title": "Always God",
        "url": "https://genius.com/Dunsin-oyekan-always-god-lyrics"
    },
    {
        "title": "The Code of Worship",
        "url": "https://genius.com/Dunsin-oyekan-the-code-of-worship-lyrics"
    },
    {
        "title": "Halleluyah",
        "url": "https://genius.com/Dunsin-oyekan-halleluyah-lyrics"
    },
    {
        "title": "Yhwh",
        "url": "https://genius.com/Dunsin-oyekan-yhwh-lyrics"
    },
    {
        "title": "One on One",
        "url": "https://genius.com/Dunsin-oyekan-one-on-one-lyrics"
    },
    {
        "title": "IRE",
        "url": "https://genius.com/Ty-bello-ire-lyrics"
    },
    {
        "title": "People of His Presence",
        "url": "https://genius.com/Dunsin-oyekan-people-of-his-presence-lyrics"
    },
    {
        "title": "Holy Is The Lord",
        "url": "https://genius.com/Dunsin-oyekan-holy-is-the-lord-lyrics"
    },
    {
        "title": "Kaabo",
        "url": "https://genius.com/Dunsin-oyekan-kaabo-lyrics"
    },
    {
        "title": "Benediction",
        "url": "https://genius.com/Dunsin-oyekan-benediction-lyrics"
    },
    {
        "title": "When I See You",
        "url": "https://genius.com/Dunsin-oyekan-when-i-see-you-lyrics"
    },
    {
        "title": "Finger of God",
        "url": "https://genius.com/Dunsin-oyekan-finger-of-god-lyrics"
    },
    {
        "title": "Your Goodness",
        "url": "https://genius.com/Dunsin-oyekan-your-goodness-lyrics"
    },
    {
        "title": "Open Up",
        "url": "https://genius.com/Dunsin-oyekan-open-up-lyrics"
    },
    {
        "title": "Hallelujah - The Sacred Sound",
        "url": "https://genius.com/Dunsin-oyekan-hallelujah-the-sacred-sound-lyrics"
    },
    {
        "title": "Na You",
        "url": "https://genius.com/Dunsin-oyekan-na-you-lyrics"
    },
    {
        "title": "Can’t Be Less",
        "url": "https://genius.com/Dunsin-oyekan-cant-be-less-lyrics"
    },
    {
        "title": "I’ll Be Here",
        "url": "https://genius.com/Dunsin-oyekan-ill-be-here-lyrics"
    },
    {
        "title": "If All I Say Is Jesus",
        "url": "https://genius.com/Dunsin-oyekan-if-all-i-say-is-jesus-lyrics"
    },
    {
        "title": "Arise",
        "url": "https://genius.com/Dunsin-oyekan-arise-lyrics"
    },
    {
        "title": "Because He Is, I Am",
        "url": "https://genius.com/Dunsin-oyekan-because-he-is-i-am-lyrics"
    },
    {
        "title": "Maranatha",
        "url": "https://genius.com/Dunsin-oyekan-maranatha-lyrics"
    },
    {
        "title": "At All Cost",
        "url": "https://genius.com/Dunsin-oyekan-at-all-cost-lyrics"
    },
    {
        "title": "Those Who Will",
        "url": "https://genius.com/Dunsin-oyekan-those-who-will-lyrics"
    },
    {
        "title": "Oh To Love You (Conversation With The Father)",
        "url": "https://genius.com/Dunsin-oyekan-oh-to-love-you-conversation-with-the-father-lyrics"
    },
]

def getAlbumTitlesFromArtistPage (url):
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

def getSongTitlesFromAlbumPage (url):
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

def getLyricsFromSongPage (url):
    # url = "https://genius.com/Nathaniel-bassey-carry-me-lyrics"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        lyrics = soup.find(name="div", class_=lyrics_class_name).get_text(separator='\n')
        return lyrics
    except:
        print("No lyrics found for: ", url.replace("https://genius.com/", ""))
        return "No lyrics here"

def getAllLyricsDataFromArtists ():
    for artist in artists:
        formattedArtist = artist.lower().replace(' ', '-').replace("'", "")
        albums = getAlbumTitlesFromArtistPage("https://genius.com/artists/" + formattedArtist + "/albums")
        for album in albums:
            songs = getSongTitlesFromAlbumPage(album["url"])
            for song in songs:
                temp_song_data = {
                    "lyrics": "",
                    "title": song["title"],
                    "album": album["title"],
                    "cover": album["cover"],
                    "artist": artist
                }
                lyrics = getLyricsFromSongPage(song["url"])
                temp_song_data["lyrics"] = lyrics
                all_songs_data.append(temp_song_data)

getAllLyricsDataFromArtists()

for song in all_songs_data:
    temp_song = {"lyrics": "", "title": "", "album" : "", "cover": "", "artist": artist_name}
    temp_song["title"] = song["title"]
    lyrics = getLyricsFromSongPage(song["url"])
    temp_song["lyrics"] = lyrics


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

