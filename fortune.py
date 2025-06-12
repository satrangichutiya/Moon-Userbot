from pyrogram import Client, filters
import random
from .help import add_command_help

fortunes = [
    "💰 Aaj paisa barsega!", "💔 Breakup ke chances high hain!",
    "🧠 Bada idea aane wala hai!", "⚠️ Dhokha milega kisi se!",
    "👀 Koi stalk kar raha hai tujhe!", "🎉 Tera time aagaya bhai!"
]

@Client.on_message(filters.command("fortune", prefixes="!") & filters.me)
async def fortune_cmd(client, message):
    await message.reply(random.choice(fortunes))

add_command_help("fortune", [["fortune", "Batao aaj ki taqdeer kaisi hai."]])
