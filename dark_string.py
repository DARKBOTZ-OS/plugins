import os
os.system("pip install telethon")
os.system("pip install pyrogram")
from pyrogram import Client
from telethon.sessions import StringSession
from telethon.sync import TelegramClient


print("•••   DARKBOT  SESSION  GENERATOR   •••")
print("\nHello!! Welcome to DARKBot Session Generator\n")
okvai = input("Enter 69 to continue: ")
if okvai == "69":
    print("Choose the string session type: \n1. DarkBot)
    library = input("\nYour Choice: ")
    if library == "1":
        print("\nTelethon Session For DarkBot")
        APP_ID = int(input("\nEnter APP ID here: "))
        API_HASH = input("\nEnter API HASH here: ")
        with TelegramClient(StringSession(), APP_ID, API_HASH) as hellbot:
            print("\nYour DarkBot Session Is sent ur Telegram Saved Messages.")
            hellbot.send_message("me", f"#DARKBOT #DARKBOT_SESSION \n\n`{darkbot.session.save()}`")
    elif library == "2":
        print("Pyrogram Session for Music Bot")
        APP_ID = int(input("\nEnter APP ID here: "))
        API_HASH = input("\nEnter API HASH here: ")
        with Client(':memory:', api_id=APP_ID, api_hash=API_HASH) as hellbot:
            print("\nYour DarkBot Session Is sent in your Telegram Saved Messages.")
            darkbot.send_message("me", f"#DARKBOT_MUSIC #DARKBOT_SESSION\n\n`{darkbot.export_session_string()}`")
    else:
        print("Please Enter 1 or 2 only.")
else:
    print("Bhag jaa bhosdike")
