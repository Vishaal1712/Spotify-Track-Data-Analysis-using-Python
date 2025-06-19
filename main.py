from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re

#  step 1 setup the client credentials

sp = spotipy.Spotify(oauth_manager=SpotifyClientCredentials(
    client_id='8f4905963bd14bc3b6ca4ff65afa6cf8',
    client_secret='c07e1379cee849f4bce2233264fe395b'
))

# step 2 track url to our project

track_url = 'https://open.spotify.com/track/0nrJ7jsUFR0pDHV6NvKJje'

# Step 3 track id extract
track_id = re.search(r'track/([a-zA-Z0-9]+)',track_url).group(1)
# print(track_id) this line used the check the above code is working properly 

# track detail 
track = sp.track(track_id)
# print(track)
    
# track details
track_data = {
    'Track name': track['name'],
    'Artists': track['artists'][0]['name'],
    'Album': track['album']['name'],
    'Popularity':track['popularity'],
    'Duration (min)': track['duration_ms']/60000
}

# display the metadata
print(f'\n Track name: {track_data['Track name']}')
print(f' Artists name: {track_data['Artists']}')
print(f' Album name: {track_data["Album"]}')
print(f' popularity: {track_data["Popularity"]}')
print(f' Duration: {track_data["Duration (min)"]:.2F} minutes') 

# convert the metadata to data frame 

df = pd.DataFrame([track_data])
print('\n Tack data as data frame')
print(df)

#  metadata to csv file

df.to_csv('spotify_track_data.csv', index=False)

# visualize track data 

features = ['popularity','Duration (min)']
value = [track_data['Popularity'],track_data['Duration (min)']]

plt.figure(figsize=(8, 5))
plt.bar(features,value, color='skyblue', edgecolor= 'black')
plt.title(f'Track metadata for {track_data['Track name']}')
plt.ylabel('Value')
plt.show()