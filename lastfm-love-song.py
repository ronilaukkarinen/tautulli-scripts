#/usr/bin/python
import os
import sys
import time
import pylast
import subprocess

artist = sys.argv[1] 
title = sys.argv[3]

# Update your credentials here
network = pylast.LastFMNetwork(api_key="", api_secret="",
                               username="", password_hash=pylast.md5(""))

track = pylast.Track(artist, title, network)
track.love()

print("LAST.FM: Loved a song: {0} - {1}").format(artist, title)