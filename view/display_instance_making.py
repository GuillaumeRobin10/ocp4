#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from controller.Display import display, type_str
from controller.building import make_a_tournament, make_a_player

from view.tools import display_head_menu


def display_make_a_tournament():
    """ Display the tournament making menu, using no attribute"""
    os.system('cls||clear')
    display_head_menu("tournament Building")
    tournament_dict = {"name": display("Nom: ")}
    tournament_dict.update({"place": display("Lieu: ")})
    tournament_dict.update({"starting_date": display("Date de début: ", "date")})
    tournament_dict.update({"ending_date": display("Date de fin: ", "date", "", tournament_dict["starting_date"])})
    tournament_dict.update({"kind": type_str()})
    print(f'Type : {tournament_dict["kind"]}')
    tournament_dict.update({"number_of_round": display("Nombre de ronde: ", "int")})
    tournament_dict.update({"description": display("Description: ")})
    return make_a_tournament(tournament_dict)


def display_make_a_player():
    """ Display the player making menu, using no attribute"""
    os.system('cls||clear')
    display_head_menu("Création de joueur")
    player_dict = {"lastname": display("Nom: ")}
    player_dict.update({"firstname": display("Prénom: ")})
    player_dict.update({"gender": display("Genre : (homme/femme)", "gender")})
    player_dict.update({"date_of_birth": display("Date de naissance: ", "date")})
    player_dict.update({"ranking": display("Classement : ", "natural")})
    return make_a_player(player_dict)


if __name__ == "__main__":
    print("can't be run")
