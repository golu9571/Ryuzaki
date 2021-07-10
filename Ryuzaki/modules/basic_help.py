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

*All done now use below given button's to know about use.*
"""

@telethn.on(events.callbackquery.CallbackQuery(data="basic_help"))
async def _(event):

    await event.edit(HELP_TEXT, buttons=[[Button.inline("Admin Help", data="admin_help")]])
