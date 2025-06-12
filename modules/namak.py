from pyrogram import Client, filters
import random
from .help import add_command_help

hl = "!"

roasts = [
    "Tumse better toh notepad ki autosave hai 💻",
    "Duniya gol hai, tu straight nahi ho sakta 💀",
    "Bina soche kaam karta hai... jaise Airtel internet.",
    "IQ negative, brain error 404."
]

@Client.on_message(filters.command("namak", prefixes=hl) & filters.me)
async def roast_user(client, message):
    name = message.text.split(" ", 1)[1] if len(message.command) > 1 else "Koi"
    await message.reply(f"🧂 Roast for {name}:\n{random.choice(roasts)}")

add_command_help("•─╼⃝𖠁 Namak", [[f"{hl}namak <name>", "Roast someone with spicy logic."]])
