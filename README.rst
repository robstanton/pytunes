pytunes
=======

Features
--------

* Combines two music libraries together
* These libraries can be from itunes or any arbitory folder structure
* Finds all music files  in these libraries and gets their metadata from their tags
* For songs that don't have full tags, it gets the metadata from Discogs
* Initial de-dupes songs in each library based on tags for Artist, Album and song
* For duplicates, it chooses the best quality version
* Builds a new library containing only unique songs
* This new library is recorded in SQLlite so reports can be created
* All songs are re-tagged using Discogs metadata
* Discogs API calls are cached to speed things up
* Oraganises new library by Artist > Album > Songs
* Songs with no album are put the root of the artists folder
* Filename is set at "ARTIST_SONG_TITLE"
