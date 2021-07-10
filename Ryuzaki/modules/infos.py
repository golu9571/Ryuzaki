from telethon import events, Button, types
from Ryuzaki import telethn
from Ryuzaki.status import *
from telethon.tl.types import ChannelParticipantsAdmins
from datetime import timedelta
from telethon.tl.functions.photos import GetUserPhotosRequest as P
from telethon.tl.functions.users import GetFullUserRequest

@telethn.on(events.NewMessage(pattern="^[!?/]id"))
async def id(event):

    if event.is_private:
       await event.reply(f"Your id is {event.sender_id}.")
       return

    ID = """
Chat- ID: {}
User- ID: {}
"""

    msg = await event.get_reply_message()
    if not msg:
      await event.reply(ID.format(event.chat_id, event.sender_id))
      return

    await event.reply(f"User {msg.sender.first_name} id is {msg.sender_id}.")
 
@telethn.on(events.NewMessage(pattern="^[!?/]info ?(.*)"))
async def info(event):

    sed = await telethn(P(user_id=event.sender_id, offset=42, max_id=0, limit=80))
    hn = await telethn(GetFullUserRequest(event.sender_id))
    text = "**Extracted UserInfo:**\n\n"
    text += "**- First Name:** {}\n"
    text += "**- Last Name:** {}\n"
    text += "**- User ID:** {}\n"
    text += "**- Username:** @{}\n"
    text += "**- Profile Pics:** {}\n"
    text += "**- Link:** [Link](tg://user?id={})\n"

    input_str = event.pattern_match.group(1)
    if not input_str:
          await telethn.send_message(event.chat_id, text.format(hn.user.first_name, hn.user.last_name, event.sender_id, event.sender.username, sed.count, hn.about, event.sender_id))
          return
 
    input_str = event.pattern_match.group(1)
    ha = await telethn.get_entity(input_str)
    hu = await telethn(GetFullUserRequest(id=input_str))
    sedd = await telethn(P(user_id=input_str, offset=42, max_id=0, limit=80))

    text = "**Extracted UserInfo:**\n\n"
    text += "**- First Name:** {}\n"
    text += "**- Last Name:** {}\n"
    text += "**- User ID:** {}\n"
    text += "**- Username:** @{}\n"
    text += "**- Profile Pics:** {}\n"
    text += "**- Link:** [Link](tg://user?id={})\n"

    await event.reply(textn.format(ha.first_name, ha.last_name, ha.id, ha.username, sedd.count, hu.about, ha.id))
   
__mod_name__ = "Info's"

__help__ = """
**This Plugin To Find Details Of Person/Chat ID's**

• /id -  To get current chat id or replied user id.
• /info -  To get info of a user.
"""
