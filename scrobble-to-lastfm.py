#/usr/bin/python
import os
import sys
import time
import pylast
import subprocess

artist = sys.argv[1] 
album = sys.argv[2] 
title = sys.argv[3]
timestamp = sys.argv[4]

# Update your credentials here
network = pylast.LastFMNetwork(api_key="", api_secret="",
                               username="", password_hash=pylast.md5(""))

network.scrobble(artist = artist, title = title, album = album, timestamp = timestamp)
print("LAST.FM: Scrobbled successfully {0} - {2} (from album {1})").format(artist, album, title)