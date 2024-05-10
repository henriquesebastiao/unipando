from decouple import config
from dotenv import load_dotenv

load_dotenv()

DEBUG = config('DEBUG', default=False, cast=bool)

COLOR_YELLOW = 0xFDDA46
COLOR_CYAN = 0x7AE8FF
COLOR_BLUE = 0x0068BE
COLOR_DARK_BLUE = 0x0B254D
