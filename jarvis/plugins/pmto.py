# By @HeisenbergTheDanger for TeleBot
# @its_xditya
# Kangers keep credits

from jarvis.utils import admin_cmd


@jarvis.on(admin_cmd("pmto ?(.*)"))
async def pmto(event):
    a = event.pattern_match.group(1)
    b = a.split(" ")
    chat_id = b[0]
    try:
        chat_id = int(chat_id)
    except:
        pass
    msg = ""
    for i in b[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await jbot.send_message(chat_id, msg)
        await event.edit("Message sent!")
    except:
        await event.edit("Something went wrong.")
