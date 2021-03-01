#!/usr/bin/env python
# -*- coding: utf-8 -*-
import glob


def get_datafiles(source='databases/tournaments/*.json'):
    listing = {}
    for files in glob.glob(source):
        test = files.split("/")
        id = test[-1].split("_")[0]
        name = test[-1].split("_")[1].split(".")[0]
        listing.update({id: name})
    return listing


if __name__ == "__main__":
    print("can't be run")