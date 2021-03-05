#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Tournament:
    def __init__(self, identity="", name="", place="", starting_date="", ending_date="", kind="", description="", number_of_round=4):
        self.identity = identity
        self.name = name
        self.place = place
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.kind = kind
        self.description = description
        self.number_of_round = number_of_round
        self.players_id = []
        self.rounds = []
        self.players_id_sorted = []

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

    def edit_players_id(self,player_id):
        self.players_id.append(player_id)

    def add_a_round(self, round):
        self.rounds.append(round)

    def edit_players_id_sorted(self,player_id):
        self.players_id_sorted.append(player_id)

if __name__ == "__main__":
    print("can't be run")
