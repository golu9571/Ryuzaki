import io
from Ryuzaki.events import register
from Ryuzaki import telethn
from Ryuzaki import telethn
from telethon import types
from telethon import events, Button
from telethon.tl import functions, types
from telethon.tl.types import *

HELP_TEXT = """
**Here's basic Help regarding How to use Me?**

• Firstly Add me to your group by pressing [here](http://t.me/Ryuzakibot?startgroup=true)

• After adding promote me manually with full rights for faster experience.

• Than send `/admincache@TheRyuzakiBot` in that chat to refresh admin list in My database.

**All done now use below given button's to know about use.**
"""

btn =[
    [Button.inline("Admin Help", data="admin_help"), Button.inline("Bans", data="bans")],
    [Button.inline("User Help", data="user_help"), Button.inline("Video Tutorial", data="v_tuts")],
    [Button.inline("Extra Help", data="extra_help")],
    [Button.inline("Back", data="Ryuzakibot_back")]]

@telethn.on(events.callbackquery.CallbackQuery(data="basic_help"))
async def _(event):

    await event.edit(HELP_TEXT, buttons=btn)

ADMIN_TXT = """
**Here is the help for the Admin!**

• `/admins`: list of admins in the chat
• `/pin`: silently pins the message replied to - add 'loud' or 'notify' to give notifs to users
• `/unpin`: unpins the currently pinned message
• `/invitelink`: gets invitelink
• `/promote`: promotes the user
• `/demote`: demotes the user.
• `/setsticker`: As a reply to some sticker to set it as group sticker set!
• `/admincache`: force refresh the admins list.

**This is only Basic Commands For Full Command List** - `/help admin`.

**List May Update In Next Update.**

**✨ Join Updates : @RyuzakiNews**
"""

@telethn.on(events.callbackquery.CallbackQuery(data="admin_help"))
async def _(event):

    await event.edit(ADMIN_TXT, buttons=[
    [Button.inline("Back", data="basic_help")]])

