#!/usr/bin python
'''
' COEN 281
' Team 9
' This script requests user for song name, searches for and downloads its features to file.
'''

import sys, os, requests, json
from pyechonest import song as sng
from pyechonest import config
config.ECHO_NEST_API_KEY = "PUWRUFW0PGBFUACZC"
DEBUG = False
OUTPUT_FILE = "_testcase"
fh = open(OUTPUT_FILE, "w")

##############
## USER INPUT

while not DEBUG:
    songname = str(raw_input("\nSong name?? "))
    ts_results = sng.search(title=songname)    
    if ts_results:  #got some search results
        print ("Found song by user "+ts_results[0].artist_name+" - "+ts_results[0].title)
        resp = str(raw_input("Fetch this song? [y/n] "))
        if "y" in resp.lower():
            print("Fetching...")
            break
    else:
        print "No such song found."

############################
## DOWNLOAD TIMBRE FEATURES

fh.write("# "+ts.title+" - "+ts.artist_name+"\n") #first line of file = songname

ts = ts_results[0]
audsum = requests.get(ts.audio_summary['analysis_url']).text
for seg in json.loads(audsum)['segments']:
    line = ",".join(map(str,seg['timbre'])) #convert each segment into comma-delimited line
    fh.write(line+"\n")


