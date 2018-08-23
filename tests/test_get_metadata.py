

import pytunes.songs as songs
import os
import pytest


def test_returns_list(tmpdir):
    returned = songs.get_songs_from_library(tmpdir)
    assert  isinstance(returned, list) 
    
def test_validates_path(tmpdir):
    with pytest.raises(ValueError):
      returned = songs.get_songs_from_library('/fake/path')
    
