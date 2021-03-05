#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime


def control_int():
    itsok = False
    os.system("stty -echo")
    while not itsok:
        user = input()
        try:
            int(user)
            itsok = True
            return int(user)
        except ValueError:
            pass


def control_input(cases):
    choice_ok = False
    user_choice = input()
    if user_choice in cases:
        choice_ok = True
        return choice_ok, user_choice
    return choice_ok


def control_choice(string, cases):
    print(string)
    os.system("stty -echo")
    user = input()
    while user not in cases:
        user = input()
    os.system("stty echo")
    return user


def type_str():
    types = display("Choisir un Type: Bullet (1) , Blitz (2) , Coup Rapide (3)", "choice", ["1", "2", "3"])
    if types == "1":
        return "Bullet"
    elif types == "2":
        return "Blitz"
    else:
        return "Coup Rapide"


def control_date(string1, string2=""):
    itsok = False
    print(string1, end="")
    os.system("stty -echo")
    user = ""
    while not itsok:
        user = input()
        itsok = control_a_date(user)
        if not string2 =="" and itsok:
            itsok = control_a_date_after(string2, user)
    os.system("stty echo")
    print(user)
    return user


def control_a_date(string):
    list = string.split("/")
    try:
        year = int(list[2])
        month = int(list[1])
        day = int(list[0])
        datetime.date(year, month, day)
        return True
    except ValueError:
        return False
    except IndexError:
        return False


def control_a_date_after(date1,date2):
    date1list = date1.split("/")
    year1 = int(date1list[2])
    month1 = int(date1list[1])
    day1 = int(date1list[0])
    d1 = datetime.date(year1, month1, day1)
    date2list = date2.split("/")
    year2 = int(date2list[2])
    month2 = int(date2list[1])
    day2 = int(date2list[0])
    d2 = datetime.date(year2, month2, day2)
    if d1 <= d2:
        return True
    else :
        return False


def control_natural():
    natural = -1
    while natural < 0:
        natural = control_int()
    return natural


def control_gender():
    gender = ""
    os.system("stty -echo")
    while not (gender =="homme" or gender == "femme"):
        gender = input().lower()
    return gender


def display(string, type_to_check="str", cases=(), string2=""):
    """fonction input qui se contrôle automatiquement"""
    if type_to_check == "int":
        print(string, end="")
        integer = control_int()
        os.system("stty echo")
        print(integer)
        return integer
    elif type_to_check == "natural":
        print(string, end="")
        natural = control_natural()
        os.system("stty echo")
        print(natural)
        return natural
    elif type_to_check == "date":
        return control_date(string, string2)
    elif type_to_check == "choice":
        return control_choice(string, cases)
    elif type_to_check == "str":
        return input(string)
    elif type_to_check == "gender":
        print(string, end="")
        gender = control_gender()
        os.system("stty echo")
        print(gender)
        return gender


if __name__ == "__main__":
    print("can't be run")