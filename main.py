from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os
import psutil

app = Client(
    name="botstatus_pratheek",
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    session_string=os.environ["SESSION_STRING"]
)

TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]

# Define a dictionary to store the uptime of each bot
bot_uptimes = {}

async def get_server_status():
    cpu_percent_per_core = psutil.cpu_percent(interval=1, percpu=True)
    total_cpu_percent = sum(cpu_percent_per_core)  # Calculate the total CPU usage
    total_cpu_cores = psutil.cpu_count(logical=False)  # Get the total number of physical CPU cores
    ram = psutil.virtual_memory()
    total_ram = ram.total  # Total RAM size in bytes
    used_ram = ram.used
    ram_percent = ram.percent
    disk = psutil.disk_usage('/')
    total_rom = disk.total  # Total disk (ROM) size in bytes
    used_rom = disk.used
    disk_percent = disk.percent

    return total_cpu_percent, total_cpu_cores, total_ram, total_rom, used_ram, used_rom, ram_percent, disk_percent, cpu_percent_per_core

async def main_pratheek():
    async with app:
        while True:
            print("Checking...")
            total_cpu_percent, total_cpu_cores, total_ram, total_rom, used_ram, used_rom, ram_percent, disk_percent, cpu_percent_per_core = await get_server_status()
            xxx_pratheek = f"📊 | 𝗟𝗜𝗩𝗘 𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗨𝗦\n"
            for bot in BOT_LIST:
                try:
                    yyy_pratheek = await app.send_message(bot, "/start")
                    aaa = yyy_pratheek.id
                    await asyncio.sleep(10)
                    zzz_pratheek = app.get_chat_history(bot, limit=1)
                    async for ccc in zzz_pratheek:
                        bbb = ccc.id
                    if aaa == bbb:
                        # Bot is down
                        if bot in bot_uptimes:
                            del bot_uptimes[bot]  # Remove bot from uptime dictionary
                        xxx_pratheek += f"\n\n🤖  @{bot}\n        └ **Down** ❌"
                        for bot_admin_id in BOT_ADMIN_IDS:
                            try:
                                await app.send_message(int(bot_admin_id), f"🚨 **Beep! Beep!! @{bot} is down** ❌")
                            except Exception:
                                pass
                        await app.read_chat_history(bot)
                    else:
                        # Bot is up
                        if bot not in bot_uptimes:
                            bot_uptimes[bot] = datetime.datetime.now()
                        uptime = datetime.datetime.now() - bot_uptimes[bot]
                        xxx_pratheek += f"\n\n🤖  @{bot}\n        └ **Alive** ✅\n"
                        xxx_pratheek += f"\n        └ **Uptime**: {str(uptime).split('.')[0]}\n"
                        xxx_pratheek += f"╭⎋ Total CPU Usage: {total_cpu_percent}%\n"
                        xxx_pratheek += f"╰⊚ Total CPU Cores: {total_cpu_cores}\n"
                        xxx_pratheek += f"╭⎋ Total RAM: {total_ram / (1024 ** 3):.2f} GB\n"
                        xxx_pratheek += f"╰⊚ Used RAM: {used_ram / (1024 ** 3):.2f} GB\n"
                        xxx_pratheek += f"╭⎋ RAM Usage: {ram_percent}%\n"
                        xxx_pratheek += f"╰⊚ Total ROM: {total_rom / (1024 ** 3):.2f} GB\n"
                        xxx_pratheek += f"╭⎋ Used ROM: {used_rom / (1024 ** 3):.2f} GB\n"
                        xxx_pratheek += f"╰⊚ ROM Usage: {disk_percent}%\n"
                        # Your existing code to display server status

                        await app.read_chat_history(bot)
                except FloodWait as e:
                    await asyncio.sleep(e.x)

            time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
            last_update = time.strftime(f"%d %b %Y at %I:%M %p")
            xxx_pratheek += f"\n\n✔️ Last checked on: {last_update} ({TIME_ZONE})\n"
            xxx_pratheek += "**♻️ Refreshes every 3min automatically - Powered By...**"
            await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_pratheek)
            print(f"Last checked on: {last_update}")
            await asyncio.sleep(180)

app.run(main_pratheek())
