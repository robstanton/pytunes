

import pytunes.discogs as discogs
import pytest


def test_search_song_data():
    results = discogs.search_for_song_data('Frankie Knuckles - The Whistle Song')
    assert 1 + 1 == 3


    
    

    
