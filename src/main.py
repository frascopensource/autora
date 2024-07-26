"""
Main module to scrape the last article and send it via WhatsApp.
"""

import utils.last_article
import utils.whatsapp_sender
import utils

from utils import RECIPIENTS


if __name__ == "__main__":
    # Step 1: Get the last article
    article_info = utils.last_article.scrape_last_article()

    # Step 2: Format the article
    formatted_article = utils.last_article.format_article_for_message(
        article_info)

    # Step 3: Send the formatted article via WhatsApp
    broadcast_list = RECIPIENTS
    utils.whatsapp_sender.send_whatsapp_message(broadcast_list, formatted_article)
