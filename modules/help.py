
# modules/help.py

HELP_COMMANDS = {}

def add_command_help(module_name: str, help_text: str):
    """
    Registers a help command for a given module.
    Use this in your module like:
    add_command_help("ModuleName", "Help text here")
    """
    module_name = module_name.strip().title()
    HELP_COMMANDS[module_name] = help_text.strip()

def get_all_modules():
    return sorted(HELP_COMMANDS)

def get_help(module_name: str):
    return HELP_COMMANDS.get(module_name.strip().title())
