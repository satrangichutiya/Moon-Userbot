from pyrogram import Client, filters
from pyrogram.types import Message
from config import CMD_HNDLR

# Dictionary to store help information
HELP_COMMANDS = {}

def add_command_help(module_name, commands):
    """
    Registers commands for help system
    Format:
    add_command_help("module", {"command": "description", "command2": "desc2"})
    """
    HELP_COMMANDS[module_name] = commands

@Client.on_message(filters.command("help", prefixes=CMD_HNDLR) & filters.me)
async def help_handler(client, message: Message):
    if len(message.command) == 1:
        # General Help Overview
        help_text = "**🌐 UserBot Help Menu**\n\n"
        help_text += "Use `.help modulename` to get command info for a specific module.\n\n"
        help_text += "**🧩 Available Modules:**\n"

        for module in sorted(HELP_COMMANDS):
            help_text += f"🔹 `{module}`\n"

        await message.edit(help_text)
    else:
        # Specific Module Help
        module = message.text.split(None, 1)[1].strip().lower()

        if module in HELP_COMMANDS:
            commands = HELP_COMMANDS[module]
            help_text = f"**📚 Help for `{module}`**\n\n"
            for cmd, desc in commands.items():
                help_text += f"➤ `{CMD_HNDLR}{cmd}` — {desc}\n"
            await message.edit(help_text)
        else:
            await message.edit("🚫 Unknown module name. Use `.help` to see all available modules.")
