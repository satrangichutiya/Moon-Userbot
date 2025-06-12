import random
from pyrogram import Client, filters
from .help import add_command_help

hl = "!"

futures = [
    "Banega OnlyFans model for pigeons 🐦",
    "2026 me Mars se rishta ayega 👽",
    "Meme ban jaayega: ‘When life gives you math’ 🧮",
    "Apna crypto launch karega: ‘BKL Coin’ 💰",
    "AI girlfriend chhod ke real ex wapas ayegi 💔",
    "Tera future: 5 missed calls from Zomato 🍔"
]

@Client.on_message(filters.command("future", prefixes=hl) & filters.me)
async def bhavishyavani(client, message):
    name = message.text.split(" ", 1)[1] if len(message.command) > 1 else "Tu"
    prediction = random.choice(futures)
    await message.reply(f"🔮 {name} ka bhavishya:\n{prediction}")

add_command_help("•─╼⃝𖠁 Future", [[f"{hl}future <name>", "Predicts a random funny future."]])
