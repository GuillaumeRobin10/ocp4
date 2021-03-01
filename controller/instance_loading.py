#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json


def load_a_json_files(tournament_file="databases/tournaments/1_test.json"):
    dict={}
    with open(tournament_file) as files:
        data = json.load(files)
    for entry in data:
        dict.update(entry["content"])
    return dict


if __name__ == "__main__":
    print("can't be run")
