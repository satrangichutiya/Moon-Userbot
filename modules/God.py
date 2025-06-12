from pyrogram import Client, filters
import random
from .help import add_command_help

hl = "!"

divine_replies = [
    "🕉️ I am everywhere. Even in your CPU.",
    "☁️ Pralay aa raha hai, but chill kr bhakt.",
    "📿 Tere paap bhi /help se clear nahi honge.",
    "⚡ I'm not ChatGPT, I'm ChatGOD."
]

@Client.on_message(filters.command("god", prefixes=hl) & filters.me)
async def god_mode(client, message):
    await message.reply(random.choice(divine_replies))

add_command_help("•─╼⃝𖠁 GodMode", [[f"{hl}god", "Makes bot reply like a divine power."]])
