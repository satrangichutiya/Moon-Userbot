import random
from pyrogram import Client, filters
from .help import add_command_help

hl = "!"

replies = [
    "Mujhe kya pata, main toh Pyrogram hoon 😤",
    "Is sawal ka jawab pehle IPL me nahi mila, yahan kya milega?",
    "Science bhi confuse hai iss baat pe 💀",
    "Sochne do... beep... error... bakchodi overload 🧠💥"
]

@Client.on_message(filters.command("bakchodi", prefixes=hl) & filters.me)
async def useless_gyan(client, message):
    topic = message.text.split(" ", 1)[1] if len(message.command) > 1 else "life"
    await message.reply(f"🧠 Regarding *{topic}*:\n{random.choice(replies)}")

add_command_help("•─╼⃝𖠁 Bakchodi", [[f"{hl}bakchodi <topic>", "Gives a useless but funny AI answer."]])
