import inspect
import re

from pathlib import Path
from telethon import events

from .session import D2, D3, D4, D5
from darkbot import CMD_LIST, LOAD_PLUG, bot
from darkbot.config import Config
from darkbot.sql.gvar_sql import gvarstat


def dark_cmd(
    pattern: str = None,
    allow_sudo: bool = True,
    disable_edited: bool = False,
    forword=False,
    command: str = None,
    **args,
):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    if "disable_edited" in args:
        del args["disable_edited"]

    args["blacklist_chats"] = True
    black_list_chats = list(Config.BL_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats
    sudo_user = []
    if gvarstat("SUDO_USERS"):
        a = gvarstat("SUDO_USERS").split(" ")
        for c in a:
            a = int(c)
            sudo_user.append(a)

    if pattern is not None:
        global dark_reg
        global sudo_reg
        if (
            pattern.startswith(r"\#")
            or not pattern.startswith(r"\#")
            and pattern.startswith(r"^")
        ):
            dark_reg = sudo_reg = re.compile(pattern)
        else:
            dark_ = "\\" + Config.HANDLER
           sudo_ = "\\" + Config.SUDO_HANDLER
            dark_reg = re.compile(dark_ + pattern)
            sudo_reg = re.compile(sudo_ + pattern)
            if command is not None:
                cmd1 = dark_ + command
                cmd2 = sudo_ + command
            else:
                cmd1 = (
                    (dark_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
                cmd2 = (
                    (sudo_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd1)
            except BaseException:
                CMD_LIST.update({file_test: [cmd1]})


    def decorator(func):
        if not disable_edited:
            bot.add_event_handler(func, events.MessageEdited(**args, outgoing=True, pattern=dark_reg))
        bot.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=dark_reg))
        if allow_sudo:
            if not disable_edited:
                bot.add_event_handler(func, events.MessageEdited(**args, from_users=sudo_user, pattern=sudo_reg))
            bot.add_event_handler(func, events.NewMessage(**args, from_users=sudo_user, pattern=sudo_reg))
        if D2:
            if not disable_edited:
                D2.add_event_handler(func, events.MessageEdited(**args, outgoing=True, pattern=dark_reg))
            D2.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=dark_reg))
        if D3:
            if not disable_edited:
                D3.add_event_handler(func, events.MessageEdited(**args, outgoing=True, pattern=dark_reg))
           D3.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=dark_reg))
        if D4:
            if not disable_edited:
                D4.add_event_handler(func, events.MessageEdited(**args, outgoing=True, pattern=dark_reg))
            D4.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=dark_reg))
        if D5:
            if not disable_edited:
                D5.add_event_handler(func, events.MessageEdited(**args, outgoing=True, pattern=dark_reg))
            D5.add_event_handler(func, events.NewMessage(**args, outgoing=True, pattern=dark_reg))
        try:
            LOAD_PLUG[file_test].append(func)
        except Exception:
            LOAD_PLUG.update({file_test: [func]})
        return func

    return decorator


def dark_handler(
    **args,
):
    def decorator(func):
        bot.add_event_handler(func, events.NewMessage(**args, incoming=True))
        if D2:
            D2.add_event_handler(func, events.NewMessage(**args, incoming=True))
        if D3:
            D3.add_event_handler(func, events.NewMessage(**args, incoming=True))
        if D4:
            D4.add_event_handler(func, events.NewMessage(**args, incoming=True))
        if D5:
            D5.add_event_handler(func, events.NewMessage(**args, incoming=True))
        return func

    return decorator
