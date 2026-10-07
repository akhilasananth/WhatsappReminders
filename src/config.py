import os
from dotenv import load_dotenv

load_dotenv()

WHATSAPP_API_KEY = os.getenv("WHATSAPP_API_KEY")
WHATSAPP_CHAT_ID = os.getenv("WHATSAPP_CHAT_ID")
WHATSAPP_API_URL = os.getenv("WHATSAPP_API_URL")
REMINDERS_FILE = os.getenv("REMINDERS_FILE") or "data/reminders.json"
REMINDER_DUE_PARAM = os.getenv("REMINDER_DUE_PARAM") or "due_date"
REMINDER_SUBJECT_PARAM = os.getenv("REMINDER_SUBJECT_PARAM") or "reminder"
REMINDER_ADDITIONAL_MESSAGE = os.getenv("REMINDER_ADDITIONAL_MESSAGE") or ""
