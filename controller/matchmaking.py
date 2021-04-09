#!/usr/bin/env python
# -*- coding: utf-8 -*-
from controller.setting import current_tournament


def other_matchmaking(players_sorted_list):
    matches = []
    match_done = []
    for rounded in current_tournament.rounds:
        for match in rounded.matches:
            match_done.append(match)
    while len(players_sorted_list) > 0:
        make = False
        i = 1
        while (not i == (len(players_sorted_list) - 1)) and not make:
            try_match_1 = (players_sorted_list[0], players_sorted_list[i])
            try_match_2 = (players_sorted_list[i], players_sorted_list[0])
            if (try_match_1 not in match_done) and (try_match_2 not in match_done):
                print(try_match_1)
                matches.append((players_sorted_list.pop(i), players_sorted_list.pop(0)))
                make = True
            i += 1
        matches.append((players_sorted_list.pop(0), players_sorted_list.pop(0)))
    return matches
