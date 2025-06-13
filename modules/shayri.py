import random
from pyrogram import filters
from pyrogram.types import Message
from config import app  # make sure app is imported from your bot's main instance

# 200+ Hindi Shayari list
shayaris = [
    "तू सामने हो और वक्त ठहर जाए, यही ख्वाहिश है मेरी।",
    "पलकों पे रखा है तुझको, मगर नजरों से दूर ना किया।",
    "हर किसी को जवाब देना ज़रूरी नहीं होता, कुछ को तो नजरअंदाज करना ही बेहतर है।",
    "तू पूछ ले सुबह से, ना यकीन हो तो शाम से, ये दिल धड़कता है बस तेरे ही नाम से।",
    "तेरी मुस्कान ही मेरी पहचान है।",
    "इतना भी प्यार किसी से ना करना कि वो तुम्हें तोड़ के चला जाए।",
    "हमारा दिल भी कितना पागल है, हर उस शख्स को चाहता है जो इसका होना नहीं चाहता।",
    "वो तेरे होने का एहसास अब भी रहता है हर साँस के साथ।",
    "ख्वाब देखना तो शुरुआत है, उन्हें पूरा करना ही ज़िंदगी है।",
    "तू पास हो या दूर, तेरी यादें साथ चलती हैं।",
    # Add more funny/hardcore ones...
]

# Shayari users set
shayari_users = set()

# Add user to shayari list
@app.on_message(filters.command("shayri") & filters.me)
async def add_shayari_user(_, message: Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        shayari_users.add(user_id)
        await message.reply(f"✅ User `{user_id}` added for Shayari auto-replies.")
    else:
        await message.reply("⚠️ Reply to a user's message to add them.")

# Remove user from shayari list
@app.on_message(filters.command("del shayri") & filters.me)
async def remove_shayari_user(_, message: Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        if user_id in shayari_users:
            shayari_users.remove(user_id)
            await message.reply(f"❌ User `{user_id}` removed from Shayari list.")
        else:
            await message.reply("⚠️ This user is not in the list.")
    else:
        await message.reply("⚠️ Reply to a user's message to remove them.")

# Auto reply with random shayari
@app.on_message(filters.private & ~filters.me)
async def auto_shayari_reply(_, message: Message):
    user_id = message.from_user.id
    if user_id in shayari_users:
        await message.reply(random.choice(shayaris))
