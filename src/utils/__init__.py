"""
Utils package initialization.

This module loads environment variables from the `.env` file and sets up global variables
for use across the package. It also provides a function to reload environment variables.
"""

from dotenv import load_dotenv
import os

def load_environment_variables():
    """
    Load environment variables from the .env file and set global variables.
    """
    load_dotenv(override=True)

    global URL, ACCOUNT_SID, AUTH_TOKEN, FROM_WHATSAPP_NUMBER, RECIPIENTS

    URL = os.getenv('URL')
    ACCOUNT_SID = os.getenv('ACCOUNT_SID')
    AUTH_TOKEN = os.getenv('AUTH_TOKEN')
    FROM_WHATSAPP_NUMBER = os.getenv('FROM_WHATSAPP_NUMBER')
    RECIPIENTS = os.getenv('RECIPIENTS').split(',')

# Initial load of environment variables
load_environment_variables()
