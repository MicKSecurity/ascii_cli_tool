# Thank you for using this tool :D
# Make sure to check out my Github profile for more useful projects <3

import os

#ASCII code to character


def ascii_to_char():
    print("(Type 'menu' to go back or 'exit' to stop the script)")
    while True:

        ascii_val = input("input an ASCII code:")

        if ascii_val.lower() == "menu":
           os.system("cls" if os.name == "nt" else "clear")
           break
        
        if ascii_val.lower() == "exit":
            exit()
        try:
            ascii_val = int(ascii_val)
            char_val = chr(ascii_val)
            print("CHAR ==> ",char_val)

        except ValueError:
            print("Invalid input! please enter a number between 0-127.")

        

    

#character

def char_to_ascii():
    print("(Type 'menu' to go back or 'exit' to stop the script)")
    while True:
        
        ascii_char=input("please input a character:")
        

        if ascii_char.lower() == "menu":
           os.system("cls" if os.name == "nt" else "clear")
           break
        
        if ascii_char.lower() == "exit":
            exit()

        if ascii_char == "":
            print("Invalid input! please input a character")
            continue

        if len(ascii_char) != 1:
            print("Invalid input! only one character is allowed.")
            continue
        if ascii_char.isdigit():
            print("numbers are not allowed , please enter a character.")
            continue
        try:
            
            char_val2 = ord(ascii_char)
            
            print("ASCII VALUE ==> ",char_val2)

        except ValueError:
            print("Invalid input! please input a character.")   
    

#string to ASCII values

def text_to_ascii():
    print("(Type 'm' to go back or 'e' to stop the script)")
    while True:   
        text = input("enter your text here:")

        if text.lower() == "m":
            break
            
        if text.lower() == "e":
            exit()
        if text.isdigit():
            print("numbers are not allowed , please enter a text.")
            continue
        if text.lower() == "":
            print("invalid input! enter a text.")
            continue
        if len(text) == 1:
                print("single char not allowed, please enter a text.")
                continue
        try:

            ascii_list = [ord(char) for char in text]

            print("ASCII VALUES ARE ==> ",ascii_list)
        except ValueError:
                    print("Invalid input! please input a character.")

        
    




while True:

    os.system("cls" if os.name == "nt" else "clear")
    # MAIN PAGE
    print("                                 ")
    print("                                 ")
    print("░█████╗░░██████╗░█████╗░██╗██")
    print("██╔══██╗██╔════╝██╔══██╗██║██║")
    print("███████║╚█████╗░██║░░╚═╝██║██║")
    print("██╔══██║░╚═══██╗██║░░██╗██║██║")
    print("██║░░██║██████╔╝╚█████╔╝██║██║")
    print("                              ")
    print("████████╗░█████╗░░█████╗░██╗░░")
    print("╚══██╔══╝██╔══██╗██╔══██╗██║░░░░")
    print("░░░██║░░░██║░░██║██║░░██║██║░░░░")
    print("░░░██║░░░██║░░██║██║░░██║██║░░░░")
    print("░░░██║░░░╚█████╔╝╚█████╔╝███████╗")
    print("                                 ")
    print("█▀▄▀█ █ █▀▀ █▄▀   █▀ █▀▀ █▀▀ █░█ █▀█ █ ▀█▀ █▄█")
    print("█░▀░█ █ █▄▄ █░█   ▄█ ██▄ █▄▄ █▄█ █▀▄ █ ░█░ ░█")
    print("                                 ")
    print("                                 ")
    print("                                 ")
    print("                                 ")
    print("Options Menu: \n")
    print("1. ASCII code to character: \n")
    print("2.Character to ASCII value: \n")
    print("3.Text to ASCII values:")
    print("                                 ")
    print("                                 ")
    options = input("Choose an option: 1 , 2 , 3 or e to exit! \n")

    if options == "1":
        ascii_to_char()

    elif options == "2":
        char_to_ascii()

    elif options == "3":
        text_to_ascii()

    elif options == "e":
        print("Bye!")
        exit()

    else:
        print("Invalid option!")









