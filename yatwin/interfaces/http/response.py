from . import utils
import bs4

"""
Imports:
    .utils
    bs4

Contains:
    <HttpResponse>
"""

class HttpResponse(object):
    """
    Indirect wrapper for requests.models.Response
    """

    def __init__(self, requests_resp):
        """
        Initialises class attributes
        access 'requests_resp' via HttpResponse.Response
        """

        self._init_attrs()

        self.Response = requests_resp

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name(url)>
        """

        return f'<{self.__class__.__name__}({self.Response.url})>'

    def parse_html(self):
        """
        Returns a bs4.BeautifulSoup of self.Response.text
        """

        if self.failed():
            return

        soup = bs4.BeautifulSoup(self.Response.text, 'html.parser')

        return soup

    def parse_js(self):
        """
        Returns a dictionary of the javascript variables
        E.g:
            JavaScript: var key = val;
            Dictionary: {key: val}
        """

        if self.failed():
            return

        js_dict = utils.jstopy(self.Response.text)

        return js_dict

    def parse_raw(self):
        """
        Returns self.Response.text
        """

        if self.failed():
            return

        return self.Response.text

    def parse_bytes(self):
        """
        Returns self.Response.content
        """

        if self.failed():
            return

        return self.Response.content

    def failed(self):
        """
        Returns self.Response is None

        Which indicates whether the request failed or not
        """

        return self.Response is None

    def _init_attrs(self):
        """
        Initialises class attributes
        """

        self.Response = None
