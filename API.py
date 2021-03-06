import requests
import os

ITUNES_URL = 'https://itunes.apple.com/search'

params = {
    'tern': 'Монеточка',
    'limit': 200,
    'media': 'music',
    'country': 'ru'
}

headers = {
    'User_Agent': 'Python Netology'
}

resp = requests.get(ITUNES_URL, params=params, headers=headers)

resp_json = resp.json()

for track in resp_json['results']:
    print('*'*30)
    print(track)

    track_id, track_name, artist = track['trackId'], track['trackName'], track['artistName']
    file_name = f'{track_id}-{track_name}-{artist}.jpg'
    full_file_name = os.path.join('covers', file_name)
    print("Filename", full_file_name)

    with open (full_file_name, 'wb') as f:
        img_url = track['artworkUrl100']
        img_file_resp = requests.get(img_url)
        img = img_file_resp.content

        f.write(img)