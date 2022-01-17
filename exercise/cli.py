"""Command line interface for the exercise."""
# Only importing fire at top level to speed up the interface.
import fire


class GetLinks():
    """Command line tool to show the links contained in any given webpage."""

    def _show_links(self, links):
        if not links:
            print('Could not found links for the given url')
            return
        print('Found links:')
        print('------------')
        for link in links:
            print(link)

    def _load_cache(self):
        from .linker import load_cache, purge_cache
        self.cache = load_cache()
        purge_cache(self.cache)

    def _save_cache(self):
        from .linker import save_cache
        save_cache(self.cache)

    def all(self, url: str):
        """Show all links from a webpage.

        Parameters
        ----------
        url : str
            Webpage's url
        """
        from .linker import get_links
        self._load_cache()
        self._show_links(get_links(url, cache=self.cache))
        self._save_cache()

    def http(self, url: str):
        """Show http[s] links from a given webpage.

        Parameters
        ----------
        url : str
            Webpage's url
        """
        from .linker import get_http_links
        self._load_cache()
        self._show_links(get_http_links(url, cache=self.cache))
        self._save_cache()

    def ftp(self, url: str):
        """Show ftp links from a webpage.

        Parameters
        ----------
        url : str
            Webpage's url
        """
        from .linker import get_ftp_links
        self._load_cache()
        self._show_links(get_ftp_links(url, cache=self.cache))
        self._save_cache()

    def startserver(self):
        """Start online server."""
        import uvicorn
        uvicorn.run('exercise.api:app', reload=True)


def run():
    """Run the `esmvaltool` program, logging any exceptions."""

    # Workaround to avoid using more for the output
    def display(lines, out):
        text = "\n".join(lines) + "\n"
        out.write(text)

    fire.core.Display = display
    fire.Fire(GetLinks())
