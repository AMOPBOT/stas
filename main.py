import os
import asyncio
import datetime
import pytz
import psutil
from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.errors import FloodWait

load_dotenv()

app = Client(
    name="krishna",
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH"),
    session_string=os.getenv("STRING_SESSION")
)

BOT_LIST = [x.strip() for x in os.getenv("BOT_LIST").split(' ')]
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))
MESSAGE_ID = int(os.getenv("MESSAGE_ID"))
TIME_ZONE = os.getenv("TIME_ZONE")
LOG_ID = int(os.getenv("LOG_ID"))

async def main():
    print("Status Checker Bot Started")
    async with app:
        while True:
            cpu_percent = psutil.cpu_percent()
            ram_percent = psutil.virtual_memory().percent
            disk_usage = psutil.disk_usage('/')
            TEXT = "⚡️𝗛𝗲𝗿𝗲 𝗜𝘀 𝗧𝗵𝗲 𝗟𝗶𝘀𝘁 𝗢𝗳 𝗧𝗵𝗲 𝗕𝗼𝘁𝘀 ⚡️.\n\nWhich We Own And Their Status\n\nOnline ✅\nOffline ❌\n\nThis Message Will Keep Updating Every 30 Minutes."
            for bots in BOT_LIST:
                ok = await app.get_users(f"@{bots}")
                try:
                    await app.send_message(bots, "/start")
                    await asyncio.sleep(2)
                    messages = app.get_chat_history(bots, limit=1)
                    async for x in messages:
                        msg = x.text
                    if msg == "/start":
                        TEXT += f"\n\n**╭⎋ [{ok.first_name}](tg://openmessage?user_id={ok.id})**\n**╰⊚ 𝓢𝓽𝓪𝓽𝓾𝓼:  ❌\n\nSystem Info:\nCPU Usage: {cpu_percent}%\nRAM Usage: {ram_percent}%\nStorage Usage: {disk_usage.percent}%\n"
                        await app.send_message(LOG_ID, f"𝓢𝓲𝓻 **[{ok.first_name}](tg://openmessage?user_id={ok.id}) 𝓞𝓯𝓯 𝓗𝓮..**")
                        await app.read_chat_history(bots)
                    else:
                        TEXT += f"\n\n**╭⎋ [{ok.first_name}](tg://openmessage?user_id={ok.id})**\n**╰⊚ 𝓢𝓽𝓪𝓽𝓾𝓼:  ✅\n\nSystem Info:\nCPU Usage: {cpu_percent}%\nRAM Usage: {ram_percent}%\nStorage Usage: {disk_usage.percent}%\n"
                        await app.read_chat_history(bots)
                except FloodWait as e:
                    await asyncio.sleep(e.value)
            time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
            date = time.strftime("%d %b %Y")
            time = time.strftime("%I:%M %p")
            TEXT += f"\n\n**Last check on:**\n**Date:** {date}\n**Time:** {time}\nNetwork status: Soon..."
            await app.edit_message_text(int(CHANNEL_ID), MESSAGE_ID, TEXT)
            await asyncio.sleep(1800)  # Sleep for 30 minutes (1800 seconds)

app.run(main())
