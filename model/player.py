#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Player:
    def __init__(self, lastname="", firstname="", date_of_birth="", gender="", ranking=0, identity="",
                 tournament_point=None):
        self.identity = identity
        self.lastname = lastname
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
        self.tournament_point = tournament_point
        self.serialized_player = {}

    def edit_identity(self, identity):
        self.identity = identity

    def edit_lastname(self, lastname):
        self.lastname = lastname

    def edit_firstname(self, firstname):
        self.firstname = firstname

    def edit_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def edit_gender(self, gender):
        self.gender = gender

    def edit_ranking(self, ranking):
        ranking = abs(ranking)
        self.ranking = ranking

    def add_ranking_point(self, ranking_added):
        ranking_added = abs(ranking_added)
        self.ranking += ranking_added

    def remove_ranking_point(self, ranking_removed):
        ranking_removed = abs(ranking_removed)
        if (self.ranking - ranking_removed) >= 0:
            self.ranking -= ranking_removed
        else:
            print("modification impossible, le classement ne peut pas être inférieur a 0")

    def add_tournament_point(self, identity, added):
        self.tournament_point[identity] += added

    def serialization(self):
        self.serialized_player = {"lastname": self.lastname,
                                  "firstname": self.firstname,
                                  "date_of_birth": self.date_of_birth,
                                  "gender": self.gender,
                                  "ranking": self.ranking,
                                  "identity": self.identity,
                                  "tournament_point": self.tournament_point}


if __name__ == "__main__":
    print("can't be run")
