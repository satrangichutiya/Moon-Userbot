# modules/help.py

from pyrogram import Client, filters
from pyrogram.types import Message

# Global help dictionary
HELP_COMMANDS = {}

# Add help from modules
def add_command_help(module_name, help_text):
    HELP_COMMANDS[module_name] = help_text.strip()

# Format help list in chunks (to avoid Telegram 4096 char limit)
def split_help_chunks():
    help_list = sorted(HELP_COMMANDS.keys(), key=str.lower)
    chunks = []
    chunk = "**📚 Available Modules:**\n\n"
    for mod in help_list:
        line = f"🔹 `•─╼⃝𖠁 {mod}`\n"
        if len(chunk + line) > 4000:
            chunks.append(chunk)
            chunk = "**📚 Continued Modules:**\n\n"
        chunk += line
    if chunk:
        chunks.append(chunk)
    return chunks

@Client.on_message(filters.command("help", prefixes=["!", ".", "/"]) & filters.me)
async def help_command(client, message: Message):
    args = message.text.split(maxsplit=1)
    if len(args) == 1:
        for chunk in split_help_chunks():
            await message.reply_text(chunk)
    else:
        module = args[1].strip()
        if module in HELP_COMMANDS:
            await message.reply_text(
                f"**🧠 Help for `{module}` module:**\n\n{HELP_COMMANDS[module]}"
            )
        else:
            await message.reply_text("❌ Unknown module. Try `!help` to see the list.")
