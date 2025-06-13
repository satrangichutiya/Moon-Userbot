from pyrogram import Client, filters
import asyncio
from random import choice, randint
from datetime import datetime

# Command: !rebootos

@Client.on_message(filters.command("rebootos", prefixes="!") & filters.me)
async def fake_reboot(client, message):
    reboot_messages = [
        "[INFO] Saving unsaved memory chunks...",
        "[INFO] Encrypting current session...",
        "[INFO] Killing idle processes...",
        "[WARN] Session tampering detected!",
        "[INFO] Wiping vulnerable cache sectors...",
        "[INFO] Initiating soft reboot...",
        "[CRITICAL] Error in core daemon handler...",
        "[INFO] Rolling back corrupted modules...",
        "[INFO] Restoring backup...",
        "[INFO] Reinitializing sockets...",
        "[INFO] Authenticating root signature...",
        "[FAIL] Key mismatch at line 0x4F3...",
        "[INFO] Injecting anti-malware sequences...",
        "[SUCCESS] Safe mode engaged...",
        "[BOOT] TelegramOS Kernel v5.3.1",
        "[BOOT] Mounting /core, /lib, /usr/bin...",
        "[BOOT] Starting fail2ban...",
        "[INFO] Firewall status: LOCKED",
        "[SECURITY] IP Address blacklisted: 185.0.91.13",
        "[SECURITY] Logging out all other sessions...",
        "[SECURITY] Performing session lockdown...",
        "[AI] Neural network backup active...",
        "[AI] Uploading last consciousness snapshot...",
        "[EMERGENCY] Launch code abort: SUCCESS",
        "[FINALIZE] System fully reinitialized."
    ]

    await message.edit_text("🔄 **System Reboot Initiated**...\n", disable_web_page_preview=True)
    await asyncio.sleep(2)

    reboot_log = ""
    for log in reboot_messages:
        timestamp = datetime.utcnow().strftime("[%H:%M:%S]")
        reboot_log += f"{timestamp} {log}\n"
        await message.edit_text(f"```\n{reboot_log}```")
        await asyncio.sleep(0.4)

    # Final message
    status = choice([
        "**✅ Reboot Complete. System stabilized.**",
        "**⚠️ Critical modules failed. Entering failsafe mode.**",
        "**🧠 AI Consciousness Backup Loaded.**",
        "**❌ Reboot Failed. Manual override required.**"
    ])

    await asyncio.sleep(1.5)
    await message.edit_text(f"```\n{reboot_log}```\n\n{status}")
