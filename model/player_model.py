#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tinydb import TinyDB
from os import path


class Player:
    def __init__(self, lastname="", firstname="", date_of_birth="", gender="", ranking=0):
        self.id = 0
        self.lastname = lastname
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.ranking = ranking
        self.points = 0
        self.list_of_tournament = 0
        self.serialized_player = {}

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

    def edit_point(self, points):
        points = abs(points)
        self.points = points

    def add_point(self, added):
        added = abs(added)
        self.points += added

    def remove_point(self, removed):
        removed = abs(removed)
        if (self.points - removed) >= 0:
            self.points -= removed
        else:
            print("impossible d'avoir un nombre de point négatifs")

    def __serialized(self):
        self.serialized_player.update({
            "lastname": self.lastname,
            "firstname": self.firstname,
            "date_of_birth": self.date_of_birth,
            "gender": self.gender,
            "ranking": self.ranking,
            "points": self.points,
            "list_of tournament": self.list_of_tournament})

    def save(self):
        player_files_name = f"../databases/players/{self.id}_{self.lastname}_{self.firstname}.json"
        self.__serialized()
        if path.isfile(player_files_name):
            player_db = TinyDB(player_files_name)
            player_db.update(self.serialized_player)
            print("editing")
        else:
            player_db = TinyDB(player_files_name)
            print("New")
            player_db.insert(self.serialized_player)


if __name__ == "__main__":

    magnus = Player()
    magnus.edit_gender("homme")
    magnus.edit_firstname("Magnus")
    magnus.edit_lastname("Carlsen")
    magnus.save()