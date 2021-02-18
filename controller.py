#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tinydb import TinyDB,Query
from model import *
import datetime

db=TinyDB("Tournament.json")

def save_a_tournament(tournament):
    db.insert({"Nom":tournament.name})


def make_a_tournament(tournament):
    tournois = Tournament(name=tournament["Nom"],place=tournament["Lieu"],debut=tournament["Debut"],fin=tournament["Fin"],kind=tournament["Type"],number_of_turn=tournament["Round"])
    return tournois

def make_a_player(player):
    player = Player(lastname=player["Nom"],firstname=player["Prenom"],date_of_birth=player["Birthday"],gender=player["Sexe"],elo=player["Classement"])
    return player

def load_a_tournament():
    print("loading")

def control_a_date(string):
    list = string.split("/")
    try :
        year = int(list[2])
        month = int(list[1])
        day = int(list[0])
        datetime.date(year, month, day)
        return True
    except ValueError :
        return False
    except IndexError:
        return False

def control_a_date_after(date1,date2):
    date1list = date1.split("/")
    year1 = int(date1list[2])
    month1 = int(date1list[1])
    day1 = int(date1list[0])
    d1 = datetime.date(year1, month1, day1)
    date2list = date2.split("/")
    year2 = int(date2list[2])
    month2 = int(date2list[1])
    day2 = int(date2list[0])
    d2 = datetime.date(year2, month2, day2)
    if d1 < d2:
        return True
    else :
        return False



if __name__ == "__main__":
    print("can't be run")

