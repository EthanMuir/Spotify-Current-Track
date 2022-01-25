import time

import requests

SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'
SPOTIFY_ACCESS_TOKEN = ''

def get_current_track(access_token):
    response = requests.get(
        SPOTIFY_GET_CURRENT_TRACK_URL,
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )
    resp_json = response.json()

    track_name = resp_json['item']['name']
    artists = resp_json['item']['artists']
    artist_names = ', '.join(
        [artist['name'] for artist in artists]
    )

    current_track_info = "Current Track Is: " + track_name + ", By: " + artist_names
    

    return current_track_info

def main():

    current_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)
    print(current_track_info)

    while True:

        last_track_info = current_track_info
        current_track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)

        if last_track_info != current_track_info:

            print(current_track_info)

        time.sleep(1)

    
    
if __name__ == '__main__':
    main()