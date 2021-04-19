#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.setting import db


def get_identity(what_we_looking_for):
    """take a table on attribute and return the 1st free id """
    list_of_identity = []
    identity = 1
    table = db.table(what_we_looking_for).all()
    for i in range(len(table)):
        list_of_identity.append(table[i]["identity"])
    while identity in list_of_identity:
        identity += 1
    return identity


def scooting_player():
    """
    find all player in database
    :return: dictionary with different cases ( list of interger, one by player identity)
    and a string ( all players separate by \n)
    """
    menu = {"cases": [], "string": ""}
    listing = db.table("players").all()
    for i in range(len(listing)):
        menu["cases"].append(str(i+1))
        menu["string"] += f"{listing[i]['lastname']} {listing[i]['firstname']} ({i + 1})\n"
    if menu["string"] == "":
        return 0
    return menu


def scooting_player_id(player_to_scoot):
    """
    find a player in database
    :param player_to_scoot: instance of player you want to find
    :return: interger (the player identity in the database)
    """
    listing = db.table("players").all()
    for i in range(len(listing)):
        if listing[i]["lastname"] == player_to_scoot.lastname and listing[i]["firstname"] == player_to_scoot.firstname:
            return listing[i]["identity"]


def scooting_tournament():
    """
    find all tournament in database
    :return: dictionary with different cases ( list of interger, one by tournament identity)
    and a string ( all tournament separate by \n)
    """
    menu = {"cases": [], "string": ""}
    listing = db.table("tournament").all()
    for i in range(len(listing)):
        menu["cases"].append(str(i+1))
        menu["string"] += f"{listing[i]['name']} {listing[i]['starting_date']} ({i + 1})\n"
    if menu["string"] == "":
        return 0
    return menu


def loading_tournament(identity):
    """
    :param identity: integer, your tournameent's identity
    :return: a dictionary with all your tournameent's information
    """
    listing = db.table("tournament").all()
    tournament_to_load = listing[int(identity)-1]
    return {"identity": tournament_to_load["identity"],
            "name": tournament_to_load["name"],
            "place": tournament_to_load["place"],
            "starting_date": tournament_to_load["starting_date"],
            "ending_date": tournament_to_load["ending_date"],
            "kind": tournament_to_load["kind"],
            "description": tournament_to_load["description"],
            "number_of_round": tournament_to_load["number_of_round"],
            "players_id": tournament_to_load["players_id"],
            "serialized_round": tournament_to_load["serialized_round"]}


def loading_player(identity):
    """
    :param identity: integer, your player's identity
    :return: a dictionary with all your player's information
    """
    listing = db.table("players").all()
    player_to_load = listing[int(identity)-1]
    return {"lastname": player_to_load["lastname"],
            "firstname": player_to_load["firstname"],
            "date_of_birth": player_to_load["date_of_birth"],
            "gender": player_to_load["gender"],
            "ranking": player_to_load["ranking"],
            "identity": player_to_load["identity"],
            "tournament_point": player_to_load["tournament_point"]}


def get_db(table):
    """
    :param table: table you want to search
    :return: all element of your table
    """
    return db.table(table).all()


if __name__ == "__main__":
    print("can't be run")
