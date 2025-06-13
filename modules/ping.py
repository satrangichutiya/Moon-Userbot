import random
import time
from pyrogram import Client, filters
from pyrogram.types import Message

# Stylish emojis and terminal themes
PONG_EMOJIS = ["⚡", "🚀", "💥", "💫", "🔥", "🌩️", "🔋", "💻", "🧠", "🛰️"]
STYLES = [
    "`Connecting to Quantum Core...`",
    "`Loading Pulse Matrix...`",
    "`Calculating Time Distortion...`",
    "`Routing Ping through wormhole...`",
]

@Client.on_message(filters.command("ping", prefixes=["!", "/", "."]) & filters.me)
async def ultra_ping(client: Client, message: Message):
    start = time.time()

    # 1st message: boot animation
    anim = await message.reply(random.choice(STYLES))
    await anim.edit("`Initiating connection...`")
    await asyncio.sleep(0.5)
    await anim.edit("`Engaging ping matrix...`")
    await asyncio.sleep(0.5)

    # 2nd message: final ping result
    end = time.time()
    ping_speed = round((end - start) * 1000, 2)

    emoji = random.choice(PONG_EMOJIS)
    await anim.edit(
        f"**{emoji} Pᴏɴɢ!**\n\n"
        f"📡 Sᴘᴇᴇᴅ: `{ping_speed} ms`\n"
        f"⚙️ Sᴛᴀᴛᴜs: `System Stable`\n"
        f"🔗 Powered by: `Moon-X`"
    )
