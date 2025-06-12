from pyrogram import Client, filters
import asyncio

@Client.on_message(filters.command("!possess"))
async def demon_voice(_, message):
    await message.edit("☠️ Summoning demon...")
    await asyncio.sleep(1)
    demon_lines = [
        "𝐘𝐎𝐔 𝐂𝐀𝐍'𝐓 𝐄𝐒𝐂𝐀𝐏𝐄...",
        "𝐈 𝐖𝐀𝐒 𝐖𝐀𝐓𝐂𝐇𝐈𝐍𝐆 𝐘𝐎𝐔.",
        "𝐘𝐎𝐔𝐑 𝐒𝐎𝐔𝐋 𝐈𝐒 𝐌𝐈𝐍𝐄 🩸",
        "𝐃𝐄𝐕𝐈𝐋 𝐇𝐀𝐒 𝐄𝐍𝐓𝐄𝐑𝐄𝐃..."
    ]
    for line in demon_lines:
        await message.edit(line)
        await asyncio.sleep(1)
