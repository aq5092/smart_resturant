import os
# Configuration file for the bot
# Bot token and database name
# Make sure to keep this file secure and not share it publicly
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("TOKEN")
DB_NAME = os.getenv("DB_NAME")

# TOKEN = '7540878752:AAEXjPPKiP_Dp2ll1ewEc_k1SIaCE84S1ZA'
# DB_NAME = ('users.db')