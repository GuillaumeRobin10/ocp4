#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tinydb import TinyDB
from os import path


class Tournament:

    def __init__(self, name="", place="", kind="", number_of_round=0, starting_date="", ending_date="", description=""):
        self.name = name
        self.place = place
        self.kind = kind
        self.number_of_round = number_of_round
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.serialized_tournament = {}
        self.players = []
        self.rounds = [[(1-5), (2-6), (3-7), (4-8)]]
        self.description = description
        # round 0 = [0]
        # match 1 = [0][0]
        self.id = 0

    def edit_name(self, name):
        self.name = name

    def edit_place(self, place):
        self.place = place

    def edit_kind(self, kind):
        self.kind = kind

    def edit_number_of_turn(self, number_of_turn):
        self.number_of_turn = number_of_turn

    def edit_starting_date(self, starting_date):
        self.starting_date = starting_date

    def edit_ending_date(self, ending_date):
        self.ending_date = ending_date

    def add_a_player(self, player_id):
        self.players.append(player_id)

    def add_a_round(self, round_id):
        self.rounds.append(round_id)

    def __serialized(self):
        self.serialized_tournament.update({
            "name": self.name,
            "place": self.place,
            "kind": self.kind,
            "number_of_round": self.number_of_round,
            "starting_date": self.starting_date,
            "ending_date": self.ending_date,
            "List_players": self.players,
            "description": self.description})

    def save(self):
        tournament_files_name = f"../databases/tournament/{self.id}_{self.name}.json"
        self.__serialized()
        if path.isfile(tournament_files_name):
            player_db = TinyDB(tournament_files_name)
            player_db.update(self.serialized_tournament)
            print("editing")
        else:
            player_db = TinyDB(tournament_files_name)
            player_db.insert(self.serialized_tournament)
            print("New")


if __name__ == "__main__":
    print("can't be run")
