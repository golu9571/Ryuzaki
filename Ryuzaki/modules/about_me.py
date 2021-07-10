import io
from Ryuzaki.events import register
from Ryuzaki import telethn
from telethon import types
from telethon import events, Button
from telethon.tl import functions, types
from telethon.tl.types import *

AB_TXT = """
Ryuzaki bot - A bot to manage your groups with additional features
Here's the about menu of Ryuzaki.

Almost all modules usage defined in the help menu, checkout by sending /help

Report error/bugs here @RyuzakiSupportChat.
"""

@telethn.on(events.callbackquery.CallbackQuery(data="about_me"))
async def _(event):

     await event.edit(AB_TEXT, buttons=[
     [Button.inline("T&C", data="tc"), Button.inline("Contributors", data="cb")],
     [Button.inline("Dev", data="dev"), Button.inline("About Me", data="ab")],
     [Button.inline("Back", data="RyuzakiBot_back")]])

#T&C

TC_TXT = """
**Terms and Conditions:**

• Only your first name, last name(if any) and username(if any) is stored.
• No group ID or it's messages are stored, We respect everyone's privacy.
• Don't spam commands, buttons, or anything in bot PM, if we found anyone doing than he will probhited to use Nidhi permanently.
• Messages between Bot & you is only infront of your eyes and there is no backuse of it..
• NSFW will get permanent global ban in Nidhi which never removes, report spammers here -> @RyuzakiSupportChat.

NOTE: **Terms and Conditions will be change anytime.**

**Join @RyuzakiNews for Updates.
Join @RyuzakiSupportChat to get answer of yours questions.**
"""

@telethn.on(events.callbackquery.CallbackQuery(data="tc"))
async def _(event):

     await event.edit(TC_TEXT, buttons=[[Button.inline("Back", data="about_me")]])
