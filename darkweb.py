from pyrogram import Client, filters
import random
import string

def gen_onion():
    return ''.join(random.choices(string.ascii_lowercase + "234567", k=16)) + ".onion"

@Client.on_message(filters.command("onion", "!") & filters.me)
async def onion_link(client, message):
    site = gen_onion()
    await message.reply(f"🕸️ Here's your secret site:\n`http://{site}`")
