import datetime as dt
import json
from config import REMINDERS_FILE, REMINDER_DUE_PARAM, REMINDER_SUBJECT_PARAM, REMINDER_ADDITIONAL_MESSAGE, REMINDERS


def get_reminders():
    if REMINDERS is not None:
        return REMINDERS
    
    with open(REMINDERS_FILE, "r") as file:
        return json.load(file)


def is_reminder_due_tomorrow(reminder):
    tomorrow = dt.date.today() + dt.timedelta(days=1)
    due_date = dt.date.fromisoformat(reminder[REMINDER_DUE_PARAM]) #"YYYY-MM-DD"

    return due_date == tomorrow


def get_reminder_message(reminder):
    return (f"{REMINDER_ADDITIONAL_MESSAGE}\nReminder: {reminder[REMINDER_SUBJECT_PARAM]} is due on {reminder[REMINDER_DUE_PARAM]}.")