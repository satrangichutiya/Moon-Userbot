import random
from pyrogram import Client, filters
from .help import add_command_help

hl = "!"

toxics = [
    "looks like you were coded in HTML without CSS.",
    "has the personality of a forwarded WhatsApp joke.",
    "was rejected by both ChatGPT *and* Bing AI.",
    "got roasted by their own reflection.",
    "thinks '404 error' is a compliment.",
    "still buffering in real life."
]

@Client.on_message(filters.command("toxic", prefixes=hl) & filters.me)
async def toxic_gen(client, message):
    if len(message.command) < 2:
        return await message.reply("💀 Use: `!toxic <name>`")
    name = message.text.split(" ", 1)[1]
    roast = random.choice(toxics)
    await message.reply(f"💢 {name} {roast}")

add_command_help("•─╼⃝𖠁 Toxic", [[f"{hl}toxic <name>", "Gives an AI-style roast for fun."]])
