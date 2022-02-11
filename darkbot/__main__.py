import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

from darkbot import LOGS, bot, tbo
from darkbot.clients.session import DarK, D2, D3, D4, D5
from darkbot.config import Config
from darkbot.utils import load_module
from darkbot.version import __dark__ as darkver
hl = Config.HANDLER

DARK_PIC = "https://telegra.ph/file/fd93f6309369694e71644.jpg"


# let's get the bot ready
async def d1(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"DARKBOT_SESSION - {str(e)}")
        sys.exit()


# Multi-Client helper
async def dark_client(client):
    client.me = await client.get_me()
    client.uid = telethon.utils.get_peer_id(client.me)


# Multi-Client Starter
def darks():
    failed = 0
    if Config.SESSION_2:
        LOGS.info("SESSION_2 detected! Starting 2nd Client.")
        try:
            D2.start()
            D2.loop.run_until_complete(hell_client(H2))
        except:
            LOGS.info("SESSION_2 failed. Please Check Your String session.")
            failed += 1

    if Config.SESSION_3:
        LOGS.info("SESSION_3 detected! Starting 3rd Client.")
        try:
            D3.start()
            D3.loop.run_until_complete(hell_client(H3))
        except:
            LOGS.info("SESSION_3 failed. Please Check Your String session.")
            failed += 1

    if Config.SESSION_4:
        LOGS.info("SESSION_4 detected! Starting 4th Client.")
        try:
            D4.start()
            D4.loop.run_until_complete(hell_client(H4))
        except:
            LOGS.info("SESSION_4 failed. Please Check Your String session.")
            failed += 1

    if Config.SESSION_5:
        LOGS.info("SESSION_5 detected! Starting 5th Client.")
        try:
            D5.start()
            D5.loop.run_until_complete(hell_client(H5))
        except:
            LOGS.info("SESSION_5 failed. Please Check Your String session.")
            failed += 1

    if not Config.SESSION_2:
        failed += 1
    if not Config.SESSION_3:
        failed += 1
    if not Config.SESSION_4:
        failed += 1
    if not Config.SESSION_5:
        failed += 1
    return failed


# darkbot starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = tbot
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("🔰 Starting DarkBot 🔰")
            bot.loop.run_until_complete(h1(Config.BOT_USERNAME))
            failed_client = hells()
            global total
            total = 5 - failed_client
            LOGS.info("🔥 DarkBot Startup Completed 🔥")
            LOGS.info(f"» Total Clients = {total} «")
        else:
            bot.start()
            failed_client = hells()
            total = 5 - failed_client
            LOGS.info(f"» Total Clients = {total} «")
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()


# imports plugins...
path = "darkbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))


# let the party begin...
LOGS.info("Starting Bot Mode !")
tbot.start()
LOGS.info("⚡ Your  Darkbot Is Now Working ⚡")
LOGS.info("Head to @Itz_Dark_userBot for Updates. Also join chat group to get help regarding to DarkBot.")
LOGS.info(f"» Total Clients = {total} «")

# that's life...
async def dark_is_on():
    try:
        x = await bot.get_me()
        xid = telethon.utils.get_peer_id(x)
        send_to = Config.LOGGER_ID if Config.LOGGER_ID != 0 else xid
        await bot.send_file(
            send_to,
            DARK_PIC,
            caption=f"#START \n\n<b><i>Version :</b></i> <code>{darkver}</code> \n<b><i>Clients :</b></i> <code>{total}</code> \n\n<b><i>»» <u><a href='https://t.me/Its_HellBot'>†hê Hêllẞø†</a></u> ««</i></b>",
            parse_mode="HTML",
        )
    except Exception as e:
        LOGS.info(str(e))
# Join DarkBot Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@Itz_dark_userbot"))
    except BaseException:
        pass
    try:
        if D2:
            await D2(JoinChannelRequest("@Itz_dark_userbot"))
    except BaseException:
        pass
    try:
        if D3:
            await D3(JoinChannelRequest("@itz_dark_userbot"))
    except BaseException:
        pass
    try:
        if D4:
            await D4(JoinChannelRequest("@itz_dark_userbot"))
    except BaseException:
        pass
    try:
        if D5:
            await D5(JoinChannelRequest("@itz_dark_userbot"))
    except BaseException:
        pass
# Why not come here and chat??
    try:
        await bot(ImportChatInviteRequest('4ny4S5P2hx9kNDdl'))
    except BaseException:
        pass
    try:
        if D2:
            await D2(ImportChatInviteRequest('4ny4S5P2hx9kNDdl'))
    except BaseException:
        pass
    try:
        if D3:
            await D3(ImportChatInviteRequest('4ny4S5P2hx9kNDdl'))
    except BaseException:
        pass
    try:
        if D4:
            await D4(ImportChatInviteRequest('4ny4S5P2hx9kNDdl'))
    except BaseException:
        pass
    try:

            await D5(ImportChatInviteRequest('4ny4S5P2hx9kNDdl'))
    except BaseException:
        pass



bot.loop.create_task(dark_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

# darkbot
