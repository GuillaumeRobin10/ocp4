#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model.round import Round

from controller.setting import current_tournament, players, result_list
from controller.matchmaking import other_matchmaking


def pairing():
    if not current_tournament.rounds:
        round_building(True)
    else:
        round_building(False)


def sort_players():
    sorted_player = sorted(players,
                           key=lambda player: player.ranking,
                           reverse=True)
    sorted_player = sorted(sorted_player,
                           key=lambda player: player.tournament_point[current_tournament.identity],
                           reverse=True)
    return sorted_player


def get_players_id(sorted_player_list):
    sorted_id_list = []
    for player in sorted_player_list:
        sorted_id_list.append(player.identity)
    return sorted_id_list


def round_building(first):
    sorted_players = get_players_id(sort_players())
    current_round = Round(sorted_players, current_tournament.identity)
    if first:
        current_round.first_matchmaking()
    else:
        current_round.edit_matches(other_matchmaking(sorted_players))
    current_tournament.add_a_round(current_round)


def scoring():
    i = 0
    for result in result_list:
        if result == "v":
            for player in players:
                if player.identity == current_tournament.rounds[-1].matches[i][0]:
                    player.add_tournament_point(current_tournament.identity, 1)
        elif result == "n":
            for player in players:
                if player.identity == current_tournament.rounds[-1].matches[i][0]:
                    player.add_tournament_point(current_tournament.identity, 0.5)
                elif player.identity == current_tournament.rounds[-1].matches[i][1]:
                    player.add_tournament_point(current_tournament.identity, 0.5)
        elif result == "d":
            for player in players:
                if player.identity == current_tournament.rounds[-1].matches[i][1]:
                    player.add_tournament_point(current_tournament.identity, 1)
        i += 1
    result_list.clear()


if __name__ == "__main__":
    print("can't be run ")
