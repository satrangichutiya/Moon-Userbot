import asyncio
from pyrogram import Client, filters

GHOST_TEXT = [
    "👻 𝙔𝙊𝙐 𝘼𝙍𝙀 𝙉𝙊𝙏 𝘼𝙇𝙊𝙉𝙀...",
    "😱 𝙄 𝙎𝙀𝙀 𝙔𝙊𝙐...",
    "🧠 𝙔𝙊𝙐𝙍 𝙈𝙄𝙉𝘿 𝙄𝙎 𝙉𝙊𝙒 𝙈𝙄𝙉𝙀...",
    "👁️ 𝙄 𝘼𝙈 𝙒𝘼𝙏𝘾𝙃𝙄𝙉𝙂 𝙔𝙊𝙐...",
    "🕯️ 𝙎𝙋𝙄𝙍𝙄𝙏 𝘾𝙊𝙉𝙏𝘼𝘾𝙏 𝙄𝙉𝙄𝙏𝙄𝘼𝙏𝙀𝘿...",
    "📳 𝘿𝙀𝙑𝙄𝘾𝙀 𝙏𝘼𝙆𝙀𝙊𝙑𝙀𝙍 𝙄𝙉 3...",
    "🔄 2...",
    "💀 1...",
    "☠️ 𝙂𝙃𝙊𝙎𝙏 𝙈𝙊𝘿𝙀 𝘼𝘾𝙏𝙄𝙑𝘼𝙏𝙀𝘿 ☠️"
]

@Client.on_message(filters.command("ghost", prefixes=[".", "!"]) & filters.me)
async def ghost_haunt(client, message):
    chat_id = message.chat.id
    await message.delete()

    for line in GHOST_TEXT:
        await client.send_message(chat_id, line)
        await asyncio.sleep(2)

    await client.send_animation(
        chat_id,
        "https://media.giphy.com/media/3ohzdYJK1wAdPWVk88/giphy.gif",
        caption="👁️ 𝙔𝙊𝙐 𝘼𝙍𝙀 𝙉𝙊𝙒 𝙃𝘼𝙐𝙉𝙏𝙀𝘿 👁️"
    )
