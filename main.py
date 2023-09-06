import os
import asyncio
import datetime
import pytz
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
            TEXT = "✨ 𝗪𝗲𝗹𝗹𝗖𝗼𝗺𝗲 𝗧𝗼 𝗧𝗵𝗲 𝗦𝘁𝗮𝗿 𝗕𝗲𝗿𝗿𝘆 𝗡𝗲𝘁𝗪𝗼𝗿𝗸.**\n\n\n❄ Here Is The List Of The Bots.\n❄ Which We Own And Their Status\n\n𝓞𝓷𝓵𝓲𝓷𝓮 ✅\n 𝓞𝓯𝓯𝓵𝓲𝓷𝓮 ❌ \n\nThis Messege Well Keep Updating On Every 5 Minutes."
            for bots in BOT_LIST:
                ok = await app.get_users(f"@{bots}")
                try:
                    await app.send_message(bots, "/start")
                    await asyncio.sleep(2)
                    messages = app.get_chat_history(bots, limit=1)
                    async for x in messages:
                        msg = x.text
                    if msg == "/start":
                        TEXT += f"\n\n**╭⎋ [{ok.first_name}](tg://openmessage?user_id={ok.id})** \n**╰⊚ 𝓢𝓽𝓪𝓽𝓾𝓼:  ❌**"
                        await app.send_message(LOG_ID, f"𝓢𝓲𝓻 **[{ok.first_name}](tg://openmessage?user_id={ok.id}) 𝓞𝓯𝓯 𝓗𝓮..**")
                        await app.read_chat_history(bots)
                    else:
                        TEXT += f"\n\n**╭⎋ [{ok.first_name}](tg://openmessage?user_id={ok.id})**\n**╰⊚** 𝓢𝓽𝓪𝓽𝓾𝓼:  ✅"
                        await app.read_chat_history(bots)
                except FloodWait as e:
                    await asyncio.sleep(e.value)
            time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
            date = time.strftime("%d %b %Y")
            time = time.strftime("%I:%M %p")
            TEXT += f"\n\n**ʟᴀꜱᴛ ᴄʜᴇᴄᴋ ᴏɴ :**\n**ᴅᴀᴛᴇ :** {date}\n**ᴛɪᴍᴇ :** {time}\n\n"
            await app.edit_message_text(int(CHANNEL_ID), (MESSAGE_ID), TEXT)
            await asyncio.sleep(300)

app.run(main())          
