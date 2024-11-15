import os
import platform
from modules.base64decoder import *
from modules.hidenbot import *
from modules.bchatsbot import *
from modules.bichatbot import *
from colorama import *
import inquirer

#Use clear() to clear console
clear = lambda: os.system('cls')

#Reset Color
def resetcolor():
    print(Fore.RESET)

#App Header
def header():
    clear()
    print(Fore.GREEN + "Telegram Chat Bot Hacking Tool V1.0")
    print(Fore.GREEN + "---" + Fore.WHITE +"@nimazerobit" + Fore.GREEN + "--------------------")
    print(Fore.WHITE + "Operating system : " + Fore.CYAN + platform.system())
    print(Fore.WHITE + "Python version : " + Fore.CYAN + platform.python_version())
    print(Fore.GREEN + "-----------------------------------")
    resetcolor()

#App Menu
def menu():
    header()
    options = ["@HidenChat_bot", "@BChatsBot", "@BiChatBot", "Base64 Decoder", "Exit"]
    question = [inquirer.List('choice', message="Select an option", choices=options)]
    answer = inquirer.prompt(question)
    return options.index(answer['choice'])


def main():
    clear()
    user_choice = menu()
    
    #HidenChat_bot
    if user_choice == 0:
        header()
        hidenchat()

    #BChatsBot
    elif user_choice == 1:
        header()
        bchats()

    #BiChatBot
    elif user_choice == 2:
        header()
        bichat()

    #Base64 Decoder
    elif user_choice == 3:
        header()
        print(base64decoder(input("Enter Base64 : " + Fore.GREEN), 2))

    #Exit
    elif user_choice == 4:
        clear()
        exit()

if __name__=="__main__":
    main()