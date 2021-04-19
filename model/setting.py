#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import mkdir
from tinydb import TinyDB

try:
    mkdir("data")
except FileExistsError:
    pass
db = TinyDB("data/databases.json")
