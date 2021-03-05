#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.tournament import Tournament
from model.round import Round
from model.player import Player

def sort(players, tid):
    sorted_player = sorted(players, key=lambda player: player.ranking, reverse=True)
    sorted_player = sorted(sorted_player, key=lambda player: player.tournament_point[tid], reverse=True)
    return sorted_player

def make_a_round(players,current_tournament):
    sorted_players = sort(players, current_tournament.identity)
    players_id = []
    for player in sorted_players:
        players_id.append(player.identity)
    return Round(players_id, current_tournament.identity)


def first_round(players, current_tournament):
    current_round = make_a_round(players, current_tournament)
    current_round.first_matchmaking()
    current_tournament.add_a_round(current_round)
    return current_tournament


def other_round(players, current_tournament):
    list_of_match = []
    current_round = make_a_round(players, current_tournament)
    safety_list = current_round.players_id
    for rounded in current_tournament.rounds:
        for match in rounded.matches:
            list_of_match.append(match)
    while len(current_round.matches) < 4:
        i = 1
        while (safety_list[0], safety_list[i]) in list_of_match:
            i += 1
            if i == len(safety_list):
                i = 1
                break
        match = (safety_list.pop(0), safety_list.pop(i-1))
        current_round.matches.append(match)
    current_tournament.add_a_round(current_round)
    return current_tournament

def test_point(players,tournament):
    for match in tournament.rounds[-1].matches:
        whowin = input(f"{players[match[0]].firstname} vs {players[match[1]].firstname}")
        if whowin == "v":
            players[match[0]].add_tournament_point(tournament.identity, 1)
        elif whowin == "n":
            players[match[0]].add_tournament_point(tournament.identity, 0.5)
            players[match[1]].add_tournament_point(tournament.identity, 0.5)
        else:
            players[match[1]].add_tournament_point(tournament.identity, 1)