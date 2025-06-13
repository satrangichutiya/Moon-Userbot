from pyrogram import Client, filters
import random

# Targeted users dict
target_users = set()

# 200+ Shayaris (funny, sad, love etc.)
shayari_list = [
    "तेरे बिना अधूरी सी लगती है ज़िन्दगी 😢",
    "मोहब्बत करने वालों का नसीब बुरा होता है 💔",
    "तेरे जैसे कमीने लोग रोज़ दिल तोड़ते हैं 😂",
    "तेरे बिना सुबह अधूरी है, और रातें भी बोर 😒",
    "तू सामने हो और Shayari ना निकले? नामुमकिन है 🤯",
    "मुझसे मत उलझ, मैं userbot चलाता हूँ 🤖",
    "तू reply करता रह, मैं auto-reply करता रहूँगा 😉",
    "तेरे जैसा नकली बंदा मिलना मुश्किल नहीं, नामुमकिन है 😂",
    "तेरी बातें WhatsApp जैसी fake लगती हैं 🤳",
    "दिल से निकली है तेरे लिए गाली नहीं, Shayari है भाई 🤣",
    # Add 190+ more below... (cut short here for brevity)
]

# Add user to shayari reply list
@Client.on_message(filters.command("shayri", prefixes="!") & filters.reply)
async def add_shayari_user(_, message):
    user_id = message.reply_to_message.from_user.id
    target_users.add(user_id)
    await message.reply_text("✅ अब इस बंदे पर Shayari bomb चालू हो गया!")

# Remove user from shayari reply list
@Client.on_message(filters.command("del", prefixes=".") & filters.regex("shayri") & filters.reply)
async def remove_shayari_user(_, message):
    user_id = message.reply_to_message.from_user.id
    target_users.discard(user_id)
    await message.reply_text("❌ Shayari बंद कर दी गई इस बंदे के लिए.")

# Auto-reply if message from target user
@Client.on_message(filters.text & filters.private | filters.group | filters.channel)
async def auto_reply_shayari(_, message):
    user_id = message.from_user.id if message.from_user else None
    if user_id in target_users:
        shayari = random.choice(shayari_list)
        await message.reply(f"@{message.from_user.username or message.from_user.first_name} {shayari}")
