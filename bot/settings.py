import os

from decouple import config
from dotenv import load_dotenv

load_dotenv()

DEBUG = config('DEBUG', default=False, cast=bool)

COLOR_YELLOW = 0xFDDA46
COLOR_CYAN = 0x7AE8FF
COLOR_BLUE = 0x0068BE
COLOR_DARK_BLUE = 0x0B254D


if DEBUG:
    BOT_ID = os.getenv('BOT_ID_DEV')
    TOKEN = os.getenv('TOKEN_DEV')
    PREFIX = os.getenv('PREFIX_DEV')
    MODE = 'DEVELOPMENT MODE'

    GUILD_ID = os.getenv('GUILD_DEV')
    CHANNEL_EVENT_ID = os.getenv('CHANNEL_EVENT_DEV')
    CHANNEL_MESSAGE_ID = os.getenv('CHANNEL_BOT_DEV')
    CHANNEL_STICK_NOTES_ID = os.getenv('CHANNEL_STICK_NOTES_DEV')
else:
    BOT_ID = os.getenv('BOT_ID')
    TOKEN = os.getenv('TOKEN')
    PREFIX = os.getenv('PREFIX')
    MODE = 'PRODUCTION MODE'

    GUILD_ID = int(os.getenv('GUILD'))
    CHANNEL_EVENT_ID = int(os.getenv('CHANNEL_EVENT'))
    CHANNEL_MESSAGE_ID = int(os.getenv('CHANNEL_BOT'))
    CHANNEL_STICK_NOTES_ID = int(os.getenv('CHANNEL_STICK_NOTES'))
