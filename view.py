#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from controller import *

# init
#Const
MENU = "|       Menu       |"
MAKE_TOURNAMENT = "| Creation d'un tournoi |"
MAKE_PLAYER = "| Creation d'un joueur |"
DISPLAY_ROUND = "| Ronde |"

#end Const
#global variable

# end init


def make_a_hyphens(name_menu):
    """Give it a sting and return a string of hyphens egal of the giving string."""
    hyphens = ""
    for _ in range(len(name_menu)):
        hyphens += "-"
    return hyphens

def display_head_menu(name):
    print(make_a_hyphens(name))
    print(name)
    print(make_a_hyphens(name))

def control_and_display_a_choice(text_to_display,case,header=""):
    """control the user input and display the choice 'til he don't make a good choice"""
    user_input = ""
    os.system('cls||clear')
    while not user_input in case:
        if not header == "":
            display_head_menu(header)
        user_input = input(text_to_display)
        os.system('cls||clear')
    return user_input

def early_menu():
    """first menu"""
    menu_string ="\n Nouveau tournoi '1' \n Charger un tournoi '2' \n"
    cases=["1","2"]
    control_and_display_a_choice(menu_string,cases,MENU)


def display_main_menu():
    """Display the main menu"""
    menu_string = " Prochaine round (1) \n Joueur (2) \n Matchs (3) \n Round (4) \n sauvegarder (5) \n"
    cases =["1","2","3","4","5"]
    control_and_display_a_choice(menu_string,cases,MENU)


def display_and_control_make_a_tournament():
    tournament ={}
    display_head_menu(MAKE_TOURNAMENT)
    user_choice = input(" Nom :")
    tournament["Nom"] = user_choice
    user_choice = input(" Lieu :")
    tournament["Lieu"] = user_choice
    #mettre la date
    date_statement = f" Nom : {tournament['Nom']} \n Lieu : {tournament['Lieu']} \n"
    date_choice = date_statement + " Tounois sur plusieurs jours ? oui(1) non(2)"
    cases=["1","2"]
    user_choice=control_and_display_a_choice(date_choice,cases,MAKE_TOURNAMENT)
    if user_choice == "1":
        date_ok=False
        while not date_ok == True:
            os.system('cls||clear')
            display_head_menu(MAKE_TOURNAMENT)
            print(date_statement+" Tounois sur plusieurs jours")
            user_choice = input(" Date du début du tournois : ( format JJ/MM/AAAA ) ")
            date_ok = control_a_date(user_choice)
        tournament["Debut"] = user_choice
        date_ok = False
        after = False
        while not (date_ok == True and after== True):
            os.system('cls||clear')
            display_head_menu(MAKE_TOURNAMENT)
            print(date_statement+f" Tounois sur plusieurs jours \n Début du tournois : {tournament['Debut']} ")
            user_choice = input(" Date de fin du tournois : ( format JJ/MM/AAAA ) ")
            date_ok = control_a_date(user_choice)
            if date_ok :
                after = control_a_date_after(tournament['Debut'],user_choice)
        tournament["Fin"] = user_choice
    else :
        date_ok = False
        while not date_ok :
            os.system('cls||clear')
            display_head_menu(MAKE_TOURNAMENT)
            print(date_statement + " Tounois sur une journée")
            user_choice = input(" Date du tournois : ( format JJ/MM/AAAA ) ")
            date_ok = control_a_date(user_choice)
        tournament["Debut"] = user_choice
        tournament["Fin"] = user_choice
    type_statement = f" Nom : {tournament['Nom']} \n Lieu : {tournament['Lieu']} \n Début :{tournament['Debut']} \n Fin :{tournament['Fin']} \n"
    type_statement += " Type : Bullet (1) , Blitz (2) , Coup Rapide (3)"
    cases=["1","2","3"]
    user_choice = control_and_display_a_choice(type_statement, cases, MAKE_TOURNAMENT)
    if user_choice == "1":
        tournament["Type"] = "Bullet"
    elif user_choice == "2":
        tournament["Type"] = "Blitz"
    elif user_choice == "3":
        tournament["Type"] = "Coup Rapide"
    os.system('cls||clear')
    display_head_menu(MAKE_TOURNAMENT)
    print(f" Nom : {tournament['Nom']}")
    print(f" Lieu : {tournament['Lieu']}")
    print(f" Début : {tournament['Debut']}")
    print(f" Fin : {tournament['Fin']}")
    print(f" Type : {tournament['Type']}")
    user_choice = input(" Nombre de ronde : ( entre 1 et 8, par défault il y a 4 ronde)")
    try:
        nb_round =int(user_choice)
        if 0 < nb_round < 8:
            tournament["Round"] = nb_round
        else:
            tournament["Round"] = 4
    except ValueError:
        tournament["Round"] = 4
    os.system('cls||clear')
    display_head_menu(MAKE_TOURNAMENT)
    end_display = f" Nom : {tournament['Nom']} \n Lieu : {tournament['Lieu']} \n Début : {tournament['Debut']} \n Fin : {tournament['Fin']} \n Type : {tournament['Type']} \n Nombre de round : {tournament['Round']}"
    user_choice = input(f"{end_display} \n Description :")
    tournament["Description"] = user_choice
    end_display += f"\n Description : {tournament['Description']} \n continuer (1)"
    control_and_display_a_choice(end_display,["1"],MAKE_TOURNAMENT)

    return make_a_tournament(tournament)


def display_and_control_make_a_player():
    player={}
    display_head_menu(MAKE_PLAYER)
    user_choise = input(f" Nom : ")
    player["Nom"]= user_choise
    user_choise = input(f" Prénom : ")
    player["Prenom"]= user_choise
    user_choise = input(f" Date de naissance : ")
    player["Birthday"]= user_choise
    user_choise = input(f" Sexe : ")
    player["Sexe"]= user_choise
    user_choise = input(f" Classement : ")
    player["Classement"]= user_choise
    return make_a_player(player)

def main():
    user=control_and_display_menu_choise()
    if user=="1":
        tournois = display_and_control_make_a_tournament()
        tournois.display()
        player=display_and_control_make_a_player()
        player.display()
        save_a_tournament(tournois)
    else:
        load_a_tournament()

    control_and_display_main_choise()

if __name__ == "__main__":
    display_and_control_make_a_tournament()
