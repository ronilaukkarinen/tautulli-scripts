#/usr/bin/python
import os
import sys
import time
import pylast
import subprocess

artist = sys.argv[1] 
album = sys.argv[2] 
title = sys.argv[3]
seconds = int(sys.argv[4])
duration = int(sys.argv[4]) - int( seconds / 3.5 )

print("PLEX: Trying to get metadata for: {0} / {1} / {2} / {3}").format(artist, album, title, duration)

# Update your credentials here
network = pylast.LastFMNetwork(api_key="", api_secret="",
                               username="", password_hash=pylast.md5(""))

network.update_now_playing(artist = artist, album = album, title = title, duration = duration)
print("LAST.FM: Updated now playing status successfully for {0} - {2} (from album {1})").format(artist, album, title)