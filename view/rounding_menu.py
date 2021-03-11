#!/usr/bin/env python
# -*- coding: utf-8 -*-


from controller.rounding import first_round, other_round, scoring


from view.tools import choice_menu
from view.setting import IN_ROUND_MENU
from view.setting import players


def in_round_menu(current_tournament):
    u_choice = choice_menu(IN_ROUND_MENU["string"], IN_ROUND_MENU["cases"], IN_ROUND_MENU["Header"])
    if u_choice == "1":
        if len(current_tournament.players_id) == 8:
            if not current_tournament.rounds:
                current_tournament = first_round(players, current_tournament)


                for match in current_tournament.rounds[-1].matches:
                    print(f"{players[match[0]].firstname} vs {players[match[1]].firstname}")

                scoring(players, current_tournament)
                in_round_menu(current_tournament)

            else:
                current_tournament = other_round(players, current_tournament)
                print(current_tournament.rounds[-1].matches)
                scoring(players, current_tournament)
                in_round_menu(current_tournament)

        else:
            p_menu()
    elif u_choice == "2":
        p_menu()
    elif u_choice == "3":
        r_menu()
    elif u_choice == "9":
        pass
    else:
        pass
