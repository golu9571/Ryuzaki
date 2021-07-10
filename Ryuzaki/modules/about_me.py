import io
from Ryuzaki.events import register
from Ryuzaki import telethn
from telethon import types
from telethon import events, Button
from telethon.tl import functions, types
from telethon.tl.types import *

AB_TXT = """
**Ryuzaki bot - A bot to manage your groups with additional features
Here's the about menu of Ryuzaki.**

**Almost all modules usage defined in the help menu, checkout by sending /help**

**Report error/bugs here @RyuzakiSupportChat.**
"""

@telethn.on(events.callbackquery.CallbackQuery(data="about_me"))
async def _(event):

     await event.edit(AB_TXT, buttons=[
     [Button.inline("T&C", data="tc"), Button.inline("System", data="sys")],
     [Button.inline("About Me", data="ab")],
     [Button.inline("Back", data="Ryuzakibot_back")]])

#T&C

TC_TXT = """
**Terms and Conditions:**

• Only your first name, last name(if any) and username(if any) is stored.
• No group ID or it's messages are stored, We respect everyone's privacy.
• Don't spam commands, buttons, or anything in bot PM, if we found anyone doing than he will probhited to use Nidhi permanently.
• Messages between Bot & you is only infront of your eyes and there is no backuse of it..
• NSFW will get permanent global ban in Ryuzaki which never removes, report spammers here -> @RyuzakiSupportChat.

NOTE: **Terms and Conditions will be change anytime.**

**Join @RyuzakiNews for Updates.
Join @RyuzakiSupportChat to get answer of yours questions.**
"""

@telethn.on(events.callbackquery.CallbackQuery(data="tc"))
async def _(event):

     await event.edit(TC_TXT, buttons=[[Button.inline("Back", data="about_me")]])

#Contributors

SYS_TXT = """
**Here Is The Details About System :**

**× Written In : Pyrogram, Telethon, PTB
× Alive Since : July/09/2021
× Hosted On : Heroku
× Database : SQL, Redis, Mongo
× Chats Under Me : 8
× Developed By @EvilBinner**
"""

@telethn.on(events.callbackquery.CallbackQuery(data="sys"))
async def _(event):

     await event.edit(SYS_TXT, buttons=[[Button.inline("Back", data="about_me")]])

AB_TR = """
**I am Ryuzaki, a python based Telegram Group Management bot

Currently I'm managing 5+ chats

My developers:
• @EvilBinner
• @Madboi_xD

Thanks to My Sudo & Support users who makes me usable for you!

Updates channel: @RyuzakiNews
support chat: @RyuzakiUpdates**
"""

@telethn.on(events.callbackquery.CallbackQuery(data="ab"))
async def _(event):

     await event.edit(AB_TR, buttons=[[Button.inline("Back", data="about_me")]])
