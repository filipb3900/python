def binary_to_decimal(b):
    bin = int(b, 2)
    return bin

'''def binary_to_decimal(binstr):
    if not binstr:
        return 0
    return binary_to_decimal(binstr[:-1]) * 2 + int(binstr[-1]) #http://stackoverflow.com/questions/40567667'''

def decimal_to_binary(newint2):
    newint2 = int(newint2)
    binstr = ""
    while newint2 > 0:
        binstr = str(newint2 % 2) + binstr
        newint2 = newint2 // 2
    return binstr

def ticket(text):
    print ("/" + "-" *48 + "\\")
    number_of_spaces = (48-len(text))/2
    print("|" + " "*int(number_of_spaces) + text + " "*int(number_of_spaces) + "|")
    print("\\" + "-"*48 + "/")


calc_is_on = True
while calc_is_on:
    try:
        number, dec_or_bin = input("First enter number and after the space enter system: ").split()
        while not( dec_or_bin == "2" or dec_or_bin == "10"): #check if user input right number of system
            dec_or_bin = input("Do you want calc bin or dec? (2/10): ").upper()
        while not(number.isdigit()): #check if imput is number
            number = input("Enter the right number: ")


        if dec_or_bin == "2": #calculate binary to decimal
            try:
                if ("1" in number and "0" in number) or ("0" in number) or ("1" in number):
                    liczba = str(binary_to_decimal(number))
                    print(ticket(liczba + " | 10 " ))
                else:
                    print("Binary number consist of 1 and 0!!!\n")
                    continue
            except:
                print("Binary number consist of 1 and 0!!!\n")
                continue


            ###ask to new calculation or exit
            ask = input("Another calc? (n to exit or press any key to continue)\n ").upper() ###ask to new calculation or exit
            if ask == "N":
                calc_is_on = False
            else:
                calc_is_on = True


        else: #calulate decimal to binary
            print(ticket(decimal_to_binary(number) + " | 2"))
            ask = input("Another calc? (n to exit or press any key to continue)\n ").upper()
            if ask == "N":
                calc_is_on = False
            else:
                calc_is_on = True

    except:
        print("Wrong! You must enter number and after the space enter system ")
        ask = input("Do you want try again? (n to exit or press any key to continue)\n ").upper()
        if ask == "N":
            calc_is_on = False
        else:
            calc_is_on = True
