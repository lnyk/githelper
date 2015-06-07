#!/usr/bin/env python2

"""githelper.py [option]

Author: William Yao <LNYK@ME.COM> at <LNYK2.COM>

Used to operate git in a short hand with these options:

BEWARE OF THE ORDER OF OPTIONS!

-a\t\t->\tAdd --all

-c <comment>\t->\tcommit with comment message

-p\t\t->\tpush to origin

-s\t\t->\tgit status

-C <comment>\t->\tAdd., commit with comment message and push.
\t\t\tLike: -a -c "comment" -p -s
"""
import sys
import getopt
import os

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        try:
            opts, args = getopt.getopt(argv[1:], "hov:c:apyzsC:", ["help", "output="])
        except getopt.error, msg:
             raise Usage(msg)

        # option processing
        for option, value in opts:
            if option == "-v":
                verbose = True
            if option in ("-h", "--help"):
                raise Usage(__doc__)
            if option in ("-o", "--output"):
                output = value
            if option == "-a":
                gadd()
            if option == "-c":
                gcommit(value)
            if option == "-p":
                gpush()
            if option == "-s":
                print "=" * 10
                os.system("git status")
            if option == "-C":
                gadd()
                gcommit(value)
                gpush()
                print "=" * 10
                os.system("git status")

    except Usage, err:
        print >>sys.stderr, sys.argv[0].split("/")[-1] + ": " + str(err.msg)
        #print >>sys.stderr, "	 for help use --help"
        return 2

def gadd():
    print "=" * 10
    os.system("git add --all")
    print "Added everything to stash."

def gcommit(value):
    print "=" * 10
    os.system("git commit -m \"" + value + "\"")

def gpush():
    print "=" * 10
    os.system("git push")

if __name__ == "__main__":
    sys.exit(main())
