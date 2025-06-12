from pyrogram import Client, filters

@Client.on_message(filters.command("crash", "!") & filters.me)
async def fake_crash(client, message):
    msg = await message.reply("⚠️ SYSTEM FAILURE\n███▓▒░ Loading Crash...")
    await asyncio.sleep(2)
    await msg.edit("💀 Fatal Error: `0xDEADFACE`\n🧠 Kernel Dumping...\n💾 RAM Corrupted")
    await asyncio.sleep(2)
    await msg.edit("☠️ **Moon-Userbot has crashed.**\nGoodbye world.")
