"""
Module for scraping and formatting the last article from a specified URL.
"""

import requests
import logging

from bs4 import BeautifulSoup
from . import URL

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def __get_element_text(element, selector, attribute=None):
    """
    Helper function to get text or attribute value from a BeautifulSoup element.

    Args:
        element (bs4.element.Tag): The BeautifulSoup element to search within.
        selector (str): The CSS selector for the target element.
        attribute (str, optional): The attribute to extract. If None, extracts text. Defaults to None.

    Returns:
        str: The text or attribute value, or None if the element or selector is not found.
    """
    if not element:
        return None
    target = element.select_one(selector)
    return target.get(attribute).strip() if attribute and target else target.text.strip() if target else None


def format_article_for_message(article):
    """
    Format the article for WhatsApp message.

    Args:
        article (dict): The article data.

    Returns:
        dict: The formatted article data with keys 'image_path' and 'description'.
    """
    try:
        description = f"{article.get('testo_title', 'No Title')}\n\n" \
                      f"{article.get('testo_paragraph', 'No Description')}\n\n" \
                      f"{article.get('footer_link', 'No URL')}"

        formatted_article = {
            "image_path": article['foto_img_src'],
            "description": description
        }
        logging.info("Article formatted successfully.")
        return formatted_article
    except KeyError as e:
        logging.error(f"Key error during formatting article: {e}")
        return {}


def scrape_last_article(url=URL):
    """
    Scrape the last article from the provided URL.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        dict: A dictionary containing the extracted article information.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        last_article = soup.select_one(
            "article.scheda.scheda-round.scheda-news.card")

        if not last_article:
            raise ValueError("No articles found on the page.")

        article_info = {
            "foto_link": __get_element_text(last_article, "div.scheda-foto a", "href"),
            "foto_img_src": __get_element_text(last_article, "div.scheda-foto img", "src"),
            "icona_small_text": __get_element_text(last_article, "div.scheda-icona-small"),
            "testo_title": __get_element_text(last_article, "div.scheda-testo h4"),
            "testo_paragraph": __get_element_text(last_article, "div.scheda-testo p"),
            "categorie": [a.text.strip() for a in last_article.select("div.scheda-argomenti")[0].select("a")],
            "tags": [a.text.strip() for a in last_article.select("div.scheda-argomenti")[1].select("a")],
            "footer_text": __get_element_text(last_article, "div.scheda-footer a"),
            "footer_link": __get_element_text(last_article, "div.scheda-footer a", "href"),
        }

        logging.info("Successfully scraped the last article.")
        return article_info

    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
    except IndexError as e:
        logging.error(f"Error processing article elements: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

    return {}
