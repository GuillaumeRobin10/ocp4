def sort_players_alpha(list_of_player):
    tuples = []
    for player in list_of_player:
        tuples.append((player["lastname"], player["firstname"]))
    sorted_list = sorted(tuples, key=lambda p: p[1], reverse=True)
    sorted_list = sorted(sorted_list, key=lambda p: p[0], reverse=True)
    return sorted_list


def sort_players_ranking(list_of_player):
    tuples = []
    for player in list_of_player:
        tuples.append((player["lastname"], player["firstname"], player["ranking"]))
    sorted_list = sorted(tuples, key=lambda p: p[2], reverse=True)
    return sorted_list
