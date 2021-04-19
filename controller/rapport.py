def sort_players_alpha(list_of_player):
    """
    sort a list of player by firstname, and the lastname
    :param list_of_player: list of all player you want sort
    :return: list of player
    """
    tuples = []
    for player in list_of_player:
        tuples.append((player["lastname"], player["firstname"]))
    sorted_list = sorted(tuples, key=lambda p: p[1], reverse=False)
    sorted_list = sorted(sorted_list, key=lambda p: p[0], reverse=False)
    return sorted_list


def sort_players_ranking(list_of_player):
    """
    sort a list of player by the ranking points
    :param list_of_player: list of all player you want sort
    :return: list of player
    """
    tuples = []
    for player in list_of_player:
        tuples.append((player["lastname"], player["firstname"], player["ranking"]))
    sorted_list = sorted(tuples, key=lambda p: p[2], reverse=True)
    return sorted_list


if __name__ == "__main__":
    print("can't be run")
