from pyrogram import filters
from main import app  # Make sure 'app' is defined in main.py and correctly imported
import random

# List of Shayaris
shayari_list = [
    "🌹 दिल तोड़ने वाले भी अजब हुनर रखते हैं, पहले महोब्बत का वादा फिर नफरत करते हैं।",
    "😂 तुम इतने प्यारे हो कि तुम्हे देख के शरमाएं आईने!",
    "😜 दिमाग तो हमारा भी खराब है पर कोई मौके देता नहीं!",
    "🤣 तेरी स्माइल के बिना तो मेरी लाइफ भी नीरस लगती है!",
    "💔 किसी का दिल तोड़ कर माफ़ी मांगना आसान है, मगर टूटा हुआ दिल जुड़ता नहीं।",
    "🔥 मत समझो कमजोर हमें, हम वो शेर हैं जो अकेले जंगल हिला दें!",
    "😂 पढ़ाई छोड़ दी मैंने, जबसे तूने कहा 'तू पढ़-लिख के क्या करेगा?'",
    "😈 चेहरे पर न दिखे लेकिन, हम अंदर से पूरे खतरनाक हैं!",
    "💘 तू सामने हो और Shayari ना निकले, ऐसा तो कभी हो ही नहीं सकता!",
    "🥺 अकेले बैठ कर सोचते हैं कि क्या कमी रह गई थी मुझमें!"
    # ... 100+ more shayaris can be added here
]

# Dictionary to store users who will get auto-replies
auto_reply_users = set()

@app.on_message(filters.command("shayri") & filters.me)
async def add_user_to_shayari(client, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        auto_reply_users.add(user_id)
        await message.reply(f"✅ अब से <b>{message.reply_to_message.from_user.first_name}</b> को Shayari में डुबोया जाएगा 🥀")
    else:
        await message.reply("⚠️ किसी के reply में use करो ताकि Shayari शुरू की जा सके।")

@app.on_message(filters.command("delshayri") & filters.me)
async def remove_user_from_shayari(client, message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        auto_reply_users.discard(user_id)
        await message.reply(f"❌ अब <b>{message.reply_to_message.from_user.first_name}</b> को Shayari नहीं दी जाएगी।")
    else:
        await message.reply("⚠️ किसी के reply में use करो ताकि Shayari हटाई जा सके।")

@app.on_message(filters.text & ~filters.me)
async def auto_shayari_reply(client, message):
    user_id = message.from_user.id
    if user_id in auto_reply_users:
        chosen = random.choice(shayari_list)
        try:
            await message.reply(chosen)
        except Exception as e:
            print(f"Reply failed: {e}")


