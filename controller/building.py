#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.player import Player
from model.round import Round
from model.loading import get_identity, scooting_player_id, loading_player
from controller.setting import current_tournament, players
from model.saving import saving_player


def make_a_tournament(tournament_dict, new=True):
    """
    :param tournament_dict: dictionary with your tournament caract
    :param new: True if it's a new tournament, else false
    :return: tournament instance
    """
    current_tournament.edit_name(tournament_dict['name'])
    current_tournament.edit_place(tournament_dict['place'])
    current_tournament.edit_starting_date(tournament_dict['starting_date'])
    current_tournament.edit_ending_date(tournament_dict['ending_date'])
    current_tournament.edit_kind(tournament_dict['kind'])
    try:
        current_tournament.edit_number_of_round(tournament_dict['number_of_round'])
    except KeyError:
        pass
    current_tournament.edit_description(tournament_dict['description'])
    if new:
        current_tournament.edit_id(get_identity("tournament"))
    else:
        current_tournament.edit_id(tournament_dict["identity"])
        for player_id in tournament_dict["players_id"]:
            current_tournament.edit_players_id_by_one(player_id)
        for player_id in tournament_dict["players_id"]:
            make_a_player(loading_player(player_id), False, current_tournament.identity)
        for ronde in tournament_dict["serialized_round"]:
            current_tournament.add_a_round(make_a_round(ronde, current_tournament.identity))


def make_a_round(ronde_dict, tournament_id):
    """
    :param ronde_dict: dictionary, with your round caract
    :param tournament_id: interger, identity of your tournament
    :return: round instance
    """

    rond = Round(tournament_id=tournament_id, name=ronde_dict["name"],
                 starting_date=ronde_dict["starting_date"], ending_date=ronde_dict["ending_date"])
    rond.edit_matches(ronde_dict["matches"])
    return rond


def make_a_player(player_dict, new=True, tournament_id=0):
    """
    :param player_dict: ictionary, with your player caract
    :param new: true if it's a new player, else False
    :param tournament_id: interger, identity of your tournament
    :return: player instance
    """
    if len(players) < 8:
        current_player = Player()
        current_player.edit_lastname(player_dict["lastname"])
        current_player.edit_firstname(player_dict["firstname"])
        current_player.edit_date_of_birth(player_dict["date_of_birth"])
        current_player.edit_gender(player_dict["gender"])
        current_player.edit_ranking(player_dict["ranking"])
        if new:
            current_player.edit_identity(get_identity("players"))
            saving_player(current_player)
        else:
            try:
                t_id = str(tournament_id)
                current_player.add_tournament_point(tournament_id, player_dict["tournament_point"][t_id])
            except KeyError:
                pass
            except TypeError:
                pass
            current_player.edit_identity(scooting_player_id(current_player))
        players.append(current_player)
        return True
    else:
        return False


if __name__ == "__main__":
    print("can't be run")
