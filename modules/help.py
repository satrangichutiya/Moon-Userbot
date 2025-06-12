from pyrogram import Client, filters
from pyrogram.types import Message

# Prefix for commands (change if needed)
CMD_PREFIX = "!"

# Dictionary to hold help commands
HELP_COMMANDS = {}

# Function to register module help
def add_command_help(module_name: str, commands: list):
    """
    module_name: Name of the module (str)
    commands: List of tuples -> [(command, description), ...]
    """
    HELP_COMMANDS[module_name] = commands

# Help command to show all help text
@Client.on_message(filters.command("help", prefixes=CMD_PREFIX) & filters.me)
async def help_command_handler(client: Client, message: Message):
    text = "**🌙 Moon UserBot Help Menu**\n\n"
    for mod_name, cmds in HELP_COMMANDS.items():
        text += f"🔹 **{mod_name.capitalize()}**\n"
        for cmd in cmds:
            text += f"`{CMD_PREFIX}{cmd[0]}` — {cmd[1]}\n"
        text += "\n"
    await message.reply(text)
