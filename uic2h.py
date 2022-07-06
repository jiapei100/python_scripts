#!/usr/bin/env python

"""uic2h.py: Convert from Qt .ui files to corresponding .h header files."""

__author__      = "Pei Jia"
__copyright__   = "Copyright 2022, Longer Vision Technology"
__version__     = "0.0.1"
__date__        = "2022-07-05"



import sys, os, glob
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder", type=str, help="Please provide a folder containing .ui files.")

    args = parser.parse_args()

    if not os.path.isdir(args.folder):
        print("Folder {} does not exist.".format(args.folder))
        sys.exit(1)


    for file in os.listdir(args.folder):
        # check only text files
        if file.endswith('.ui'):
            hname = args.folder + '/ui_' + file[:-2]+ 'h'
            bashcommand = 'uic ' + args.folder + '/' + file + ' -o ' + hname
            os.system(bashcommand)


