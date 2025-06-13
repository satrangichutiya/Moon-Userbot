import random
from pyrogram import Client, filters
from pyrogram.types import Message

# 200+ Shayari List (You can add more shayaris here)
shayris = [
    "सपने उस वक्त पूरे होते हैं, जब हमारी आँखों में नींद नहीं होती...",
    "जिसे हम भूलना चाहते हैं, वह हमें कभी नहीं भूलता...",
    "तुम्हें देख कर तो बस एक ख्वाब सा लगता है...",
    "दिल में जगह बहुत है, पर तुम ही सबसे खास हो...",
    "सपने भी एक दिन सच होंगे, पर उसकी चाहत तुमसे ज्यादा नहीं होगी...",
    "वो दिल ही क्या, जिसमें तुझे चाहने का ख्वाब न हो...",
    "हमारी मोहब्बत के सिवा, कुछ भी नहीं मिलता...",
    "तुमसे जुदा होकर भी हर वक्त तुम्हारी यादों में खोते रहते हैं हम...",
    "तुम हमारी दुनिया हो, हमारी जिंदगी हो, हमारे ख्वाब हो...",
    "कभी कभी सोचता हूँ, तेरे बिना जीने की कोशिश करूँ, फिर तेरा ख्याल आता है और जीने का मन करता है...",
    # Add more shayari...
]

# Initialize bot with your API credentials
app = Client("shayri_bot")

# Dictionary to store the users for shayri
shayri_users = {}

# Function to handle shayari auto-reply
@app.on_message(filters.private)
async def reply_shayari(client, message: Message):
    user_id = message.from_user.id
    if user_id in shayri_users:
        # Send a random shayari to the user
        shayari = random.choice(shayris)
        await message.reply(shayari)

# Command to add users for shayari
@app.on_message(filters.command('shayri'))
async def add_shayri_user(client, message: Message):
    user_id = message.reply_to_message.from_user.id if message.reply_to_message else message.from_user.id
    if user_id not in shayri_users:
        shayri_users[user_id] = True
        await message.reply(f"Shayari updates are now enabled for user {user_id}.")
    else:
        await message.reply(f"User {user_id} is already receiving shayari.")

# Command to remove users from shayari list
@app.on_message(filters.command('del shayri'))
async def remove_shayri_user(client, message: Message):
    user_id = message.reply_to_message.from_user.id if message.reply_to_message else message.from_user.id
    if user_id in shayri_users:
        del shayri_users[user_id]
        await message.reply(f"Shayari updates are now removed for user {user_id}.")
    else:
        await message.reply(f"User {user_id} was not found in the shayari list.")

# Run the bot
app.run()
