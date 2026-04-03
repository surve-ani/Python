import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify auth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="d6104c2733104c6d97d57f5d99e7f36a",
    client_secret="142d07e8f1de486b9c1b6fc21abbef26",
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-modify-playback-state user-read-playback-state user-library-read user-follow-read playlist-read-private playlist-read-collaborative",
    cache_path=".cache",
    open_browser=False
))

# ---------------------- Get a Song URI ----------------------
results = sp.current_user_followed_artists(limit=1)
artists = results['artists']['items']
if not artists:
    print("❌ No followed artists found.")
    exit()

artist = artists[0]
top_tracks = sp.artist_top_tracks(artist['id'], country='IN')
if not top_tracks['tracks']:
    print("❌ No top tracks found for artist.")
    exit()

track = top_tracks['tracks'][0]
track_name = track['name']
track_uri = track['uri']
artist_name = artist['name']

print(f"🎵 Found track: '{track_name}' by {artist_name}")
print(f"📡 Spotify URI: {track_uri}")

# 2. Play on Sonos via Home Assistant
HOME_ASSISTANT_IP = "192.168.40.6"
home_assistant_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiI0N2YyMGU0Njg1MTg0NTJiOWZmOTI4MzdhZDkyMmU0NCIsImlhdCI6MTc1MjQ2ODMzMiwiZXhwIjoxNzg0MDA0MzMyfQ.Piq-mwNlBaBbeBvB5aZoo2nkNCk0PFt7myrnYPAgAUI"
sonos_entity_id = "media_player.den"  # Replace with actual entity_id in HA

url = f"http://{HOME_ASSISTANT_IP}:8123/api/services/media_player/play_media"

headers = {
    "Authorization": f"Bearer {home_assistant_token}",
    "Content-Type": "application/json"
}

payload = {
    "entity_id": sonos_entity_id,
    "media_content_id": track_uri,
    "media_content_type": "spotify"
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    print(f"✅ Playing '{track_name}' on Sonos via Home Assistant.")
else:
    print(f"❌ Error: {response.status_code} - {response.text}")
