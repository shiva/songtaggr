#!/usr/bin/env python3
"""Song tagger in python

Tags the specified file list with given tags

Usage: python3 tag.py [options] [source]

Options:
  -a ..., --artist=...    use specified artist
  -l ..., --album=...     use specified album
  -g ..., --genre=...     use specified genre
  -h, --help              show this help
  -d                      show debugging information while parsing

Examples:
  tag.py file1.mp3 file2.mp3     displays tag content of each file
  tag.py -a "The Doors" file1.mp3  Changes file1.mp3's artist tag to "The Doors"

"""

__author__ = "Shiva Velmurugan(shiv@shiv.me)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2011/03/06 22:24:23 $"
__copyright__ = "Copyright (c) 2011 Shivanand Velmurugan"
__license__ = "Python"

import sys
import getopt
import songdetails

def usage():
    print (__doc__)

def printsong(song):
    if song is not None:
        print ("Title: ", song.title)
        print ("Artist: ", song.artist)
        print ("Album: ", song.album)
        print ("Genre: ", song.genre)


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "ha:l:g:d", ["help", "artist=", "album=", "genre="]) 
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt == '-d':
            global _debug
            _debug = 1
        elif opt in ("-a", "--artist"):
            print ("Found artist: ", arg)
            artist = arg
        elif opt in ("-l", "--album"):
            print ("Found album: ", arg)
            album = arg
        elif opt in ("-g", "--genre"):
            print ("Found genre: ", arg)
            genre = arg

    for file in args:
        print ("file: ", file)
        song = songdetails.scan(file)
        printsong(song)


if __name__ == "__main__":
    main(sys.argv[1:])
