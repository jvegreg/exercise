"""Main module."""

import requests
from bs4 import BeautifulSoup


def get_http_links(url: str):
    """
    Get http links from a web page.

    All other links are discarded.
    """
    return get_links(url, link_type='http')


def get_ftp_links(url: str):
    """
    Get http links from a url.

    Only
    """
    return get_links(url, link_type='ftp')


def get_links(url: str, link_type=None):
    """
    Get http links from a url.

    Only
    """
    html = _get_html(url)

    found_links = []
    for link in _get_all_links(html):
        if link and (not link_type or link.startswith(link_type)):
            found_links.append(link)
    return found_links


def _get_html(url: str):
    return requests.get(url).text


def _get_all_links(html: str):
    parsed = BeautifulSoup(html, features='html.parser')
    links = parsed.find_all('a', href=True)
    return (link.attrs['href'] for link in links)
