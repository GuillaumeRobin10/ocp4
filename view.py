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
    for i in range(len(name_menu)):
        hyphens += "-"
    return hyphens

def display_head_menu(name):
    print(make_a_hyphens(name))
    print(name)
    print(make_a_hyphens(name))

def control_and_display_a_choice(text_to_display,case,header=""):
    """control the user input and display the choice 'til he don't make a good choice"""
    user_input = ""
    while not user_input in case:
        if not header == "":
            display_head_menu(header)
        print(text_to_display)
        user_input = input()
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
    print("Nom :")
    user_choise = input()
    tournament["Nom"] = user_choise
    os.system('cls||clear')
    display_head_menu(MAKE_TOURNAMENT)
    print(f"Nom : {tournament['Nom']}")
    print("Lieu :")
    user_choise = input()
    tournament["Lieu"] = user_choise
    os.system('cls||clear')
    display_head_menu(MAKE_TOURNAMENT)
    print(f"Nom : {tournament['Nom']}")
    print(f"Lieu : {tournament['Lieu']}")
    #mettre la date
    user_choise = ""
    while not ( user_choise in ["1","2"]):
        os.system('cls||clear')
        display_head_menu(MAKE_TOURNAMENT)
        print(f"Nom : {tournament['Nom']}")
        print(f"Lieu : {tournament['Lieu']}")
        user_choise = input("Tounois sur plusieurs jours ? oui(1) non(2)")

    if user_choise == "1":
        os.system('cls||clear')
        display_head_menu(MAKE_TOURNAMENT)
        print(f"Nom : {tournament['Nom']}")
        print(f"Lieu : {tournament['Lieu']}")
        print("Tounois sur plusieurs jours")
        # mettre la date
        user_choise = input("Date du début")
        tournament["Debut"] = user_choise
        user_choise = input("Date de fin")
        tournament["Fin"] = user_choise
    else :
        user_choise = ""
        os.system('cls||clear')
        display_head_menu(MAKE_TOURNAMENT)
        print(f"Nom : {tournament['Nom']}")
        print(f"Lieu : {tournament['Lieu']}")
        user_choise = input("quelle est la date du tournois ?")
        tournament["Debut"]= user_choise
        tournament["Fin"] = user_choise
    print("Type : Bullet (1) , Blitz (2) , Coup Rapide (3)")#controler le type
    user_choise = ""
    while not ( user_choise in ["1","2","3"]):
        user_choise = input()
    if user_choise == "1":
        tournament["Type"] = "Bullet"
    elif user_choise == "2":
        tournament["Type"] = "Blitz"
    elif user_choise == "3":
        tournament["Type"] = "Coup Rapide"
    os.system('cls||clear')
    display_head_menu(MAKE_TOURNAMENT)
    print(f"Nom : {tournament['Nom']}")
    print(f"Lieu : {tournament['Lieu']}")
    print(f"Début : {tournament['Debut']}")
    print(f"Fin : {tournament['Fin']}")
    print(f"Type : {tournament['Type']}")
    print("Nombre de round : (passer pour un nombre de round par défault a 4)") #défault=4
    user_choise = input()
    try:
        nb_round =int(user_choise)
        tournament["Round"] = nb_round
    except:
        tournament["Round"] = 4
    os.system('cls||clear')
    display_head_menu(MAKE_TOURNAMENT)
    print(f"Nom : {tournament['Nom']}")
    print(f"Lieu : {tournament['Lieu']}")
    print(f"Début : {tournament['Debut']}")
    print(f"Fin : {tournament['Fin']}")
    print(f"Type : {tournament['Type']}")
    print(f"Nombre de round : {tournament['Round']}")
    print("Description :")
    user_choise = input()
    tournament["Description"] = user_choise
    while not user_choise =="1":
        os.system('cls||clear')
        display_head_menu(MAKE_TOURNAMENT)
        print(f"Nom : {tournament['Nom']}")
        print(f"Lieu : {tournament['Lieu']}")
        print(f"Début : {tournament['Debut']}")
        print(f"Fin : {tournament['Fin']}")
        print(f"Type : {tournament['Type']}")
        print(f"Nombre de round : {tournament['Round']}")
        print(f"Description : {tournament['Description']}")
        user_choise = input ("Continuer (1)\n")
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
