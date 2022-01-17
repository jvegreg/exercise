"""Tools for getting links from a given webpage"""
from fastapi import FastAPI

from . import linker

app = FastAPI()


@app.get("/get_links")
async def get_links(url: str):
    """Get all links from a given webpage.

    Parameters
    ----------
    url : str
        Target webpage's url.

    Returns
    -------
    list(str)
        List of links found
    """
    return linker.get_links(url)


@app.get("/get_http_links")
async def get_http_links(url: str):
    """Get http links from a given webpage.

    Parameters
    ----------
    url : str
        Target webpage's url.

    Returns
    -------
    list(str)
        List of links found
    """
    return linker.get_http_links(url)


@app.get("/get_ftp_links")
async def get_ftp_links(url: str):
    """Get ftp links from a given webpage.

    Parameters
    ----------
    url : str
        Target webpage's url.

    Returns
    -------
    list(str)
        List of links found
    """
    return linker.get_ftp_links(url)
