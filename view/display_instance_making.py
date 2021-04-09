#!/usr/bin/env python
# -*- coding: utf-8 -*-
from controller.Display import display, type_str

from view.tools import display_head_menu


def display_make_a_tournament():
    """
    Display the tournament making menu,
    don't use attribute
    :return: a dictionary
    """
    display_head_menu("Création du tournois")
    tournament_dict = {}
    tournament_dict.update({"name": display("Nom: ")})
    tournament_dict.update({"place": display("Lieu: ")})
    tournament_dict.update({"starting_date": display("Date de début: ", "date")})
    tournament_dict.update({"ending_date": display("Date de fin: ", "date", "", tournament_dict["starting_date"])})
    tournament_dict.update({"kind": type_str()})
    print(f'Type : {tournament_dict["kind"]}')
    if display("modifier le nombre de ronde (defaut 4) (o/n)\n", "choice", cases=["o", "n"]) == "o":
        tournament_dict.update({"number_of_round": display("Nombre de ronde: ", "natural")})
    else:
        pass
    tournament_dict.update({"description": display("Description: ")})
    return tournament_dict


def display_make_a_player():
    """
    Display the player making menu
    don't use attribute
    :return: a dictionary
    """
    display_head_menu("Création du joueur")
    player_dict = {}
    player_dict.update({"lastname": display("Nom: ")})
    player_dict.update({"firstname": display("Prénom: ")})
    player_dict.update({"gender": display("Genre : (homme/femme)", "gender")})
    player_dict.update({"date_of_birth": display("Date de naissance: ", "date")})
    player_dict.update({"ranking": display("Classement : ", "natural")})
    return player_dict


if __name__ == "__main__":
    print("can't be run")
