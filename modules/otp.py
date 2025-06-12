import random
from pyrogram import Client, filters
from .help import add_command_help

hl = "!"

@Client.on_message(filters.command("otp", prefixes=hl) & filters.me)
async def generate_otp(client, message):
    otp = "".join([str(random.randint(0, 9)) for _ in range(random.choice([4, 6]))])
    await message.reply(f"🔐 Your OTP is: `{otp}`\n⚠️ Never share this with anyone.")

add_command_help("•─╼⃝𖠁 OTP", [[f"{hl}otp", "Generate a random 4-6 digit OTP."]])
