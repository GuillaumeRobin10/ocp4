#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Tournament:
    def __init__(self, name, place, kind, players=[], number_of_turn=4):
        self.name = name
        self.place = place
        self.number_of_turn = number_of_turn
        self.kind = kind
        self.players = players

    def add_player(self, player):
        self.players.append(player)

    def display_player(self):
        for player in self.players:
            print(player.lastname)
            print(player.firstname)
            print(player.elo)
            print(player.sex)

    def display(self):
        print(self.name)
        print(self.place)
        print(self.kind)
        print(self.number_of_turn)


class Player:
    def __init__(self, lastname, firstname, date_of_birth, sex, elo, point=0):
        self.lastname = lastname
        self.firstname = firstname
        self.date_of_birth = date_of_birth
        self.sex = sex
        self.elo = elo
        self.point = point

    def remove_elo(self, remove_e=0):
        self.elo -= int(remove_e)

    def remove_point(self, remove_p):
        self.point -= int(remove_p)

    def add_point(self, add_p):
        self.point += int(add_p)
        
    def rename_firstname(self, name):
        self.firstname = name

    def rename_lastname(self, lastname):
        self.lastname = lastname
