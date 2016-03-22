#!/usr/bin/env python3
import getpass
import re
import string

user = {}

def main():
    global user
    while True:
        username = input("Enter Username : ")
        if username:
            if username not in user.keys():
                print("Username Added")
                break
            else:
                print("User %s already exist!" % username)
                
    while True:
        password = getpass.getpass("Enter Password for %s : " % username)
        if password and CheckPass(password):
            # valid pass
            user[username] = password
            print("Valid Password")
            break

    while True:
        print("\n[0] Exit")
        print("[1] View Pass")
        print("[2] Add New Login")

        choice = int(input("Enter choice : "))

        if choice == 0:
            exit()
        elif choice == 1:
            viewpass()
        elif choice == 2:
            main()

def viewpass():
    global user
    print()

    # I like the way of printing all the saved user name and pass. However to justify the challenge, i shall follow your way.
    # for usr,pwd in user.items():
    #     print(usr+":"+pwd)
    # print()

    username = input("Enter Username : ")
    try:
        print(user[username])
    except KeyError:
        print("No Such User")

def CheckPass(Password):
    valid = True
    reasons = {
                r"\d":"At Least One Digit Required",
                r"[A-Z]":"At Least One Uppercase Letter Required",
                r"[a-z]":"At Least One Lowercase Letter Required",
                r"\W":"At Least One Special Character Required"
              }
    #print(dir(reasons))
    for pat,msg in reasons.items():
        if re.search(pat,Password) == None:
            valid = False
            print(reasons[pat])

    if len(Password) < 8:
        valid = False
        print("Password Needs to have at least 8 characters")

    return valid

#CheckPass(input("Enter pass : "))
main()