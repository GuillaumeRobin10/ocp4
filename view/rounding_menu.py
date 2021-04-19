#!/usr/bin/env python
# -*- coding: utf-8 -*-
from controller.rounding import pairing, scoring
from controller.setting import current_tournament, result_list, players
from controller.Display import display
from controller.getDate import what_date_is_it
from model.saving import saving_tournament, saving_players

from view.tools import choice_menu, display_head_menu
from view.setting import IN_ROUND_MENU, END_ROUND_MENU
from view.rapport_menu import rapport_menu, a_sort_by_ranking_in_tournament
from view.players_menu import player_menu_2


def display_rounding():
    """
    Display the round interface
    :return: none
    """
    display_head_menu(current_tournament.rounds[-1].name)
    i = 0
    joueur1 = ""
    joueur2 = ""
    for match in current_tournament.rounds[-1].matches:
        for player in players:
            if match[0][0] == player.identity:
                joueur1 = f"{player.lastname} {player.firstname}"
            if match[1][0] == player.identity:
                joueur2 = f"{player.lastname} {player.firstname}"
        print(f"{joueur1} vs {joueur2}")
    print("\nrésultat : (Entrez la lettre qui correspond V , N , D ) \n")
    for match in current_tournament.rounds[-1].matches:
        for player in players:
            if match[0][0] == player.identity:
                joueur1 = f"{player.lastname} {player.firstname}"
        result_list.append(display(f"{joueur1} :", "choice", ["v", "d", "n"]))
        print(result_list[i])
        i += 1
    current_tournament.rounds[-1].edit_ending_date(what_date_is_it())


def in_round_menu():
    """
    Main menu.
    Menu with the different choce you have.
    :return: none
    """
    if len(current_tournament.rounds) < current_tournament.number_of_round:
        u_choice = choice_menu(IN_ROUND_MENU["string"], IN_ROUND_MENU["cases"], IN_ROUND_MENU["Header"])
        if u_choice == "1":
            pairing()
            display_rounding()
            scoring()
            saving_tournament(current_tournament)
            saving_players()
            in_round_menu()
        elif u_choice == "2":
            if player_menu_2() == 1:
                in_round_menu()
        elif u_choice == "3":
            if rapport_menu() == 1:
                in_round_menu()
        elif u_choice == "9":
            quit()
    else:
        u_choice = choice_menu(END_ROUND_MENU["string"], END_ROUND_MENU["cases"], END_ROUND_MENU["Header"])
        if u_choice == "1":
            if a_sort_by_ranking_in_tournament() == 1:
                in_round_menu()
        elif u_choice == "2":
            if player_menu_2() == 1:
                in_round_menu()
        elif u_choice == "3":
            rapport_menu()
            in_round_menu()
        elif u_choice == "9":
            quit()


if __name__ == "__main__":
    print("can't be run")
