import csv


def getKey(item):  # http://stackoverflow.com/questions/34472390/
    return item[0]


def appendnew(newthing):
    with open("dictionary.csv", "a") as adds:
        adds.write("%s,%s,%s\n" % newthing)


def menu():
    print("Dictionary for a little programmer: ")
    print("1) Search explanation by appellation")
    print("2) Add new definition")
    print("3) Show all appellations alphabetically")
    print("0) Exit")


menu()
choice = input("Enter the number: ")
x = ("1", "2", "3", "4", "0")
while not choice in x:
    choice = input("Enter the number: ")

if choice == "1":

    print("Put appellation: ")
    username = input().lower()
    try:
        with open("dictionary.csv", "r") as f:
            reader = csv.reader(f, delimiter=",")
            for row in reader:
                for field in row:
                    if field == username:
                            print (row[1:])

    except:
        print("No file csv found")


elif choice == "2":

    a = input("Put your appellation: ").lower()
    a = '"' + a + '"'
    b = input("Put your definition: ").lower()
    b = '"' + b + '"'
    c = input("Put your source: ").lower()
    c = '"' + c + '"'

    variable = (a, b, c)
    appendnew(variable)


elif choice == "3":
    try:
        csvdata = []
        with open("dictionary.csv") as csvfile:
            readCSV = csv.reader(csvfile)
            for line in readCSV:
                csvdata.append(line)

        print()
        csvdata.sort(key=getKey)

        for i in csvdata:
            print(i[0])

    except:
        print("No file csv found")


else:
    exit()
