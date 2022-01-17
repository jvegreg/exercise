"""Main module."""

import datetime
import os
from pathlib import Path

import requests
import yaml
from bs4 import BeautifulSoup

ONE_DAY = datetime.timedelta(days=1)

DEFAULT_CACHE_PATH = os.path.abspath(
    os.path.join(Path.home(), '.linker', 'cache.yml'))


def load_cache(cache_file=None):
    """Load cache from a yaml file.

    Parameters
    ----------
    cache_file : str, optional
        Path to the cache file, by default None

    Returns
    -------
    dict
        Links cache dictionary.
    """
    if not cache_file:
        cache_file = DEFAULT_CACHE_PATH
    try:
        with open(cache_file) as cache_handler:
            return yaml.safe_load(cache_handler)
    except FileNotFoundError:
        return {}


def save_cache(cache: dict, cache_file: str = None):
    """Save cache to a yaml file.

    Parameters
    ----------
    cache : dict
        Links cache dictionary
    cache_file : str, optional
        Path to the cache file, by default None
    """
    if not cache_file:
        cache_file = DEFAULT_CACHE_PATH
    if not os.path.isdir(os.path.dirname(cache_file)):
        os.makedirs(os.path.dirname(cache_file))
    with open(cache_file, 'w') as cache_handler:
        yaml.safe_dump(cache, cache_handler)


def purge_cache(cache):
    """Clean old elements from cache.

    Remove elements older than one day from the links cache.

    Parameters
    ----------
    cache : dict
        Links cache dictionary
    """
    to_delete = []
    for url, data in cache.items():
        if data['time'] < datetime.datetime.utcnow() - ONE_DAY:
            to_delete.append(url)
    for url in to_delete:
        del cache[url]


def get_http_links(url: str, cache: dict = None):
    """Get http[s] links from a given webpage.

    Parameters
    ----------
    url : str
        Webpage's url.

    Returns
    -------
    list(str)
        List of links found.
    """
    return get_links(url, cache=cache, link_type='http')


def get_ftp_links(url: str, cache: dict = None):
    """Get ftp links from a given webpage.

    Parameters
    ----------
    url : str
        Webpage's url.

    Returns
    -------
    list(str)
        List of links found.
    """
    return get_links(url, cache=cache, link_type='ftp')


def get_links(
    url: str,
    link_type: str = None,
    cache: dict = None,
):
    """Get all links from a given webpage.

    Parameters
    ----------
    url : str
        Webpage's url.
    link_type : str, optional
        If provided, only links starting with this prefix will be returned

    Returns
    -------
    list(str)
        List of links found.
    """
    if cache is not None and url in cache:
        links = cache[url]['links']
    else:
        html = _get_html(url)
        links = _get_all_links(html)
        links = [link for link in links if link]
        if cache is not None:
            cache[url] = {'time': datetime.datetime.utcnow(), 'links': links}

    if not link_type:
        return links
    found_links = []
    for link in links:
        if link.startswith(link_type):
            found_links.append(link)
    return found_links


def _get_html(url: str):
    return requests.get(url).text


def _get_all_links(html: str):
    parsed = BeautifulSoup(html, features='html.parser')
    links = parsed.find_all('a', href=True)
    return (link.attrs['href'] for link in links)
