from colorama import *
import tkinter as tk
from tkinter import filedialog
from modules.base64decoder import *
import json
import inquirer
import os


def hidenchat_messages_menu():
    #Open file selection prompt
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        filetypes=[("JSON files", "*.json")],
        initialfile="result.json"
    )

    # Load the JSON data from the file
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Check if the bot id matches with @HidenChat_bot
    if data.get("id") != 467034986:
        print(Fore.RED + "ERROR: JSON data does not match the required bot ID." + Fore.WHITE)
        return
    
    # Filter messages
    messages = []
    button_data = {}
    for message in data.get("messages", []):
        if message.get("from_id") == "user467034986" and "inline_bot_buttons" in message:
            for button_row in message["inline_bot_buttons"]:
                for button in button_row:
                    if button.get("text") == "پاسخ↪️":
                        messages.append(message["text"])
                        button_data[message["text"]] = button.get("dataBase64")

    # Display the filtered messages in a menu format
    if messages:
        questions = [inquirer.List('choice',
                                   message="Select a message to extract the chat ID",
                                   choices=messages)]
        answer = inquirer.prompt(questions)

        selected_message = answer['choice']

        chat_id = base64decoder(button_data[selected_message], 1).split("/")[0]
        message_id = base64decoder(button_data[selected_message], 1).split("/")[1]
        print(Fore.WHITE + "Chat ID is : " + Fore.CYAN + chat_id + Fore.WHITE)
        print(Fore.WHITE + "Message ID is : " + Fore.CYAN + message_id + Fore.WHITE)
    else:
        print("No messages found with the specified criteria.")


def hidenchat():
    print("Tutorial: ")
    print("  1. Export chat history of @HidenChat_bot")
    print("  2. Import exported result.json file")
    print("  3. Select the message you want to extract the chat ID from")
    print("  4. Use @usinfobot to get username of the user form it's chat id\n")
    print(Fore.YELLOW + "Note: " + Fore.WHITE + "@usinfobot bot is not working for all users")
    print(Fore.YELLOW + "Note: " + Fore.WHITE + "Persian and Arabic messages may have problems displaying")
    print(Fore.RESET)
    input(Fore.GREEN + "Press any key to select file" + Fore.WHITE)
    hidenchat_messages_menu()