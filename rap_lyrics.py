import requests, json
from lyricsgenius import Genius
from time import sleep

# constant values.
BASE_URL = "https://api.genius.com"
CLIENT_ACCESS_TOKEN = "n8s7RRiDIVsle0hkrdUfG_0g4jTU_D6a1iQTJBNBW7aQj9zNcCOU3NW12lg51EIE"
ARTIST_NAME = "PNL"
genius = Genius(CLIENT_ACCESS_TOKEN)

def _get(path, params=None, headers=None):

    # generate request URL
    requrl = '/'.join([BASE_URL, path])
    token = "Bearer {}".format(CLIENT_ACCESS_TOKEN)
    if headers:
        headers['Authorization'] = token
    else:
        headers = {"Authorization": token}

    response = requests.get(url=requrl, params=params, headers=headers)
    response.raise_for_status()

    return response.json()

def get_album_artist(id_artist):
    albums = genius.artist_albums(id_artist, per_page=None, page=None)
    album = (albums['albums'])
    liste_album = {}
    for x in album:
        liste_album[x['id']] = x['name']

    return liste_album


print("searching " + ARTIST_NAME + "'s artist id. \n")

# find artist id from given data.
find_id = _get("search", {'q': ARTIST_NAME})
for hit in find_id["response"]["hits"]:
   if hit["result"]["primary_artist"]["name"] == ARTIST_NAME:
       artist_id = hit["result"]["primary_artist"]["id"]
       break

print("-> " + ARTIST_NAME + "'s id is " + str(artist_id) + "\n")

for id_album,name_album in get_album_artist(artist_id).items():
    album = genius.album(id_album)
    print(album)
    break

# url = "https://api.genius.com/search?q=Bekar"

# payload={}
# headers = {
#   'Authorization': 'Bearer n8s7RRiDIVsle0hkrdUfG_0g4jTU_D6a1iQTJBNBW7aQj9zNcCOU3NW12lg51EIE',
#   'Accept': 'application/json',
#   'User-Agent': 'CompuServe Classic/1.22',
#   'Host': 'api.genius.com'
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)