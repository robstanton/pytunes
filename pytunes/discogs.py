#Deals with all Discogs features

import requests
import pytunes.local_config as local_config
from fuzzywuzzy import fuzz
from operator import itemgetter

def get_sec(time_str):
    m, s = time_str.split(':')
    return  int(m) * 60 + int(s)

def search_for_song_data(query):
  payload = {'q': query, 'key': local_config.consumer_key,'secret': local_config.consumer_secret}
  initial_search_result = requests.get('https://api.discogs.com/database/search', params=payload).json()
  master_rescord = initial_search_result['results'][0]
  release_details = requests.get(master_rescord['resource_url']).json()
  
  song_data = {}
  
  # Get the artists for the release
  release_artist = ''
  for a in release_details['artists']:
    release_artist += a['name']
    if a['join'] != '':
      join = ' ' + a['join'] + ' '
      release_artist += join
      
  # Get the tracks from the release
  tracks = []
  for t in release_details['tracklist']:
    if t['type_'] == 'track':
      
      # Score the track title on how close it is to our search
      match_score = fuzz.token_set_ratio(t['title'],query)
      
      # Get the artists for the track
      track_artist = ''
      if 'artists' in t:
        for a in t['artists']:
          track_artist += a['name']
          if a['join'] != '':
            join = ' ' + a['join'] + ' '
            track_artist += join
      else:
        track_artist = release_artist
      
      track_data = {
                      'track_title' : t['title'],
                      'match_score' : match_score,
                      'track_artist' : track_artist,
                      'track_duration': get_sec(t['duration'])
                      
                    }
      tracks.append(track_data)
  
  #Select the track with the highest match score
  sorted_tracks = sorted(tracks, key=itemgetter('match_score'),reverse=True) 
  track_details = sorted_tracks[0]
  
  
  song_data.update(
            [
                
                ('artist', track_details['track_artist']) ,
                ('title', track_details['track_title']) ,
                ('album', release_details['title']) , 
                ('album_artist', release_artist),
               # ('track_num', song.tag.track_num),
               # ('genre_name', song.tag.genre.name if song.tag.genre is not None else None),
               # ('genre_id', song.tag.genre.id if song.tag.genre is not None else None),
               # ('time_secs', song.info.time_secs),
               # ('size_bytes', song.info.size_bytes),
               # ('file_name', os.path.basename(song.path)),
               # ('path', song.path) 
                
            ]
        )
        
  print(song_data)
  
  
  pass
  
