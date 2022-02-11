import telethon.utils

from telethon.tl.functions.users import GetFullUserRequest

from .session import dark, D2, D3, D4, D5
from darkbot.sql.gvar_sql import gvarstat


async def clients_list(Config, Dark, D2, D3, D4, D5):
    user_ids = []
    if gvarstat("SUDO_USERS"):
        a = gvarstat("SUDO_USERS").split(" ")
        for b in a:
            c = int(b)
            user_ids.append(c)
    main_id = await Dark.get_me()
    user_ids.append(main_id.id)

    try:
        if D2 is not None:
            id2 = await D2.get_me()
            user_ids.append(id2.id)
    except:
        pass

    try:
        if D3 is not None:
            id3 = await D3.get_me()
            user_ids.append(id3.id)
    except:
        pass

    try:
        if D4 is not None:
            id4 = await D4.get_me()
            user_ids.append(id4.id)
    except:
        pass

    try:
        if D5 is not None:
            id5 = await D5.get_me()
            user_ids.append(id5.id)
    except:
        pass

    return user_ids


async def client_id(event, botid=None):
    if botid is not None:
        uid= await event.client(GetFullUserRequest(botid))
        DGABHI = uid.user.id
        DARK_USER = uid.user.first_name
        dark_mention = f"[{DARK_USER}](tg://user?id={DGABHI})"
    else:
        client = await event.client.get_me()
        uid telethon.utils.get_peer_id(client)
        DGABHI = uid
        DARK_USER = client.first_name
        dark_mention = f"[{DARK_USER}](tg://user?id={DGABHI})"
    return DGABHI, DGABHI_USER, dark_mention
