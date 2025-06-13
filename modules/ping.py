import asyncio
import time
import platform
import psutil
import socket
from datetime import datetime
from pyrogram import Client, filters

TRIGGER = "!"  # Change this if your handler is different

def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "d"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        seconds = int(remainder)
        time_list.append(int(result))
    for i in range(len(time_list)):
        if time_list[i] != 0:
            up_time = str(time_list[i]) + time_suffix_list[i] + " " + up_time
    return up_time.strip()

@Client.on_message(filters.command("ping", prefixes=TRIGGER) & filters.me)
async def advanced_ping(client, message):
    start = time.time()
    uptime_seconds = time.time() - psutil.boot_time()
    uptime = get_readable_time(int(uptime_seconds))

    # Get basic system info
    uname = platform.uname()
    hostname = socket.gethostname()
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent

    animations = [
        "🔍 Pinging system .",
        "🔍 Pinging system ..",
        "🔍 Pinging system ...",
        "💻 Connecting to core server.",
        "💻 Connecting to core server..",
        "💻 Connecting to core server...",
        "⚙️ Authenticating ping response.",
        "⚙️ Authenticating ping response..",
        "⚙️ Authenticating ping response...",
        "🔧 Finalizing response packet.",
        "🔧 Finalizing response packet..",
        "🔧 Finalizing response packet...",
    ]

    # Run animation
    temp = await message.reply("`Initializing...`")
    for frame in animations:
        await temp.edit_text(f"`{frame}`")
        await asyncio.sleep(0.2)

    end = time.time()
    ping_time = (end - start) * 1000

    # Aesthetic font + emojis + info
    result = f"""
💻 **𝙐𝙡𝙩𝙧𝙖 𝙊𝙋 𝙋𝙞𝙣𝙜 𝙎𝙮𝙨𝙩𝙚𝙢** ⚡

📶 **Ping:** `{int(ping_time)} ms`
🧠 **CPU Load:** `{cpu}%`
💾 **RAM Usage:** `{ram}%`
⏱ **Uptime:** `{uptime}`
📡 **Host:** `{HOSTNAME}`
🖥 **OS:** `{uname.system} {uname.release}`
📍 **Time:** `{datetime.now().strftime('%H:%M:%S')}`

⚔️ Powered by 𝙈𝙊𝙊𝙉-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 🌙
"""
    await temp.edit_text(result)
