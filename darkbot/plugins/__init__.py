import datetime
import time

from darkbot import *
from darkbot.clients import *
from darkbot.config import Config
from darkbot.helpers import *
from darkbot.utils import *
from darkbot.random_strings import *
from darkbot.version import __hell__
from darkot.sql.gvar_sql import gvarstat
from telethon import version

dark_logo = "./darkbot/resources/pics/darkbot_logo.jpg"
cjb = "./darkbot/resources/pics/cjb.jpg"
restlo = "./darkbot/resources/pics/rest.jpeg"
shuru = "./darkbot/resources/pics/shuru.jpg"
shhh = "./darkbot/resources/pics/chup_madarchod.jpeg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
hell_ver = __hell__
tel_ver = version.__version__

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

sudos = Config.SUDO_USERS
if sudos:
    is_sudo = "True"
else:
    is_sudo = "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"


my_channel = Config.MY_CHANNEL or "itz_dark_userbot"
my_group = Config.MY_GROUP or "Darkbot_Support"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/itz_dark_userbot"
hell_channel = f"[†hê ∂αякẞø†]({chnl_link})"
grp_link = "https://t.me/DarkBot_Support"
dark_grp = f"[∂αякẞø† Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
# will add more soon

# darkbot
