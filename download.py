from telethon.sync import TelegramClient
from telethon.errors import FloodWaitError
import os
import time

# =========================
# TELEGRAM API
# =========================

from config import API_ID, API_HASH, CHANNEL

api_id = API_ID
api_hash = API_HASH
channel = CHANNEL

# =========================
# SETTINGS
# =========================

BASE_DIR = 'downloads'

PROGRESS_FILE = 'last_id.txt'

os.makedirs(BASE_DIR, exist_ok=True)

# =========================
# LOAD LAST ID
# =========================

def load_last_id():

    if os.path.exists(PROGRESS_FILE):

        with open(PROGRESS_FILE, 'r') as f:

            content = f.read().strip()

            if content:

                return int(content)

    return 0

# =========================
# SAVE LAST ID
# =========================

def save_last_id(message_id):

    with open(PROGRESS_FILE, 'w') as f:

        f.write(str(message_id))

# =========================
# GET FOLDER
# =========================

def get_folder(message):

    year = message.date.strftime('%Y')
    month = message.date.strftime('%m')

    if message.photo:

        media_type = 'photos'

    elif message.video:

        media_type = 'videos'

    else:

        media_type = 'documents'

    folder = os.path.join(
        BASE_DIR,
        media_type,
        year,
        month
    )

    os.makedirs(folder, exist_ok=True)

    return folder

# =========================
# MAIN LOOP
# =========================

while True:

    try:

        last_downloaded_id = load_last_id()

        print(f'\nResuming from message ID: {last_downloaded_id}')

        client = TelegramClient(
            'session',
            api_id,
            api_hash,
            connection_retries=999999,
            retry_delay=5,
            auto_reconnect=True
        )

        with client:

            for message in client.iter_messages(
                channel,
                reverse=True,
                min_id=last_downloaded_id
            ):

                if not message.media:
                    continue

                success = False

                while not success:

                    try:

                        print(f'Processing message {message.id}')

                        folder = get_folder(message)

                        path = client.download_media(
                            message,
                            file=folder
                        )

                        print(f'Finished: {path}')

                        save_last_id(message.id)

                        success = True

                    except FloodWaitError as e:

                        print(f'Flood wait {e.seconds}s')

                        time.sleep(e.seconds)

                    except Exception as e:

                        print(f'Download error: {e}')

                        print('Retrying file in 10 seconds...')

                        time.sleep(10)

    except KeyboardInterrupt:

        print('\nStopped manually.')

        break

    except Exception as e:

        print(f'\nConnection/server error: {e}')

        print('Reconnecting in 15 seconds...')

        time.sleep(15)