# Module containing all methods for dealing with songs

import os
import eyed3

  
def get_songs_from_library(path):
    # Returns a dict of all the songs found in a directory and it's subdirectories, the key for the dict is artist:albulm:song
    songs = {}
    try:
        # Check the path points to a valid directory
        if os.path.isdir(path) is False:
            print ('That is not a valid directory')
            raise ValueError('Error: Not a valid directory')
    except ValueError as err:
        raise
    
    for root, directories, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root,filename)
            song = get_song_metadata(path)
            if song is not None:
                song_key = ""
                sub_keys = [song["artist"],song["album"],song["title"]]
                for k in sub_keys:
                    if k is not None:
                        k =  k.replace(" ", "").upper()
                    else:
                        k = "UNKNOWN"
                    
                    song_key = song_key + ":" + k
                   
                
                print ("song_key is " + song_key)           
                songs[song_key] = song
                
                
    
    return songs
        
  
def get_song_metadata(path):
    #Return a dictionary containing the tags and other metadata for a song#
    song_data = {}
    # Read tags from file and returns them, if not MP3 then returns None
    song = eyed3.load(path)
    if song is None:
        msg = path + " is not a valid mp3 file"
        print (msg)
        song_data = None
    else:
       
        song_data.update(
            [
                
                ('artist', song.tag.artist) ,
                ('title', song.tag.title) ,
                ('album', song.tag.album) , 
                ('album_artist', song.tag.album_artist),
                ('track_num', song.tag.track_num),
                ('genre_name', song.tag.genre.name if song.tag.genre is not None else None),
                ('genre_id', song.tag.genre.id if song.tag.genre is not None else None),
                ('time_secs', song.info.time_secs),
                ('size_bytes', song.info.size_bytes),
                ('file_name', os.path.basename(song.path)),
                ('path', song.path) 
                
            ]
        )
        
    return song_data
    
