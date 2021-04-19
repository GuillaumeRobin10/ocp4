#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.loading import get_db
from controller.rapport import sort_players_alpha, sort_players_ranking
from controller.rounding import sort_name, sort_players
from controller.setting import current_tournament, players

from view.tools import choice_menu, display_head_menu
from view.setting import RAPPORT_MENU_STRING, RAPPORT_ACTOR, RAPPORT_ACTOR_IN


def a_sort_by__alpha():
    """
    display all player sorted by alpha
    :return:
    """
    i = 1
    for player in sort_players_alpha(get_db("players")):
        print(f"{i}. {player[0]} {player[1]}")
        i += 1


def a_sort_by_ranking():
    """
    display all player sorted by ranking point
    :return: none
    """
    i = 1
    try:
        for player in sort_players_ranking(get_db("players")):
            print(f"{i}. {player[0]} {player[1]} {player[2]} points")
            i += 1
    except KeyError:
        pass


def a_sort_by_alpha_in_tournament():
    """
    display player sorted by alpha
    :return: none
    """
    i = 1
    for player in sort_name():
        print(f"{i}. {player.lastname} {player.firstname}")
        i += 1


def a_sort_by_ranking_in_tournament():
    """
    display player sorted by ranking
    :return: none
    """
    i = 1
    string = ""
    for player in sort_players():
        try:
            string +=\
                f"{i}. {player.lastname}" \
                f" {player.firstname}" \
                f" {player.tournament_point[current_tournament.identity]}" \
                f" points\n"
        except KeyError:
            string +=\
                f"{i}. {player.lastname}" \
                f" {player.firstname}" \
                f" \n"

        i += 1
    string += "\n tapez sur (1) pour continuez"
    choice_menu(string, ["1"], "Classement")
    return 1


def rapport_menu():
    """
    display the rapport menu
    :return: none
    """
    u_choice = choice_menu(RAPPORT_MENU_STRING["string"], RAPPORT_MENU_STRING["cases"], RAPPORT_MENU_STRING["Header"])
    if u_choice == "1":
        u_choice = choice_menu(RAPPORT_ACTOR["string"], RAPPORT_ACTOR["cases"], RAPPORT_ACTOR["Header"])
        if u_choice == "1":
            display_head_menu("Ordre alphabétique")
            a_sort_by__alpha()
            input("\ntapez sur un touche pour continuez")
            return 1
        else:
            display_head_menu("Par classement")
            a_sort_by_ranking()
            input("\ntapez sur un touche pour continuez")
            return 1
    elif u_choice == "2":
        u_choice = choice_menu(RAPPORT_ACTOR_IN["string"], RAPPORT_ACTOR_IN["cases"], RAPPORT_ACTOR_IN["Header"])
        if u_choice == "1":
            display_head_menu("Ordre alphabétique")
            a_sort_by_alpha_in_tournament()
            input("\ntapez sur un touche pour continuez")
            return 1
        else:
            display_head_menu("Par classement")
            a_sort_by_ranking_in_tournament()
            input("\ntapez sur un touche pour continuez")
            return 1

    elif u_choice == "3":
        display_head_menu("liste de tous les tournois")
        i = 1
        for tournament in get_db("tournament"):
            print(f"{i}. {tournament['name']}")
            i += 1
        input("\ntapez sur un touche pour continuez")
        return 1
    elif u_choice == "4":
        display_head_menu("liste de tous les tours du tournois'")
        for c_round in current_tournament.rounds:
            print(f"{c_round.name} - debut: {c_round.starting_date} - fin: {c_round.ending_date}")
        input("\ntapez sur un touche pour continuez")
        return 1
    elif u_choice == "5":
        display_head_menu("liste de tous les matchs du tounois")
        for c_round in current_tournament.rounds:
            print(f"\n{c_round.name}")
            for match in c_round.matches:
                player1 = ""
                player2 = ""
                winner = ""
                for player in players:
                    if player.identity == match[0][0]:
                        player1 = f"{player.lastname} {player.firstname}"
                    if player.identity == match[1][0]:
                        player2 = f"{player.lastname} {player.firstname}"
                    if match[0][1] == 1:
                        winner = player1
                    if match[1][1] == 1:
                        winner = player2
                    if match[0][1] == 0.5:
                        winner = "Nulle"
                print(f"{player1} vs {player2} victoire : {winner}")
        input("\ntapez sur un touche pour continuez")
        return 1

    elif u_choice == "6":
        return 1
    elif u_choice == "9":
        quit()


if __name__ == "__main__":
    print("can't be run")
