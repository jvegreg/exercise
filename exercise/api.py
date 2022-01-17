"""Tools for getting links from a given webpage."""
from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from . import linker

app = FastAPI()


@app.on_event('startup')
async def startup():
    """Load and clean cache at server startup."""
    app.links_cache = linker.load_cache()
    linker.purge_cache(app.links_cache)


@repeat_every(seconds=60 * 15)
async def purge_cache():
    """Purge cache every 15 min from outdated results."""
    linker.purge_cache(app.links_cache)


@app.on_event('shutdown')
async def shutdown():
    """Save cache on server shutdown."""
    linker.save_cache(app.links_cache)


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
