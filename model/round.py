#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Round:
    def __init__(self, tournament_id, name="hello", starting_date="hello", ending_date="hello"):
        self.matches = []
        self.sorted_players_id = []
        self.tournament_id = tournament_id
        self.name = name
        self.starting_date = starting_date
        self.ending_date = ending_date
        self.serialized_round = {}

    def edit_sorted_players(self, sorted_players_id):
        self.sorted_players_id = sorted_players_id

    def edit_matches(self, matches):
        self.matches = matches

    def edit_name(self, new_name):
        self.name = new_name

    def edit_starting_date(self, new_starting_date):
        self.starting_date = new_starting_date

    def edit_ending_date(self, new_ending_date):
        self.ending_date = new_ending_date

    def first_matchmaking(self):
        top_list = []
        low_list = []
        for _ in range(4):
            top_list.append(self.sorted_players_id.pop(0))
            print(top_list)
        for _ in range(4):
            low_list.append(self.sorted_players_id.pop(0))
        for _ in range(4):
            self.matches.append(([top_list.pop(0), 0], [low_list.pop(0), 0]))

    def serialization(self):
        self.serialized_round.update({"matches": self.matches,
                                      "name": self.name,
                                      "starting_date": self.starting_date,
                                      "ending_date": self.ending_date})


if __name__ == "__main__":
    print("can't be run")
