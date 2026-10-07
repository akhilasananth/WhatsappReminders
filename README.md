# WhatsappReminders

Dad wanted me to remind him by messaging him a day before certain dates. I don't want to do that, it's too much to remember. So I am creating this. 


This is a cron job using github actions 

## Project Structure
```text 
reminder-app/
│
├── src/
│   ├── __init__.py
│   ├── main.py              # ⭐️ Starts the app
│   ├── whatsapp.py          # Sends WhatsApp messages
│   └── reminders.py         # Reminder data/logic
│   └── config.py            # Environment setup in one place 
│
├── data/
│   └── reminders.json

├── .env                     # Secrets/configuration
├── Pipfile
├── .gitignore
└── README.md
```