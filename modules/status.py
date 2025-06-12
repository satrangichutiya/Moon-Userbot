from pyrogram import Client, filters
from .help import add_command_help
import random

hl = "!"

@Client.on_message(filters.command("status", prefixes=hl) & filters.me)
async def fake_status(client, message):
    cpu = random.randint(10, 99)
    ram = random.randint(20, 99)
    ping = round(random.uniform(5, 100), 2)
    await message.reply(f"""
📊 **System Status**

🖥️ CPU Usage: `{cpu}%`
🧠 RAM Usage: `{ram}%`
📡 Ping: `{ping}ms`
⚡ Status: `All Systems Operational`
""")

add_command_help(
    "•─╼⃝𖠁 Sʏsᴛᴇᴍ",
    [[f"{hl}status", "Show fake server stats for fun/dev trolling."]]
)
