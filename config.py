import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28593211"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "27ad7de4fe5cab9f8e310c5cc4b8d43d")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://emonfx:2FNeyugOXUInZ3vQ@emonfx.cvbeelh.mongodb.net/?retryWrites=true&w=majority&appName=EmonFx")
