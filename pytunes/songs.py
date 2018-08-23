# Module containing all methods for dealing with songs

import os

  
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
    """Return a tuple containing the tags and other metadata for the song."""
    pass
