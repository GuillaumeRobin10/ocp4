#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import datetime


def control_int():
    its_ok = False
    os.system("stty -echo")
    while not its_ok:
        user = input()
        try:
            int(user)
            its_ok = True
            return int(user)
        except ValueError:
            pass


def control_choice(cases):
    os.system("stty -echo")
    user = input()
    while user not in cases:
        user = input()
    return user


def control_date(date1=""):
    os.system("stty -echo")
    is_ok = False
    user_choice = ""
    while not is_ok:
        user_choice = input()
        is_ok = control_a_date(user_choice)
        if not date1 == "" and is_ok:
            is_ok = control_a_date_after(date1, user_choice)
    return user_choice


def control_a_date(string):
    """return true if the string is a date and false if not"""
    date_list = string.split("/")
    try:
        year = int(date_list[2])
        month = int(date_list[1])
        day = int(date_list[0])
        datetime.date(year, month, day)
        return True
    except ValueError:
        return False
    except IndexError:
        return False


def control_a_date_after(date1, date2):
    """ return true if date2 > date 1, false if not"""
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
    else:
        return False


def control_natural():
    natural = -1
    while natural < 0:
        natural = control_int()
    return natural


def control_gender():
    gender = ""
    os.system("stty -echo")
    while not (gender == "homme" or gender == "femme"):
        gender = input().lower()
    return gender


def display(string, type_to_check="str", cases=(), date1=""):
    """control if an input is what is suppose to """
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
        print(string, end="")
        date = control_date(date1)
        os.system("stty echo")
        print(date)
        return date
    elif type_to_check == "choice":
        print(string, end="")
        user_choice = control_choice(cases)
        os.system("stty echo")
        return user_choice
    elif type_to_check == "str":
        return input(string)
    elif type_to_check == "gender":
        print(string, end="")
        gender = control_gender()
        os.system("stty echo")
        print(gender)
        return gender


def type_str():
    """convert a string number to a string"""
    types = display("Choisir un Type: Bullet (1) , Blitz (2) , Coup Rapide (3)", "choice", ["1", "2", "3"])
    if types == "1":
        return "Bullet"
    elif types == "2":
        return "Blitz"
    else:
        return "Coup Rapide"


if __name__ == "__main__":
    print("can't be run")
