#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Round:
    def __init__(self, sorted_players_id, tournament_id):
        self.matches = []
        self.sorted_players_id = sorted_players_id
        self.tournament_id = tournament_id

    def edit_matches(self, matches):
            self.matches = matches



    def first_matchmaking(self):
        top_list = []
        low_list = []
        print(self.sorted_players_id)
        for _ in range(4):
            top_list.append(self.sorted_players_id.pop(0))
            print(top_list)
        for _ in range(4):
            low_list.append(self.sorted_players_id.pop(0))
        for _ in range(4):
            self.matches.append((top_list.pop(0), low_list.pop(0)))


if __name__ == "__main__":
    print("can't be run")