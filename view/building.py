#!/usr/bin/env python
# -*- coding: utf-8 -*-
from controller.display_function import display, type_str
from menu import display_head_menu


def display_make_a_tournament():
    display_head_menu("tournament Building")
    tournament_dict = {"name" : display("Nom: ")}
    tournament_dict.update({"place": display("Lieu: ")})
    tournament_dict.update({"starting_date": display("Date de début: ", "date")})
    tournament_dict.update({"ending_date": display("Date de fin: ", "date", "", tournament_dict["starting_date"])})
    tournament_dict.update({"type": type_str()})
    print(f'type : {tournament_dict["type"]}')
    tournament_dict.update({"number_of_round": display("Nombre de ronde: ", "int")})
    tournament_dict.update({"Description": display("Description: ")})
    return tournament_dict


def display_make_a_player():
    player = {"lastname": display("Nom : ")}
    player.update({"firstname": display("Prénom : ")})
    player.update({"date_of_birth": display("Date de naissance : ", "date")})
    player.update({"gender": display("Genre : ", "gender")})
    player.update({"ranking": display("Classement : ", "natural")})
    return player


if __name__ == "__main__":
    print("can't be run")
