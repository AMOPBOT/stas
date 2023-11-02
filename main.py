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

async def get_server_status():
    cpu_percent_per_core = psutil.cpu_percent(interval=1, percpu=True)
    total_cpu_percent = sum(cpu_percent_per_core)  # Calculate the total CPU usage
    total_cpu_cores = psutil.cpu_count(logical=False)  # Get the total number of physical CPU cores
    ram = psutil.virtual_memory()
    total_ram = ram.total  # Total RAM size in bytes
    ram_percent = ram.percent
    disk = psutil.disk_usage('/')
    total_rom = disk.total  # Total disk (ROM) size in bytes
    disk_percent = disk.percent

    return total_cpu_percent, total_cpu_cores, ram_percent, total_ram, disk_percent, total_rom, cpu_percent_per_core

async def main_pratheek():
    async with app:
        while True:
            print("Checking...")
            xxx_pratheek = f"📊 | 𝗟𝗜𝗩𝗘 𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗨𝗦"
            for bot in BOT_LIST:
                try:
                    yyy_pratheek = await app.send_message(bot, "/start")
                    aaa = yyy_pratheek.id
                    await asyncio.sleep(10)
                    zzz_pratheek = app.get_chat_history(bot, limit=1)
                    async for ccc in zzz_pratheek:
                        bbb = ccc.id
                    if aaa == bbb:
                        xxx_pratheek += f"\n\n🤖  @{bot}\n        └ **Down** ❌"
                        for bot_admin_id in BOT_ADMIN_IDS:
                            try:
                                await app.send_message(int(bot_admin_id), f"🚨 **Beep! Beep!! @{bot} is down** ❌")
                            except Exception:
                                pass
                        await app.read_chat_history(bot)
                    else:
                        total_cpu_percent, total_cpu_cores, ram_percent, total_ram, disk_percent, total_rom, cpu_percent_per_core = await get_server_status()
                        cpu_cores_in_use = [f"Core {i + 1}: {core_percent}%" for i, core_percent in enumerate(cpu_percent_per_core)]
                        cpu_cores_text = "\n".join(cpu_cores_in_use)
                        xxx_pratheek += f"\n\n╭⎋🤖  @{bot}\n╰⊚ **Alive** ✅\n\n╭⎋ Server Status:\n╰⊚ Total CPU Usage: {total_cpu_percent}%\n╭⎋ Total CPU Cores: {total_cpu_cores}\n╰⊚ RAM Usage: {ram_percent}%\n╭⎋ Total RAM: {total_ram / (1024 ** 3):.2f} GB\n╰⊚ ROM Usage: {disk_percent}%\n╭⎋ Total ROM: {total_rom / (1024 ** 3):.2f} GB\n\n**╰⊚Currently Using CPU Cores:**\n{cpu_cores_text}"
                        await app.read_chat_history(bot)
                except FloodWait as e:
                    await asyncio.sleep(e.x)

            time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
            last_update = time.strftime(f"%d %b %Y at %I:%M %p")
            xxx_pratheek += f"\n\n✔️ Last checked on: {last_update} ({TIME_ZONE})\n\n**♻️ Refreshes every 3 minutes automatically - Powered By : **"
            await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_pratheek)
            print(f"Last checked on: {last_update}")
            await asyncio.sleep(180)  # Sleep for 3 minutes (180 seconds)

app.run(main_pratheek())
