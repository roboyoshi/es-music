# !/usr/bin/python3
# Music Library Parser

import sys
import getopt
import os
import json
import math
import mutagen
from pprint import pprint as pp

# TODO: Write a spec for this object
# So we have a "clean" json output
# that we can use for JavaScript Stuff
# Or ElasticSearch indexing.
class Track(dict):
    def __str__(self):
        return json.dumps(self)

def print_usage():
    print("Usage: parser.py -library <path/to/music>")

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help", "library="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err) # will print something like "option -a not recognized"
        print_usage()
        sys.exit(2)
    library = None
    for option, value in opts:
        if option in ("-h", "--help"):
            print_usage()
            sys.exit()
        elif option in ("-library", "--library"):
            library = value
    if library is None:
        print_usage()
        sys.exit(2)
    # --------------------------------------------------------
    library = os.path.expanduser(library)
    os.chdir(library)
    for root, dirs, files in os.walk(".", topdown = False):
        for name in files:
            fpath = os.path.join(root, name)
            try:
                # print(fpath)
                m = mutagen.File(fpath, easy=True)
                kbps = math.floor(m.info.bitrate / 1024)
                track = Track()
                track['artist'] = m['artist'][0]
                track['album'] = m['album'][0]
                track['title'] = m['title'][0]
                track['format'] = str.lower(os.path.splitext(fpath)[1])
                track['kbps'] = kbps
                print(track)
            except:
                continue

if __name__ == "__main__":
   main()