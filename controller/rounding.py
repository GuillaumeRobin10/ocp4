#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model.round import Round

from controller.setting import current_tournament, players, result_list
from controller.matchmaking import other_matchmaking
from controller.getDate import what_date_is_it


def pairing():
    if not current_tournament.rounds:
        round_building(True)
    else:
        round_building(False)


def sort_players():
    sorted_player = sorted(players,
                           key=lambda player: player.ranking,
                           reverse=True)
    try:
        sorted_player.sort(key=lambda player: player.tournament_point[current_tournament.identity], reverse=True)

    except KeyError:
        pass
    return sorted_player


def sort_name():
    sorted_player = sorted(players,
                           key=lambda player: player.firstname,
                           reverse=True)
    sorted_player = sorted(sorted_player,
                           key=lambda player: player.lastname,
                           reverse=True)
    return sorted_player


def get_players_id(sorted_player_list):
    sorted_id_list = []
    for player in sorted_player_list:
        sorted_id_list.append(player.identity)
    return sorted_id_list


def round_building(first):
    sorted_players = get_players_id(sort_players())
    current_round = Round(current_tournament.identity)
    current_round.edit_sorted_players(sorted_players)
    current_round.edit_starting_date(what_date_is_it())
    if first:
        current_round.first_matchmaking()
    else:
        current_round.edit_matches(other_matchmaking(sorted_players))
    current_tournament.add_a_round(current_round)
    nb = len(current_tournament.rounds)
    current_tournament.rounds[-1].edit_name(f"round {nb}")


def scoring():
    incrementation = 0
    for result in result_list:
        if result == "v":
            for player in players:
                if player.identity == current_tournament.rounds[-1].matches[incrementation][0][0]:
                    player.add_tournament_point(current_tournament.identity, 1)
                    current_tournament.rounds[-1].matches[incrementation][0][1] = 1
                elif player.identity == current_tournament.rounds[-1].matches[incrementation][1][0]:
                    player.add_tournament_point(current_tournament.identity, 0)
                    current_tournament.rounds[-1].matches[incrementation][1][1] = 0

        elif result == "n":
            for player in players:
                if player.identity == current_tournament.rounds[-1].matches[incrementation][0][0]:
                    player.add_tournament_point(current_tournament.identity, 0.5)
                    current_tournament.rounds[-1].matches[incrementation][0][1] = 0.5

                elif player.identity == current_tournament.rounds[-1].matches[incrementation][1][0]:
                    player.add_tournament_point(current_tournament.identity, 0.5)
                    current_tournament.rounds[-1].matches[incrementation][1][1] = 0.5

        elif result == "d":
            for player in players:
                if player.identity == current_tournament.rounds[-1].matches[incrementation][0][0]:
                    player.add_tournament_point(current_tournament.identity, 0)
                    current_tournament.rounds[-1].matches[incrementation][0][1] = 0
                elif player.identity == current_tournament.rounds[-1].matches[incrementation][1][0]:
                    player.add_tournament_point(current_tournament.identity, 1)
                    current_tournament.rounds[-1].matches[incrementation][1][1] = 1
        incrementation += 1
    result_list.clear()


if __name__ == "__main__":
    print("can't be run ")
