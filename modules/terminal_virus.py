import asyncio
from pyrogram import Client, filters
from random import randint, choice

COMMAND = "virus"
TRIGGER = "!"

ascii_banner = """
██████╗ ██╗   ██╗██████╗ ███████╗██████╗ ██╗   ██╗███████╗
██╔══██╗██║   ██║██╔══██╗██╔════╝██╔══██╗╚██╗ ██╔╝██╔════╝
██████╔╝██║   ██║██████╔╝█████╗  ██████╔╝ ╚████╔╝ █████╗  
██╔═══╝ ██║   ██║██╔═══╝ ██╔══╝  ██╔═══╝   ╚██╔╝  ██╔══╝  
██║     ╚██████╔╝██║     ███████╗██║        ██║   ███████╗
╚═╝      ╚═════╝ ╚═╝     ╚══════╝╚═╝        ╚═╝   ╚══════╝
"""

@Client.on_message(filters.command(COMMAND, TRIGGER) & filters.me)
async def virus_terminal(client, message):
    await message.delete()

    temp = await message.reply("Initializing terminal...")

    steps = [
        "[█░░░░░░░░░░] Loading virus.py...",
        "[███░░░░░░░░] Injecting payload...",
        "[███████░░░░] Bypassing firewalls...",
        "[██████████] Compiling exploit...",
        "[██████████] Establishing backdoor...",
        "[██████████] ✅ Injection complete!"
    ]

    for step in steps:
        await asyncio.sleep(1.3)
        await temp.edit(step)

    await asyncio.sleep(1)
    await temp.edit("**Executing terminal virus...**\n```python\nRunning payload.sh...\n```")

    await asyncio.sleep(2)
    fake_logs = [
        "Overwriting boot sector...",
        "Deleting C:/Windows/System32...",
        "Injecting trojan.exe to /root/bin...",
        "Fetching IP address... [SUCCESS]",
        "Activating webcam stream... [DENIED]",
        "Encrypting personal files...",
        "Spamming PornHub links to contacts...",
        "Mining Dogecoin...",
    ]

    for log in fake_logs:
        await asyncio.sleep(1.2)
        await temp.edit(f"`{log}`")

    await asyncio.sleep(1.5)
    await temp.edit("💥 `System Destroyed.`\n💀 **Device Terminated.**\n_Just kidding, it's a prank 😈_")

    # Bonus popup
    await client.send_message(
        message.chat.id,
        "**🎭 TERMINAL VIRUS SIMULATION COMPLETE 🎭**\nTag the next victim using `.virus` command!"
    )
