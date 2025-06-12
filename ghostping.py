from pyrogram import Client, filters

@Client.on_message(filters.command("ghostping", "!") & filters.me)
async def ghost_ping(client, message):
    if not message.reply_to_message:
        return await message.reply("Reply to a message to ghost ping.")
    await message.reply_to_message.reply("👻", quote=True)
    await asyncio.sleep(0.5)
    await client.delete_messages(message.chat.id, message.reply_to_message.id + 1)
