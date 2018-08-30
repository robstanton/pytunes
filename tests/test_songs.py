

import pytunes.songs as songs
import os
import pytest





    
def test_handles_invalid_mp3():
    songs.get_song_metadata("tests/testdata/lib1/music/notanmp3.mp3") is None

      
      
def test_validates_path():
    with pytest.raises(ValueError):
      returned = songs.get_songs_from_library("/fake/path")
    
    
    
def test_returns_di(tmpdir):
    returned = songs.get_songs_from_library(tmpdir)
    assert  isinstance(returned, dict)
    
def test_returns__full_metadata():
    song_data = songs.get_song_metadata("tests/testdata/km_song_with_tags.mp3")
    assert song_data["artist"] == "Kirsty MacColl"
    assert song_data["title"] == "Mother's Ruin"
    assert song_data["album"] == "Kite"
    assert song_data["album_artist"] == "Kirsty MacColl"
    assert song_data["track_num"] == (3,15)
    assert song_data["genre_name"] == "Pop"
    assert song_data["genre_id"] == 13
    assert song_data["time_secs"] == 237
    assert song_data["size_bytes"] == 5701991
    assert song_data["file_name"] == "km_song_with_tags.mp3"
    assert song_data["path"].endswith("tests/testdata/km_song_with_tags.mp3")

def test_creates_correct_song_key():
    song_dict = songs.get_songs_from_library("tests/testdata/lib1")
    assert ":KIRSTYMACCOLL:KITE:MOTHER'SRUIN" in song_dict


    
    

    
