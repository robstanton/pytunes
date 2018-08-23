

import pytunes.songs as songs
import os
import pytest


    
def test_validates_mp3():
    with pytest.raises(ValueError):
      songs.get_song_metadata("tests/testdata/lib1/music/notanmp3.mp3")
      
      
      

    
