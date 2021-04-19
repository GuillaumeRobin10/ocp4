#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import mkdir
from tinydb import TinyDB

try:
    mkdir("data")
    with open("databases.json", "w"):
        pass
except FileExistsError:
    pass
db = TinyDB("data/databases.json")
