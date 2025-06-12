import random
from pyrogram import Client, filters
from config import SUDO_USERS
from .help import add_command_help

hl = "!"

@Client.on_message(
    filters.command("bc", prefixes=hl) & (filters.me | filters.user(SUDO_USERS))
)
async def bsdke(client, message):
    bc_pics = [
        "https://graph.org/file/ac866e1d75bdfdb1e2edf.jpg",
        "https://graph.org/file/347eedd9b939c57776f97.jpg",
        "https://graph.org/file/2e51c1cb2ebfaf5b599e0.jpg",
        "https://graph.org/file/a7584d179f380b5627485.jpg",
        "https://graph.org/file/54a3e66e3c30e340cb1fa.jpg",
        "https://graph.org/file/76575287d9fa600d5effb.jpg",
        "https://graph.org/file/a27baae47423663239076.jpg",
        "https://graph.org/file/675a9904801c5bd43bc60.jpg",
    ]
    selected_pic = random.choice(bc_pics)
    await message.reply_photo(selected_pic)

add_command_help(
    "•─╼⃝𖠁 Bᴄ",
    [
        [f"{hl}bc", "Send a random BC pic 😈"],
    ],
)
