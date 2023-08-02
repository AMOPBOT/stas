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
            TEXT = "✨ **𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓣𝓸 𝓣𝓱𝓮 𝓢𝓽𝓪𝓻 𝓫𝓮𝓻𝓻𝔂 𝓷𝓮𝓽𝔀𝓸𝓻𝓴 𝓢𝓽𝓪𝓽𝓾𝓼 𝓒𝓱𝓪𝓷𝓷𝓮𝓵**\n\n❄ 𝓗𝓮𝓻𝓮 𝓘𝓼 𝓣𝓱𝓮 𝓛𝓲𝓼𝓽 𝓞𝓯 𝓣𝓱𝓮 𝓑𝓸𝓽'𝓼 𝓦𝓱𝓲𝓬𝓱 𝓦𝓮 𝓞𝔀𝓷 𝓐𝓷𝓭 𝓣𝓱𝓮𝓲𝓻 𝓢𝓽𝓪𝓽𝓾𝓼 (𝓞𝓷𝓵𝓲𝓷𝓮 ✅ 𝓐𝓷𝓭 𝓞𝓯𝓯𝓵𝓲𝓷𝓮 ❌ ), 𝓣𝓱𝓲𝓼 𝓜𝓮𝓼𝓼𝓪𝓰𝓮 𝓦𝓮𝓵𝓵 𝓚𝓮𝓮𝓹 𝓤𝓹𝓭𝓪𝓽𝓲𝓷𝓰 𝓞𝓷 **𝓔𝓿𝓮𝓻𝔂 5 𝓜𝓲𝓷𝓾𝓽𝓮𝓼.**"
            for bots in BOT_LIST:
                ok = await app.get_users(f"@{bots}")
                try:
                    await app.send_message(bots, "/start")
                    await asyncio.sleep(2)
                    messages = app.get_chat_history(bots, limit=1)
                    async for x in messages:
                        msg = x.text
                    if msg == "/start":
                        TEXT += f"\n\n**╭⎋ [{ok.first_name}](tg://openmessage?user_id={ok.id})** \n**╰⊚ 𝓢𝓽𝓪𝓽𝓾𝓼: 𝓞𝓯𝓯𝓵𝓲𝓷𝓮 ❌**"
                        await app.send_message(LOG_ID, f"sultan 𝓢𝓲𝓻 **[{ok.first_name}](tg://openmessage?user_id={ok.id}) 𝓞𝓯𝓯 𝓗𝓮..**")
                        await app.read_chat_history(bots)
                    else:
                        TEXT += f"\n\n**╭⎋ [{ok.first_name}](tg://openmessage?user_id={ok.id})**\n**╰⊚** 𝓢𝓽𝓪𝓽𝓾𝓼: 𝓞𝓷𝓵𝓲𝓷𝓮 ✅"
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
