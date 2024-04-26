from dotenv import load_dotenv
import os
class Config:
    load_dotenv()
    CURRENCY = 'INR'
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    CONN_STR = os.getenv("CONN_STR")
    TELEGRAM_ID = os.getenv("TELEGRAM_ID")
    POLL_INTERVAL = os.getenv("POLL_INTERVAL")
    PORT = os.getenv("SERVERPORT")
    HOST = os.getenv("HOST")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL") #"gpt-3.5-turbo" #"gpt-3.5-turbo-16k" "gpt-4"
