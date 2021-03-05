#!/usr/bin/env python
# -*- coding: utf-8 -*-

from model.tournament import Tournament
from model.player import Player
from model.round import Round

def test_tournois():
    current_tournament = Tournament(identity=1, name="challenger",place="moscou",starting_date="10/10/2020",ending_date="10/10/2020",kind='bullet', description="test")
    return current_tournament


def test_player(i, tid):
    player = Player(lastname=f"lastname{i}", firstname=f"firstname{i}", date_of_birth="10/10/10", gender="homme", ranking=i, identity=i, tournament_point= 0, tournament_id=tid)
    return player


def sort(players, tid):
    sorted_player = sorted(players, key=lambda player: player.ranking, reverse=True)
    sorted_player = sorted(sorted_player, key=lambda player: player.tournament_point[tid], reverse=True)
    return sorted_player

def testing():
    players = []
    current_round_nb = 0
    tournament = test_tournois()
    for i in range(8):
        players.append(test_player(i, tournament.identity))
    sorted_player = sort(players, tournament.identity)
    for player in sorted_player:
        tournament.edit_players_id(player.identity)



    while current_round_nb < tournament.number_of_round:
        sorted_player = sort(players, tournament.identity)
        for player in sorted_player:
            tournament.edit_players_id_sorted(player.identity)
        safety_list = tournament.players_id_sorted
        current_round = Round(safety_list, tournament.identity)
        current_round.first_matchmaking()
        for match in current_round.matches:
            whowin = input(f"{players[match[0]].firstname} vs {players[match[1]].firstname}")
            if whowin == "v":
                players[match[0]].add_tournament_point(tournament.identity, 1)
            elif whowin == "n":
                players[match[0]].add_tournament_point(tournament.identity, 0.5)
                players[match[1]].add_tournament_point(tournament.identity, 0.5)
            else:
                players[match[1]].add_tournament_point(tournament.identity, 1)

        tournament.add_a_round(current_round)
        current_round_nb += 1

    for player in players:
        print(f'{player.firstname} : {player.tournament_point}')
