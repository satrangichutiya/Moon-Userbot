@Client.on_message(filters.command("lag", "!") & filters.me)
async def lag(_, msg):
    await msg.edit("⚙️ CPU Overload Detected! System resources draining...")
    await asyncio.sleep(3)
    await msg.edit("💣 Bot crashed due to high load... Rebooting...")
    await asyncio.sleep(2)
    await msg.edit("✅ Booted into Safe Mode 🔧")
