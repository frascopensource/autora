"""
Module for sending WhatsApp messages using the Twilio API.
"""
from twilio.rest import Client
from . import ACCOUNT_SID, AUTH_TOKEN, FROM_WHATSAPP_NUMBER


def send_whatsapp_message(recipients, body):
    """
    Send a WhatsApp message to a list of recipients.

    Args:
        recipients (list): List of recipient phone numbers.
        body (dict): The message body containing 'description' and 'image_path'.

    Returns:
        None
    """
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    for recipient in recipients:
        try:
            client.messages.create(
                body=body["description"],
                from_=FROM_WHATSAPP_NUMBER,
                to=f'whatsapp:{recipient}',
                media_url=[body["image_path"]]
            )
            print(f'Message sent to {recipient}')
        except Exception as e:
            print(f'Failed to send message to {recipient}: {e}')
