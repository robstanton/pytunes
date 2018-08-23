# Module containing all methods for dealing with songs

import os
import eyed3

  
def get_songs_from_library(path):
    # Return a list of tuples containing all the songs found in a directory and it's subdirectories
    try:
        # Check the path points to a valid directory
        if os.path.isdir(path) is False:
            raise ValueError('Error: Not a valid directory')
            print ('That is not a valid directory')
    except ValueError as err:
        raise
    
    songs = []
    return songs
        
  
def get_song_metadata(path):
    #Return a dictionary containing the tags and other metadata for a song#
    try:
        # Read tags from file, raise error if can't
        tags = eyed3.load(path)
        if tags is None:
            msg = path + " is not a valid mp3 file"
            raise ValueError(msg)
    except ValueError as err:
        print(err)
        raise
    pass
