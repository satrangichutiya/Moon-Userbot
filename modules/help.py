from pyrogram import Client, filters
from pyrogram.types import Message

# Store all command help
HELP_COMMANDS = {}

# Add command help for each module
def add_command_help(module_name, command_info):
    HELP_COMMANDS[module_name] = command_info

@Client.on_message(filters.command("help", prefixes=["!", ".", "/", "#", "?"]) & filters.me)
async def help_command(client, message: Message):
    args = message.text.split(" ", 1)
    
    if len(args) == 1:
        # Show all modules list
        help_text = "**📚 Available Modules:**\n\n"
        for mod in sorted(HELP_COMMANDS.keys()):
            help_text += f"🔹 `{mod}`\n"
        help_text += "\nUse `!help <module>` to get help for a specific module."
        await message.reply_text(help_text)
    
    else:
        mod_name = args[1].strip()
        if mod_name in HELP_COMMANDS:
            help_text = f"**🧠 Help for `{mod_name}` module:**\n\n"
            help_text += HELP_COMMANDS[mod_name]
            await message.reply_text(help_text)
        else:
            await message.reply_text("❌ Module not found. Try `!help` to see available modules.")
