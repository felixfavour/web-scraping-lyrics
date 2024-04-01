import csv
import re
import requests
from bs4 import BeautifulSoup

# Write lyrics data to CSV file
data = [
    ["lyrics", "title", "album", "cover", "artist"]
]
songs_data = []

artists = [
    {
        "name": "Mercy Chinwo",
        "url": "https://www.boomplay.com/artists/1525719"
    },
    {
        "name": "Moses Bliss",
        "url": "https://www.boomplay.com/artists/2896560"
    },
    {
        "name": "Nathaniel Bassey",
        "url": "https://www.boomplay.com/artists/81545"
    },
    {
        "name": "Ebuka Songs",
        "url": "https://www.boomplay.com/artists/65269557"
    },
    {
        "name": "Minister GUC",
        "url": "https://www.boomplay.com/artists/17632713"
    },
    {
        "name": "Tope Alabi",
        "url": "https://www.boomplay.com/artists/27218"
    },
    {
        "name": "Frank Edwards",
        "url": "https://www.boomplay.com/artists/1090"
    },
    {
        "name": "Sunmisola Agbebi",
        "url": "https://www.boomplay.com/artists/40582498"
    },
    {
        "name": "Dunsin Oyekan",
        "url": "https://www.boomplay.com/artists/572653"
    },
    {
        "name": "Judikay",
        "url": "https://www.boomplay.com/artists/2657941"
    },
    {
        "name": "Sola Allyson",
        "url": "https://www.boomplay.com/artists/31060"
    },
    {
        "name": "Ada Ehi",
        "url": "https://www.boomplay.com/artists/11654"
    },
    {
        "name": "Hillsong Worship",
        "url": "https://www.boomplay.com/artists/3037930"
    },
    {
        "name": "Don Moen",
        "url": "https://www.boomplay.com/artists/283833"
    },
    {
        "name": "Chioma Jesus",
        "url": "https://www.boomplay.com/artists/90217",
    },
    {
        "name": "Solomon Lange",
        "url": "https://www.boomplay.com/artists/97639",
        "first_10": True
    },
    {
        "name": "Mr M & Revelation",
        "url": "https://www.boomplay.com/artists/989468"
    },
    {
        "name": "Victoria Orenze",
        "url": "https://www.boomplay.com/artists/758734"
    },
    {
        "name": "Anendlessocean",
        "url": "https://www.boomplay.com/artists/13235956"
    },
    {
        "name": "Sis. Chinyere Udoma",
        "url": "https://www.boomplay.com/artists/2697518"
    },
    {
        "name": "Sinach",
        "url": "https://www.boomplay.com/artists/43703"
    },
    {
        "name": "Dr Paul Enenche",
        "url": "https://www.boomplay.com/artists/7106534",
        "first_10": True
    },
    {
        "name": "Steve Crown",
        "url": "https://www.boomplay.com/artists/98108",
        "first_10": True
    },
    {
        "name": "Neon Adejo",
        "url": "https://www.boomplay.com/artists/1053018",
        "first_10": True
    },
    {
        "name": "CeCe Winans",
        "url": "https://www.boomplay.com/artists/1844621"
    },
    {
        "name": "Tim Godfrey",
        "url": "https://www.boomplay.com/artists/1224974"
    },
    {
        "name": "Chief Commander Ebenezer Obey",
        "url": "https://www.boomplay.com/artists/46339"
    },
    {
        "name": "Hillsong UNITED",
        "url": "https://www.boomplay.com/artists/2255828"
    },
    {
        "name": "Maverick City Music",
        "url": "https://www.boomplay.com/artists/3683505"
    },
    {
        "name": "Limoblaze",
        "url": "https://www.boomplay.com/artists/49083"
    },
    {
        "name": "Loveworld Singers",
        "url": "https://www.boomplay.com/artists/22455224"
    },
    {
        "name": "Peterson Okopi",
        "url": "https://www.boomplay.com/artists/15600756"
    },
    {
        "name": "Prospa Ochimana",
        "url": "https://www.boomplay.com/artists/372757"
    },
    {
        "name": "Prince Gozie Okeke",
        "url": "https://www.boomplay.com/artists/4340212"
    },
    {
        "name": "Mike Abdul",
        "url": "https://www.boomplay.com/artists/1158"
    },
    {
        "name": "Esther Oji",
        "url": "https://www.boomplay.com/artists/2446795",
        "first_10": True
    },
    {
        "name": "Spirit of Prophecy",
        "url": "https://www.boomplay.com/artists/44708572",
        "first_10": True
    },
    {
        "name": "Victor Thompson",
        "url": "https://www.boomplay.com/artists/1537286",
        "first_10": True
    },
    {
        "name": "Osinachi Nwachukwu",
        "url": "https://www.boomplay.com/artists/6799005"
    },
    {
        "name": "Evang. Ojo Ade",
        "url": "https://www.boomplay.com/artists/45657"
    },
    {
        "name": "Joe Praize",
        "url": "https://www.boomplay.com/artists/32484",
        "first_10": True
    },
    {
        "name": "Bethel Music",
        "url": "https://www.boomplay.com/artists/137267"
    },
    {
        "name": "Eben",
        "url": "https://www.boomplay.com/artists/13795"
    },
    {
        "name": "Rev. Fr. Ejike Mbaka C.",
        "url": "https://www.boomplay.com/artists/7461352"
    },
    {
        "name": "Lawrence Oyor",
        "url": "https://www.boomplay.com/artists/12428173"
    },
    {
        "name": "Greatman Takit",
        "url": "https://www.boomplay.com/artists/15221217"
    },
    {
        "name": "Abbey Ojomu",
        "url": "https://www.boomplay.com/artists/19173101",
    },
    {
        "name": "Samsong",
        "url": "https://www.boomplay.com/artists/43707",
        "first_10": True
    },
    {
        "name": "Panam Percy Paul",
        "url": "https://www.boomplay.com/artists/97520"
    },
    {
        "name": "David G",
        "url": "https://www.boomplay.com/artists/47643",
        "first_10": True
    },
    {
        "name": "Paul Tomisin",
        "url": "https://www.boomplay.com/artists/40949948",
        "first_10": True
    },
    {
        "name": "Tasha Cobbs Leonard",
        "url": "https://www.boomplay.com/artists/1876160"
    },
    {
        "name": "Grace Lokwa",
        "url": "https://www.boomplay.com/artists/40743173",
        "first_10": True
    },
    {
        "name": "Preye Odede",
        "url": "https://www.boomplay.com/artists/32110",
        "first_10": True
    },
    {
        "name": "JayMikee",
        "url": "https://www.boomplay.com/artists/1108437"
    },
    {
        "name": "Ron Kenoly",
        "url": "https://www.boomplay.com/artists/273924"
    },
    {
        "name": "Cory Asbury",
        "url": "https://www.boomplay.com/artists/176131"
    },
    {
        "name": "Evang. Bola Are",
        "url": "https://www.boomplay.com/artists/30398"
    },
    {
        "name": "Lara George",
        "url": "https://www.boomplay.com/artists/10607"
    },
    {
        "name": "Elevation Worship",
        "url": "https://www.boomplay.com/artists/148756"
    },
    {
        "name": "Phil Wickham",
        "url": "https://www.boomplay.com/artists/195721",
        "first_10": True
    },
    {
        "name": "Nosa",
        "url": "https://www.boomplay.com/artists/11553"
    },
    {
        "name": "TY Bello",
        "url": "https://www.boomplay.com/artists/340764"
    },
    {
        "name": "Chris Tomlin",
        "url": "https://www.boomplay.com/artists/1844719"
    },
    {
        "name": "Evang. Dare Melody",
        "url": "https://www.boomplay.com/artists/46188"
    },
    {
        "name": "Phil Thompson",
        "url": "https://www.boomplay.com/artists/1266192"
    },
    {
        "name": "Pastor Emmanuel Iren",
        "url": "https://www.boomplay.com/artists/28074316"
    },
    {
        "name": "Todd Dulaney",
        "url": "https://www.boomplay.com/artists/2529535"
    },
    {
        "name": "Freke Umoh",
        "url": "https://www.boomplay.com/artists/1121307",
        "first_10": True
    },
    {
        "name": "Theophilus Sunday",
        "url": "https://www.boomplay.com/artists/19595684"
    },
    {
        "name": "Folabi Nuel",
        "url": "https://www.boomplay.com/artists/717980",
        "first_10": True
    },
    {
        "name": "William McDowell",
        "url": "https://www.boomplay.com/artists/2668277"
    },
    {
        "name": "Monique",
        "url": "https://www.boomplay.com/artists/1160",
        "first_10": True
    },
    {
        "name": "Gbenga Akinfenwa",
        "url": "https://www.boomplay.com/artists/1567093",
        "first_10": True
    },
    {
        "name": "Travis Greene",
        "url": "https://www.boomplay.com/artists/2946434"
    },
    {
        "name": "Kirk Franklin",
        "url": "https://www.boomplay.com/artists/2773534"
    },
    {
        "name": "Jonathan McReynolds",
        "url": "https://www.boomplay.com/artists/2731259"
    },
    {
        "name": "Maranatha! Music",
        "url": "https://www.boomplay.com/artists/1844643"
    },
    {
        "name": "David Dam",
        "url": "https://www.boomplay.com/artists/7980071",
        "first_10": True
    },
    {
        "name": "Odunayo Adebayo",
        "url": "https://www.boomplay.com/artists/28529050",
        "first_10": True
    },
    {
        "name": "Chris Delvan Gwamna",
        "url": "https://www.boomplay.com/artists/19059179"
    },
    {
        "name": "Joe Mettle",
        "url": "https://www.boomplay.com/artists/168543",
        "first_10": True
    },
    {
        "name": "Michael W. Smith",
        "url": "https://www.boomplay.com/artists/2001243"
    },
    {
        "name": "Jesus Image",
        "url": "https://www.boomplay.com/artists/43556160"
    },
    {
        "name": "Midnight Crew",
        "url": "https://www.boomplay.com/artists/13796"
    },
    {
        "name": "Matt Redman",
        "url": "https://www.boomplay.com/artists/1932498"
    },
    {
        "name": "Cody Carnes",
        "url": "https://www.boomplay.com/artists/1946356"
    },
    {
        "name": "Sonnie Badu",
        "url": "https://www.boomplay.com/artists/50388"
    },
    {
        "name": "Gaise Baba",
        "url": "https://www.boomplay.com/artists/3108218",
        "first_10": True
    },
    {
        "name": "Darlene Zschech",
        "url": "https://www.boomplay.com/artists/2944783"
    },
    {
        "name": "Minstrel T-Philz",
        "url": "https://www.boomplay.com/artists/50871716",
        "first_10": True
    },
    {
        "name": "Kenny Kore",
        "url": "https://www.boomplay.com/artists/3373184",
        "first_10": True
    },
    {
        "name": "Voice Of The Cross",
        "url": "https://www.boomplay.com/artists/46067161"
    },
    {
        "name": "Joshua Banjo",
        "url": "https://www.boomplay.com/artists/44988803",
        "first_10": True
    },
    {
        "name": "Women Of Faith",
        "url": "https://www.boomplay.com/artists/4837760"
    },
    {
        "name": "Princess Njideka",
        "url": "https://www.boomplay.com/artists/7472389"
    },
    {
        "name": "Benita Okojie",
        "url": "https://www.boomplay.com/artists/12354",
        "first_10": True
    },
    {
        "name": "ELI-J",
        "url": "https://www.boomplay.com/artists/2440877",
        "first_10": True
    },
    {
        "name": "BUKOLA BEKES",
        "url": "https://www.boomplay.com/artists/36431032",
        "first_10": True
    },
    {
        "name": "Mali Music",
        "url": "https://www.boomplay.com/artists/3689686",
        "first_10": True
    },
    {
        "name": "Donnie McClurkin",
        "url": "https://www.boomplay.com/artists/132429"
    },
    {
        "name": "Todd Galberth",
        "url": "https://www.boomplay.com/artists/526152",
        "first_10": True
    },
    {
        "name": "Florocka",
        "url": "https://www.boomplay.com/artists/1689609"
    },
    {
        "name": "VaShawn Mitchell",
        "url": "https://www.boomplay.com/artists/1946679"
    },
    {
        "name": "Lionel Peterson",
        "url": "https://www.boomplay.com/artists/3045506"
    },
    {
        "name": "Marvin Sapp",
        "url": "https://www.boomplay.com/artists/3690716",
        "first_10": True
    },
    {
        "name": "E-Daniels",
        "url": "https://www.boomplay.com/artists/287009",
        "first_10": True
    },
    {
        "name": "Israel Houghton",
        "url": "https://www.boomplay.com/artists/2946978"
    },
    {
        "name": "Tauren Wells",
        "url": "https://www.boomplay.com/artists/3488394",
        "first_10": True
    },
    {
        "name": "Uche Agu",
        "url": "https://www.boomplay.com/artists/2092616"
    },
    {
        "name": "Planetshakers",
        "url": "https://www.boomplay.com/artists/147836"
    },
    {
        "name": "Sinmidele",
        "url": "https://www.boomplay.com/artists/6267229",
        "first_10": True
    },
    {
        "name": "Fred Hammond",
        "url": "https://www.boomplay.com/artists/3042370"
    },
    {
        "name": "Steffany Gretzinger",
        "url": "https://www.boomplay.com/artists/995140",
        "first_10": True
    },
    {
        "name": "Hillsong Kids",
        "url": "https://www.boomplay.com/artists/5675924"
    },
    {
        "name": "UPPERROOM",
        "url": "https://www.boomplay.com/artists/1074404"
    },
    {
        "name": "Newsboys",
        "url": "https://www.boomplay.com/artists/163510"
    },
    {
        "name": "Femi Okunuga",
        "url": "https://www.boomplay.com/artists/2826918"
    },
    {
        "name": "Donald Lawrence & The Tri-City Singers",
        "url": "https://www.boomplay.com/artists/1947169"
    },
    {
        "name": "Pat Uwaje-King",
        "url": "https://www.boomplay.com/artists/63124"
    },
    {
        "name": "Josiah Queen",
        "url": "https://www.boomplay.com/artists/46825198"
    },
    {
        "name": "Yolanda Adams",
        "url": "https://www.boomplay.com/artists/128988"
    },
    {
        "name": "Mosaic MSC",
        "url": "https://www.boomplay.com/artists/4206631"
    },
    {
        "name": "CityAlight",
        "url": "https://www.boomplay.com/artists/360303"
    },
    {
        "name": "Anne Wilson",
        "url": "https://www.boomplay.com/artists/24193560",
        "first_10": True
    },
    {
        "name": "Dr Becky Paul-Enenche",
        "url": "https://www.boomplay.com/artists/7106536",
        "first_10": True
    },
    {
        "name": "Jahdiel",
        "url": "https://www.boomplay.com/artists/110469",
        "first_10": True
    },
    {
        "name": "VOUS Worship",
        "url": "https://www.boomplay.com/artists/30607476",
        "first_10": True
    },
    {
        "name": "Matthew West",
        "url": "https://www.boomplay.com/artists/1932768"
    },
    {
        "name": "We The Kingdom",
        "url": "https://www.boomplay.com/artists/3932854",
        "first_10": True
    },
    {
        "name": "Geoffrey Golden",
        "url": "https://www.boomplay.com/artists/3039888",
        "first_10": True
    },
    {
        "name": "Pat Barrett",
        "url": "https://www.boomplay.com/artists/2150755",
        "first_10": True
    },
]
# artists = [
#     {
#         "name": "Esther Oji",
#         "url": "https://www.boomplay.com/artists/2446795",
#         "first_10": True
#     },
#     {
#         "name": "Spirit of Prophecy",
#         "url": "https://www.boomplay.com/artists/44708572",
#         "first_10": True
#     }
# ]
def get_lyrics_from_lyrics_pages (lyrics_page_url):
    try:
        lyrics_response = requests.get(lyrics_page_url)
        lyrics_soup = BeautifulSoup(lyrics_response.content, "html.parser")

        title = lyrics_soup.find(name="h1").text.replace("Lyrics", "").strip()
        artist = lyrics_soup.find(name="a", class_="ownerWrap").text.replace("Artist: ", "").strip()
        album = lyrics_soup.find(name="a", class_="ownerWrap_album").text.replace("Album: ", "").strip()
        lyrics = lyrics_soup.find(name="div", class_="lyrics").get_text(separator='\n').strip()
        lyrics = lyrics[lyrics.find("...") + 3:len(lyrics)].replace("........", "").strip()

        if lyrics.lower() == "no lyrics yet" or len(lyrics) <= 250:
            print("Do nothing")
        else:
            temp_song = {
                "lyrics": lyrics,
                "title": title,
                "album": album,
                "cover": "",
                "artist": artist,
            }
            songs_data.append(temp_song)
        # print("Success extracting song")
    except Exception as e:
        print(e)
        print("Error retrieving lyrics for: ", lyrics_page_url.replace("https://www.boomplay.com", ""))


def get_lyrics_pages_from_artists(artist):
    try:
        response = requests.get(artist["url"])
        soup = BeautifulSoup(response.content, "html.parser")
        songs = soup.findAll(name="a", class_="songName")
        for index, song in enumerate(songs):
            numbers = re.findall(r'\d{5,}', str(song))
            if len(numbers) > 0:
                lyrics_url = "https://www.boomplay.com/lyrics/" + (numbers[0])
                get_lyrics_from_lyrics_pages(lyrics_url)
            if index >= 10 and artist.get("first_10"):
                break

        print("Success retrieving all lyrics for", artist["name"])

        for row in songs_data:
            data.append(list(row.values()))

        with open("lyrics_data_boomplay_3.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

        print("CSV data written")

    except Exception as e:
        print("Error retrieving lyric page for: ", artist["url"].replace("https://www.boomplay.com", ""))

for artist in artists:
    get_lyrics_pages_from_artists(artist)
