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

    def all(self, url: str):
        """Shows all links from a webpage.

        Parameters
        ----------
        url : str
            Webpage's url
        """
        from .linker import get_links
        self._show_links(get_links(url))

    def http(self, url: str):
        """Show http[s] links from a given webpage

        Parameters
        ----------
        url : str
            Webpage's url
        """
        from .linker import get_http_links
        self._show_links(get_http_links(url))

    def ftp(self, url: str):
        """Shows ftp links from a webpage.

        Parameters
        ----------
        url : str
            Webpage's url
        """
        from .linker import get_ftp_links
        self._show_links(get_ftp_links(url))

    def startserver(self):
        """Start online server
        """
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
