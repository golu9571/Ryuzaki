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
    [Button.inline("Admin Help", data="admin_help"), Button.inline("Extra Help", data="extra_help")],
    [Button.inline("User Help", data="user_help"), Button.inline("Video Tutorial", data="v_tuts")],
    [Button.inline("Back", data="Ryuzakibot_back"), Button.inline("Main Menu", data="help_back")]]

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

USER_TXT = """
Here is the help for the **Users** module:

 • /runs: reply a random string from an array of replies
 • /slap: slap a user, or get slapped if not a reply
 • /shrug: get shrug XD
 • /table: get flip/unflip :v
 • /decide: Randomly answers yes/no/maybe
 • /toss: Tosses A coin
 • /bluetext: check urself :V
 • /roll: Roll a dice
 • /rlg: Join ears,nose,mouth and create an emo ;-;
 • /shout <keyword>: write anything you want to give loud shout
 • /weebify <text>: returns a weebified text
 • /sanitize: always use this before /pat or any contact
 • /pat: pats a user, or get patted
 • /8ball: predicts using 8ball method

**This is only Basic Commands For Full Command List** - `/help memes`.

**List May Update In Next Update.**

**✨ Join Updates : @RyuzakiNews**
"""

@telethn.on(events.callbackquery.CallbackQuery(data="user_help"))
async def _(event):

    await event.edit(USER_TXT, buttons=[
    [Button.inline("Back", data="basic_help")]])

V_TXT = """
**Video Tutorial How To Use Ryuzaki?**

**Click Here To See :** [Watch](https://t.me/RyuzakiNews/4)

**More Video tutorial regarding My use will updated soon
Report bugs & for more tutorials, Ask** [here](https://EvilBinner)
"""

@telethn.on(events.callbackquery.CallbackQuery(data="v_tuts"))
async def _(event):

    await event.edit(V_TXT, buttons=[
    [Button.inline("Back", data="basic_help")]])

EXTRA_TXT = """
Get information about anime, manga or characters from AniList

*Available commands:*
 • `/anime <anime>`: returns information about the anime.
 • `/character <character>`: returns information about the character.
 • `/manga <manga>`: returns information about the manga.
 • `/user <user>`: returns information about a MyAnimeList user.
 • `/upcoming`: returns a list of new anime in the upcoming seasons.
 • `/kaizoku <anime>`: search an anime on animekaizoku
 • `/kayo <anime>`: search an anime on animekayo
 • `/airing <anime>`: returns anime airing info.
 • /whatanime - reply to gif or video
"""

@telethn.on(events.callbackquery.CallbackQuery(data="extra_help"))
async def _(event):

    await event.edit(EXTRA_TXT, buttons=[
    [Button.inline("Back", data="basic_help")]])

