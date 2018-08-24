

import pytunes.songs as songs
import os
import pytest


    
def test_handles_invalid_mp3():
    songs.get_song_metadata("tests/testdata/lib1/music/notanmp3.mp3") is None

      
      
def test_validates_path(tmpdir):
    with pytest.raises(ValueError):
      returned = songs.get_songs_from_library('/fake/path')
    
    
    
def test_returns_list(tmpdir):
    returned = songs.get_songs_from_library(tmpdir)
    assert  isinstance(returned, list)
    


    
