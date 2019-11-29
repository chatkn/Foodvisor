#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, getopt
import json
from database import Database

def getJsonFiles(buildFile, extractFile, editsFile):
    buildDict = {}
    extractDict = {}
    editsDict = {}
    with open(buildFile, 'r') as buildData:
        buildDict = json.load(buildData)
    with open(extractFile, 'r') as extractData:
        extractDict = json.load(extractData)
    with open(editsFile, 'r') as editsData:
        editsDict = json.load(editsData)
    return buildDict, extractDict, editsDict

def createDatabase(build, extract, edits):
    if len(build) > 0:
    # Build graph
        db = Database(build[0][0])
        if len(build) > 1:
            db.add_nodes(build[1:])
    # Add extract
        db.add_extract(extract)
    # Graph edits
        db.add_nodes(edits)
    return db

def main(argv):
    usage = "Usage: main.py -b <buildGraphFile> -x <extractImageFile> -e <editedGraphFile>"
    try:
        opts, args = getopt.getopt(argv,"hb:x:e:", ["help, build, extract, edit="])
        if len(argv) != 6:
            print(usage)
            exit()
        build, extract, edits = getJsonFiles(argv[1], argv[3], argv[5])
        db = createDatabase(build, extract, edits)
        status = db.get_extract_status()
        print(status)
        
    except getopt.GetoptError as msg:
        print(msg)
        print(usage)
        sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])