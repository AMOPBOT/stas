<h1 align="center">sᴛᴀᴛᴜs ᴄʜᴇᴄᴋᴇʀ</h1>

<p align="center"><a href="https://t.me/AM_YTBOTT"><img src="https://telegra.ph/file/46802a20ecd9495f0ddc6.jpg" width="300"></a></p>

<p align="center"><b>ᴀᴛʟᴇᴀsᴛ ɢɪᴠᴇ ᴀ sᴛᴀʀ ᴀɴᴅ ғᴏʀᴋ ᴛʜᴇ ʀᴇᴘᴏ</b></p>

## 🗒️ ɴᴇᴄᴇssᴀʀʏ ᴠᴀʀs

1. `API_ID` : Telegram API_ID, get it from my.telegram.org/apps
2. `API_HASH` : Telegram API_ID, get it from my.telegram.org/apps
3. `STRING_SESSION` : A valid Pyrogram session string, get it from [@Sessoin_String_gen_BOT](https://t.me/Sessoin_String_gen_BOT)
4. `BOT_LIST` : Your bot username list without '@' (Example: Sophia_x_MusicBot Anierobot_bot)
5. `CHANNEL_ID` : Your channel's Telegram id (Example: -1001887171460)
6. `MESSAGE_ID` : Telegram id of message from your channel or group (Example: 45)
7. `LOG_ID` : Log id (Example: -1001565615923)
8. `TIME_ZONE`: Your time zone (Example: Asia/Kolkata)

<b>ɴᴏᴡ ᴄᴏᴘʏ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ᴄᴏᴅᴇ ᴀɴᴅ ᴀᴅᴅ ɪɴᴛᴏ ʏᴏᴜʀ ʀᴇᴘᴏsɪᴛᴏʀʏ ɪɴ ᴘʟᴜɢɪɴs ᴅɪʀᴇᴄᴛᴏʀʏ :</b>

```
import psutil
import time
from pyrogram import Client
from pyrogram import filters 
from pyrogram.types import Message

start_time = time.time()

def time_formatter(milliseconds):
    minutes, seconds = divmod(int(milliseconds / 1000), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    tmp = (((str(weeks) + "ᴡ:") if weeks else "") +
           ((str(days) + "ᴅ:") if days else "") +
           ((str(hours) + "ʜ:") if hours else "") +
           ((str(minutes) + "ᴍ:") if minutes else "") +
           ((str(seconds) + "s") if seconds else ""))
    if not tmp:
        return "0s"
    if tmp.endswith(":"):
        return tmp[:-1]
    return tmp


@Client.on_message(filters.command("bot"))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    TEXT = f"**ᴜᴘᴛɪᴍᴇ** : {uptime} | **ᴄᴘᴜ** : {cpu}%"
    await message.reply(TEXT)
```

━━━━━━━━━━━━━━━━━━━━

<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ ʜᴇʀᴏᴋᴜ 」─
</h3>

<p align="center"><a href="https://dashboard.heroku.com/new?template=https://github.com/AbhiMod/stas"> <img src="https://img.shields.io/badge/Deploy%20On%20Heroku-black?style=for-the-badge&logo=heroku" width="220" height="38.45"/></a></p>

<h3 align="center">
    ─「 ᴅᴇᴩʟᴏʏ ᴏɴ vps 」─
</h3>

1. Update and upgrade by :
```
sudo apt-get update && sudo apt-get upgrade -y
```
2. Clone the repository by :
```
git clone https://github.com/AbhiMod/stas && cd stas
```
3. Install requirements by :
```
pip3 install -U -r requirements.txt
```
4. Create .env using sample.env by
```
cp sample.env .env
```
5. Now open the .env file using ```vi .env```
6. Edit the vars, by pressing ```I```  on the keyboard
7. After editing save the file using ```ctrl + c``` then ```:wq```
8. Finally run the script using python3 :
```
python3 main.py
```
━━━━━━━━━━━━━━━━━━━━

<h3 align="center">
    ─「 sᴜᴩᴩᴏʀᴛ 」─
</h3>

<p align="center">
<a href="https://telegram.me/AM_YTSUPPORT"><img src="https://img.shields.io/badge/-Support%20Group-blue.svg?style=for-the-badge&logo=Telegram"></a>
</p>

<p align="center">
<a href="https://telegram.me/AMBOTYT"><img src="https://img.shields.io/badge/-Support%20Channel-blue.svg?style=for-the-badge&logo=Telegram"></a>
</p>
