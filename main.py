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
    cpu_percent = psutil.cpu_percent()
    ram = psutil.virtual_memory()
    total_ram = ram.total  # Total RAM size in bytes
    ram_percent = ram.percent
    disk = psutil.disk_usage('/')
    total_rom = disk.total  # Total disk (ROM) size in bytes
    disk_percent = disk.percent

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
                        xxx_pratheek += f"\n\n🤖  @{bot}\n        └ **Alive** ✅Server Status:\n\nCPU Usage: {cpu_percent}%\nRAM Usage: {ram_percent}%\nTotal RAM: {total_ram / (1024 ** 3):.2f} GB\nROM Usage: {disk_percent}%\nTotal ROM: {total_rom / (1024 ** 3):.2f} GB\n"
                        await app.read_chat_history(bot)
                except FloodWait as e:
                    await asyncio.sleep(e.x)

            server_status_text = await get_server_status()  # Get server status again

            time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
            last_update = time.strftime(f"%d %b %Y at %I:%M %p")
            xxx_pratheek += f"\n\n✔️ Last checked on: {last_update} ({TIME_ZONE})\n\n**♻️ Refreshes every 3 minutes automatically - Powered By : **{server_status_text}"
            await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_pratheek)
            print(f"Last checked on: {last_update}")
            await asyncio.sleep(180)  # Sleep for 3 minutes (180 seconds)

app.run(main_pratheek())
