#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Tournament:
    def __init__(self, identity="1", name="", place="", starting_date="", ending_date="", kind="", description="",
                 number_of_round=4):
        self.identity = identity
        self.name = name
        self.place = place
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.kind = kind
        self.description = description
        self.number_of_round = number_of_round
        self.rounds = []
        self.players_id_sorted = []
        self.serialized_round = []
        self.serialized_tournament = {}
        self.players_id = []

    def edit_id(self, identity):
        self.identity = identity

    def edit_name(self, name):
        self.name = name

    def edit_place(self, place):
        self.place = place

    def edit_starting_date(self, starting_date):
        self.starting_date = starting_date

    def edit_ending_date(self, ending_date):
        self.ending_date = ending_date

    def edit_kind(self, kind):
        self.kind = kind

    def edit_number_of_round(self, number_of_round):
        self.number_of_round = number_of_round

    def edit_description(self, description):
        self.description = description

    def edit_players_id_by_one(self, player_id):
        self.players_id.append(player_id)

    def add_a_round(self, a_round):
        self.rounds.append(a_round)

    def edit_players_id_sorted(self, player_id):
        self.players_id_sorted.append(player_id)

    def edit_serialized_round(self, new_serialized_roud):
        self.serialized_round.append(new_serialized_roud)

    def del_serialized_round(self):
        self.serialized_round = []

    def serialization(self):
        self.serialized_tournament = {"identity": self.identity,
                                      "name": self.name,
                                      "place": self.place,
                                      "starting_date": self.starting_date,
                                      "ending_date": self.ending_date,
                                      "kind": self.kind,
                                      "description": self.description,
                                      "number_of_round": self.number_of_round,
                                      "serialized_round": self.serialized_round,
                                      "players_id": self.players_id}


if __name__ == "__main__":
    print("can't be run")
