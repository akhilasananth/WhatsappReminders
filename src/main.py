import reminders 
from whatsapp import send_whatsapp_message
from config import WHATSAPP_CHAT_ID

reminders_data = reminders.get_reminders()
reminders_sent = False

for rd in reminders_data:
    if reminders.is_reminder_due_tomorrow(rd):
        message = reminders.get_reminder_message(rd)
        print(f"INFO: Sending reminder message: {message}")
        reminders_sent = True
        send_whatsapp_message(WHATSAPP_CHAT_ID, message)

if not reminders_sent:
    print("INFO: There are no reminders due tomorrow.")