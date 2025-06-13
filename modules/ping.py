import time
import platform
import psutil
import socket
from datetime import datetime
from pyrogram import Client, filters

# Customize your command prefix here
TRIGGER = "!"

# Helper: Uptime in human-readable format
def get_readable_time(seconds: int) -> str:
    count = 0
    result = ''
    time_list = []
    suffixes = ["s", "m", "h", "d"]

    while count < 4:
        count += 1
        if count < 3:
            seconds, remainder = divmod(seconds, 60)
        else:
            seconds, remainder = divmod(seconds, 24)
        time_list.append(int(remainder))

    for i in range(len(time_list)):
        if time_list[i] > 0:
            result = str(time_list[i]) + suffixes[i] + " " + result
    return result.strip()

# Main Ping Command
@Client.on_message(filters.command("ping", prefixes=TRIGGER) & filters.me)
async def ultra_ping(client, message):
    start_time = time.time()
    uptime_seconds = time.time() - psutil.boot_time()
    uptime = get_readable_time(int(uptime_seconds))

    # System info
    uname = platform.uname()
    host = socket.gethostname()
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    time_now = datetime.now().strftime("%H:%M:%S")

    # Simulated animation
    animation = [
        "`> Initializing...`",
        "`> Pinging .`",
        "`> Pinging ..`",
        "`> Pinging ...`",
        "`> Collecting data.`",
        "`> Collecting data..`",
        "`> Collecting data...`",
        "`> Preparing response.`",
        "`> Preparing response..`",
        "`> Preparing response...`"
    ]
    temp = await message.reply_text("`Launching ping...`")
    for i in animation:
        await temp.edit(i)
        await asyncio.sleep(0.15)

    end_time = time.time()
    ping_speed = int((end_time - start_time) * 1000)

    # Final reply
    output = f"""
✨ **𝙐𝙇𝙏𝙍𝘼 𝙋𝙄𝙉𝙂 𝙍𝙀𝙎𝙋𝙊𝙉𝙎𝙀** ⚡

📡 **Ping:** `{ping_speed} ms`
🧠 **CPU:** `{cpu}%`
💾 **RAM:** `{ram}%`
🕒 **Uptime:** `{uptime}`
🖥 **OS:** `{uname.system} {uname.release}`
📍 **Host:** `{host}`
🧭 **Time:** `{time_now}`

⚔️ 𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝙗𝙮 𝙈𝙊𝙊𝙉-𝙐𝙎𝙀𝙍𝘽𝙊𝙏 🌙
"""
    await temp.edit(output)
