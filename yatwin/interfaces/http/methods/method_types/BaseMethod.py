from ..constants import methods
from . import decorators

"""

Imports:
    ..constants.methods
    .decorators

Contains:
    <BaseMethod>
"""

class BaseMethod(object):
    """
    Base Method object. Designed to be inherited from.
    """

    def __init__ \
            (
                self,
                http = None,
                endpoint = None,
                description = None,
                get_parameters = None,
                post_parameters = None,
                returns = None,
                permission = None,
                method = None,
                files = None,
            ):
        """
        Initialises self.

        :param http - If specified, will not need to be passed to __call__
            ... stored as self.Http
        """

        self._init_attrs()

        self.endpoint = endpoint
        self.description = description
        self.get_parameters = get_parameters
        self.post_parameters = post_parameters
        self.returns = returns
        self.permission = permission
        self.method = method
        self.files = files

        self.Http = http

    def __call__(self, *args, **kwargs):
        """
        Shorthand wrapper for self.get
        """

        resp = self.get(*args, **kwargs)

        return resp.parse_raw()

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name(endpoint)>
        """

        return f'<{self.__class__.__name__}({self.endpoint})>'

    @decorators.kwarg_or_attr('http', attr='Http', not_in=(None,))
    def get(self, http=None, post_parameters={}, files={}, **get_parameters):
        """
        Imitate a function call.
        calls http.{self.method type} with the specified arguments.

        :param http - Leave None if self.Http is set, otherwise a <http.http.Http> object
        :param post_parameters - parameters for use with requests.post(data={post_parameters})
        :param files - files for use with requests.___(files={files})
        :param **get_parameters - for use with requests.___(params={get_parameters})
        """

        if self.method == methods.GET:
            resp = http.get(self.endpoint, params=get_parameters, files=files)
        elif self.method == methods.POST:
            resp = http.post(self.endpoint, params=get_parameters, data=post_parameters, files=files)
        else: # No method defined, assume get
            resp = http.get(self.endpoint, params=get_parameters, files=files)

        self._resp_last = resp

        return resp

    def _init_attrs(self):
        """
        Initialises the class attributes
        It creates them, then fills them with a default value (usually None)
        """

        self.endpoint = None
        self.description = None
        self.get_parameters = None
        self.post_parameters = None
        self.returns = None
        self.permission = None
        self.method = None
        self.files = None

        self.Http = None

        self._resp_last = None
