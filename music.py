import csv
import random


def menu():
    print("Welcome in the CoolMusic! Choose the action: ")
    print("1) Add new album")
    print("2) Find albums by artist")
    print("3) Find albums by year")
    print("4) Find musician by album")
    print("5) Find albums by letter(s)")
    print("6) Find albums by genre")
    print("7) Calculate the age of all albums")
    print("8) Choose random album by genre")
    print("0) Exit")


def appendnew(newthing):
    with open("music.csv", "a") as adds:
        filewriter = csv.writer(adds, delimiter="|", quotechar="|",
                                quoting=csv.QUOTE_NONE, escapechar="|")
        filewriter.writerow(newthing)


def choice2():
    try:
        with open("music.csv", "r") as f:
            reader = csv.reader(f, delimiter="|", quoting=csv.QUOTE_NONE)
            for row in reader:
                for field in row:
                    if field == username:
                        print (row[1:])

    except:
        print("Error")


def choice3():
    try:
        with open("music.csv", "r") as f:
            reader = csv.reader(f, delimiter="|", quoting=csv.QUOTE_NONE)
            for row in reader:
                for field in row:
                    if field == username:
                        print (row[0:2] + row[3:5])

    except:
        print("Empty")


def choice4():
    try:
        with open("music.csv", "r") as f:
            reader = csv.reader(f, delimiter="|", quoting=csv.QUOTE_NONE)
            for row in reader:
                for field in row:

                    if field == username:
                            print (row[0:1] + row[2:5])

    except:
        print("Error")


def choice6():
    try:
        with open("music.csv", "r") as f:
            reader = csv.reader(f, delimiter="|", quoting=csv.QUOTE_NONE)
            for row in reader:
                for field in row:

                    if field == username:
                            print (row[0:3] + row[4:5])

    except:
        print("Error")


def choice7():
    try:
        with open("music.csv", "r") as f:
            reader = csv.reader(f, delimiter="|", quoting=csv.QUOTE_NONE)
            total = 0
            for row in reader:
                total += (int(row[2]))
            print(total)

    except:
        print("Error")


menu()

choice = input("Enter the number: ")
x = ("1", "2", "3", "4", "5", "6", "7", "8", "0")
while not choice in x:
    choice = input("Enter the number: ")

if choice == "1":

    a = input("Put name: ")
    b = input("Put name of album: ")
    c = input("Put year: ")
    while not c.isdigit():
        c = input("Put year (Give year in numbers): ")
    c = int(c)
    d = input("Put genere: ")
    e = input("Put lenght of album: ")

    variable = (a, b, c, d, e)
    appendnew(variable)

elif choice == "2":

    print("Put artist name: ")
    username = input()
    choice2()


elif choice == "3":

    print("Put year: ")
    username = input()
    choice3()

elif choice == "4":

    print("Put album name: ")
    username = input()
    choice4()


elif choice == "5":  # dont work

    print("Put letter to find albums: ")
    username = input()
    try:
        with open("music.csv", "r") as f:
            reader = csv.reader(f, delimiter="|", quoting=csv.QUOTE_NONE)
            for row in reader:
                tryfind = (row[1])
                print(tryfind)
                if tryfind in username:
                    print(tryfind)

    except:
        print("Error")

elif choice == "6":

    print("Put genere: ")
    username = input()
    choice6()


elif choice == "7":

    choice7()

elif choice == "8":  # dont work

    print("Put genere: ")
    username = input()
    try:
        with open("music.csv", "r") as f:
            reader = csv.reader(f, delimiter="|", quoting=csv.QUOTE_NONE)
            for row in reader:
                for field in row:
                    random_choice = (row[0:3] + row[4:5])
                    if field == username:
                        print(random.choice(random_choice))

    except:
        print("Error")


else:
    exit()
