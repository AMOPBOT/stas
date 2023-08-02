import os
import pytz
import time
import datetime

from pyrogram import Client

user_session_string = os.environ.get("user_session_string")
bots = [i.strip() for i in os.environ.get("bots").split(' ')]
update_channel = os.environ.get("update_channel")
status_message_ids = [int(i.strip()) for i in os.environ.get("status_message_id").split(' ')]
api_id = int(os.environ.get("api_id"))
api_hash = os.environ.get("api_hash")
user_client = Client(user_session_string, api_id=api_id, api_hash=api_hash)

# Constants
CHECK_INTERVAL = 15  # Seconds
WAIT_TIME_BETWEEN_BOTS = 5  # Seconds
SLEEP_INTERVAL = 3 * 60 * 60  # 3 hours in seconds

def check_bot_status(bot_username):
    try:
        print(f"[INFO] Checking @{bot_username}")
        snt = user_client.send_message(bot_username, '/start')
        time.sleep(CHECK_INTERVAL)
        msg = user_client.get_history(bot_username, 1)[0]

        if snt.message_id == msg.message_id:
            print(f"[WARNING] @{bot_username} is down")
            return False
        else:
            print(f"[INFO] All good with @{bot_username}")
            return True
    except Exception as e:
        print(f"[ERROR] Error while checking @{bot_username}: {e}")
        return False

def main():
    with user_client:
        while True:
            print("[INFO] Starting to check uptime..")
            edit_text = "💕𝓢𝓽𝓪𝓻 𝓑𝓮𝓻𝓻𝔂 𝓝𝓮𝓽𝔀𝓸𝓻𝓴 𝐁𝐨𝐭𝐬 𝓑𝓸𝓽𝓼 𝓢𝓽𝓪𝓽𝓾𝓼 \n\n__(All bots are checked automatically, if any correction report it)__\n\n\n"

            for bot in bots:
                is_bot_up = check_bot_status(bot)
                status = "✅" if is_bot_up else "❌"
                edit_text += f"𝙱𝙾𝚃 𝙽𝙰𝙼𝙴    {bot} \n𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴  @{bot}\n𝚂𝚃𝙰𝚃𝚄𝚂 {status}\n\n"
                user_client.read_history(bot)
                time.sleep(WAIT_TIME_BETWEEN_BOTS)

            time_now = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
            formatted_time = time_now.strftime("%d %B %Y %I:%M %p")
            edit_text += f"**Updated on {formatted_time} (GMT)**"

            for status_message_id in status_message_ids:
                user_client.edit_message_text(int(update_channel), status_message_id, edit_text)
                time.sleep(5)

            print(f"[INFO] Everything done! Sleeping for 3 hours...")
            time.sleep(SLEEP_INTERVAL)

if __name__ == "__main__":
   main()
