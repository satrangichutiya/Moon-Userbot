from pyrogram import Client, filters
import asyncio
import random

FAKE_TARGETS = [
    "NASA", "Google", "Facebook", "Twitter", "Indian Government",
    "CBI Database", "FBI Servers", "Instagram", "Netflix", "YouTube",
    "Random User", "Rival Hacker", "Anonymous Group", "Bank Server"
]

@Client.on_message(filters.command("hack", prefixes=".") & filters.me)
async def fake_hack(_, message):
    target = message.text.split(None, 1)
    if len(target) == 2:
        victim = target[1]
    else:
        victim = random.choice(FAKE_TARGETS)

    await message.edit(f"🔍 Target locked: `{victim}`...\nInitializing hack sequence...")

    stages = [
        "📡 Connecting to server...",
        "🔐 Bypassing firewall...",
        "💣 Injecting trojan...",
        "📁 Downloading data...",
        "📦 Compressing files...",
        "📤 Uploading to remote server...",
        "⚠️ Tracing IP address...",
        "📡 Disconnecting traces...",
        "📁 Deleting logs...",
        "✅ Hack complete on `{}`!".format(victim)
    ]

    for stage in stages:
        await asyncio.sleep(1.5)
        await message.edit(stage)

    await asyncio.sleep(1.5)
    await message.edit(f"💀 Target `{victim}` successfully hacked!\nAll data secured! 👨‍💻")
