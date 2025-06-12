import random
from pyrogram import Client, filters
from .help import add_command_help

hl = "!"

traits = [
    "🔥 90% Savage", "🧠 85% Genius", "💩 45% Noob", "👑 100% Royal Blood",
    "😈 70% Evil", "👻 66% Ghost", "💖 88% Lover", "⚡ 99% Cringe-proof"
]

@Client.on_message(filters.command("dna", prefixes=hl) & filters.me)
async def fake_dna(client, message):
    if len(message.command) < 2:
        return await message.reply("🧬 Use: `!dna <name>`")
    name = message.text.split(" ", 1)[1]
    selected = random.sample(traits, 3)
    await message.reply(f"🧬 DNA Results for `{name}`:\n\n" + "\n".join(selected))

add_command_help("•─╼⃝𖠁 DNA", [[f"{hl}dna <name>", "Gives fun fake DNA analysis for any name."]])
