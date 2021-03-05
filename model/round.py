#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Round:
    def __init__(self, players_id, tournament_id):
        self.matches = []
        self.players_id = players_id
        self.tournament_id = tournament_id

    def other_matchmaking(self):
        pass

    def first_matchmaking(self):
        safety_list = self.players_id
        first_list = []
        second_list = []
        for i in range(4):
            first_list.append(safety_list.pop(0))
        for i in range(4):
            second_list.append(safety_list.pop(0))
        for i in range(4):
            match = (first_list.pop(0), second_list.pop(0))
            self.matches.append(match)



if __name__ == "__main__":
    print("can't be run")