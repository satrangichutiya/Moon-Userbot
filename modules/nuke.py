import asyncio
from pyrogram import Client, filters
from .help import add_command_help

hl = "!"

fake_lines = [
    "Initializing Target Lock...",
    "Bypassing Firewall...",
    "Access Granted ✅",
    "Planting Trojan 🐞...",
    "Uploading Malware ☣️...",
    "Injecting SQL 💉...",
    "Nuking in 3...",
    "2...",
    "1...",
    "💥 BOOM! System Terminated ☠️"
]

@Client.on_message(filters.command("nuke", prefixes=hl) & filters.me)
async def fake_nuke(client, message):
    sent = await message.reply("💣 Nuke Protocol Initiated...")
    for line in fake_lines:
        await asyncio.sleep(1)
        await sent.edit(line)

add_command_help("•─╼⃝𖠁 Nuke", [[f"{hl}nuke", "Simulates a hacking/virus nuke attack (just for fun)."]])
