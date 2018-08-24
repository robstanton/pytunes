# Module containing all methods for dealing with songs

import os
import eyed3

  
def get_songs_from_library(path):
    # Return a list of dictionarys containing all the songs found in a directory and it's subdirectories
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
            #print (filename)
            #print (os.path.join(root,filename))
            
    songs = []
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
                ('title', song.tag.artist) ,
                ('album', song.tag.artist) , 
                ('album_artist', song.tag.album_artist) 
            ]
        )
        print(song_data)
    return song_data
    
