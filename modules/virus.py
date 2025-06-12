from pyrogram import Client, filters
import asyncio
from .help import add_command_help

hl = "!"

@Client.on_message(filters.command("virus", prefixes=hl) & filters.me)
async def virus_sim(client, message):
    if len(message.command) < 2:
        return await message.edit("⚠️ Usage: !virus <target>")
    target = message.command[1]
    msg = await message.reply(f"Injecting virus in {target}'s phone...")
    stages = [
        "🧬 Initializing system breach...",
        "🔓 Bypassing firewall...",
        "📡 Connecting to mainframe...",
        "📥 Downloading contacts...",
        "📷 Stealing gallery...",
        "💣 Planting malware...",
        "💾 Saving data to `/moon/hacks/`...",
        "✅ Hack complete. Target destroyed!"
    ]
    for stage in stages:
        await asyncio.sleep(1.5)
        await msg.edit(stage)

add_command_help("•─╼⃝𖠁 Virus", [[f"{hl}virus <target>", "Simulates a crazy hacking attack."]])
