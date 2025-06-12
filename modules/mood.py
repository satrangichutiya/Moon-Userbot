import random
from pyrogram import Client, filters
from .help import add_command_help

hl = "!"

moods = [
    "😡 Gusse wala mood!",
    "😂 Hasaane ka mood hai aaj!",
    "😎 Bindass & cool mood 🔥",
    "😴 Neend mein hai lagta 😪",
    "🥰 Pyaar pyaar sa lag raha hai!",
    "🤯 Dimaag ka dahi ho gaya 😵",
    "😭 Emotional ho gaya yaar 😢",
    "🤡 Joker mood active!",
    "💩 Bakwaas mood detected 💀",
    "🧠 Genius mode ON 🤓"
]

@Client.on_message(filters.command("mood", prefixes=hl) & filters.me)
async def mood_scanner(client, message):
    args = message.text.split(" ", 1)
    target = args[1] if len(args) > 1 else message.from_user.first_name
    mood = random.choice(moods)
    await message.reply(f"🔍 Scanning mood of **{target}**...\n\n🎭 Mood: {mood}")

add_command_help(
    "•─╼⃝𖠁 Mᴏᴏᴅ",
    [
        [f"{hl}mood [name]", "Scan the mood of a user — mazedaar result! 🎭"]
    ],
)
