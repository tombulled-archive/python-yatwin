from . import constants
from . import response
from . import methods
from . import utils
import requests
import urllib.parse
import logging

logging.getLogger('urllib3').setLevel(logging.ERROR)
logging.getLogger('requests').setLevel(logging.ERROR)

"""
Imports:
    .constants
    .response
    .methods
    .utils
    requests
    urllib.parse
    logging

Contains:
    <Http>

Logging is set to ERROR level for:
    urllib3
    requests
"""

class Http(object):
    """
    Indirect wrapper for requests.Session (http://docs.python-requests.org/en/master/user/advanced/#session-objects)
    Default username: constants.DEFAULT_USERNAME
    Default password: constants.DEFAULT_PASSWORD
    Default port: constants.DEFAULT_PORT
    """

    def __init__ \
            (
                self,
                host,
                username = constants.DEFAULT_USERNAME,
                password = constants.DEFAULT_PASSWORD,
                port = constants.DEFAULT_PORT
            ):
        """
        Initialises super
        Initialises class attributes
        Configures session auth

        Default username: constants.DEFAULT_USERNAME
        Default password: constants.DEFAULT_PASSWORD
        Default port: constants.DEFAULT_PORT

        If constants.AUTO_BUILD, auto-build's the object
        """

        self._init_attrs()

        self.Session = requests.Session()

        self.host = host
        self.username = username
        self.password = password
        self.port = port

        self._configure_auth()

        if constants.AUTO_BUILD:
            self.build()

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name(username:password@ip:port)>
        """

        return '<{class_name}({username}:{password}@{host}:{port})>'.format \
        (
            class_name = self.__class__.__name__,
            username = self.username,
            password = self.password,
            host = self.host,
            port = self.port,
        )

    def __call__(self, *args, **kwargs):
        """
        Shorthand wrapper for self.get
        """

        return self.get(*args, **kwargs)

    def get(self, endpoint, *args, **kwargs):
        """
        Wrapper for requests.Session.get
        Limits requests to endpoints on the cameras website
        Endpoints in the format 'somefile.ext' or 'somedir/somefile.ext' etc.

        Implements constants.TIMEOUT
        """

        url = self._make_url(endpoint)

        kwargs.update({'timeout': constants.TIMEOUT})

        try:
            resp = self.Session.get(url, *args, **kwargs)
        except requests.exceptions.ReadTimeout as read_timeout:
            resp = None

        http_resp = response.HttpResponse(resp)

        return http_resp

    def build(self):
        """
        Build the http object.
        Gets CGI methods from methods.METHODS
        ... then sets them as class methods
        Therefore, instead of doing:
            status = get_status(http_obj)
        You can do:
            status = http_obj.get_status()
        """

        for method_name, method in methods.METHODS.items():
            setattr(self, method_name, method)

            self_method = getattr(self, method_name)

            #self_method.__class__.__name__ = method_name
            self.__name__ = method_name
            self_method.__class__.__doc__ = utils.sprintf_cgi_overview(self_method)

            self_method.Http = self

            self.methods[method_name] = self_method

    def _make_url(self, endpoint=''):
        """
        Returns a url in the format 'http://username:port@host:port/endpoint?get_auth'
        """

        url = 'http://{username}:{password}@{host}:{port}/{endpoint}'.format \
        (
            username = self.username,
            password = self.password,
            host = self.host,
            port = self.port,
            endpoint = endpoint,
        )

        if self.get_auth:
            if '?' in endpoint:
                url += '&'
            else:
                url += '?'
            url += urllib.parse.urlencode(self.get_auth)

        return url

    def _configure_auth(self):
        """
        Initialises self.get_auth and requests.Session.auth
        """

        if constants.IMPLEMENT_GET_AUTH:
            self.get_auth = \
            {
                constants.PARAM_LOGINUSE: self.username,
                constants.PARAM_LOGINPAS: self.password,
            }

        self.Session.auth = (self.username, self.password)

    def _init_attrs(self):
        """
        Initialises the class attributes
        It creates them, then fills them with a default/null value (usually None)
        """

        self.host = None
        self.username = None
        self.password = None
        self.port = None
        self.get_auth = {}
        self.methods = {}
