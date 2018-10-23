from .BaseMethod import BaseMethod
from ...parameters import utils as parameter_utils

"""
Imports:
    .BaseMethod.BaseMethod
    ...parameters.utils as parameter_utils

Contains:
    <ParamMethod>
"""

class ParamMethod(BaseMethod):
    """
    Inherits from <BaseMethod>
    Returns data as a {<ParameterType>: val} dictionary
    For use with requests that return JavaScript variables
    ... E.g. var status=1;
    """

    def __init__(self, *args, **kwargs):
        """
        Initialises super
        """

        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        """
        Shorthand wrapper for self.get
        """

        return self.get(*args, **kwargs)

    def get \
            (
                self,
                get_parameters={},
                post_parameters={},
                files={},
                _get_parameters={},
                _post_parameters={},
                _files={},
                http=None,
                **kwargs,
            ):
        """
        Wrapper for BaseMethod.get
        ... returning it as a {<ParameterType>: val} dictionary
        For use with requests that return JavaScript variables
        ... E.g. var status=1;
        """

        for get_parameter, get_parameter_value in get_parameters.items():
            _get_parameters.update({get_parameter.setter_identifier: get_parameter_value})

        for post_parameter, post_parameter_value in post_parameters.items():
            _post_parameters.update({post_parameter.setter_identifier: post_parameter_value})

        for file, file_value in files:
            _files.update({file.identifier: file_value})

        resp = super().get \
        (
            http = http,
            post_parameters = _post_parameters,
            files = _files,
            **_get_parameters,
        )

        if not resp.failed():
            resp_dict = resp.parse_js()
        else:
            resp_dict = {}

        resp_params = {}
        resp_lost_params = {}

        for key, val in resp_dict.items():
            parameter = parameter_utils.get_parameter(get_identifier=key, endpoint=self.endpoint)

            if parameter is not None:
                resp_params[parameter] = val
            else:
                resp_lost_params[key] = val

        return resp_params
