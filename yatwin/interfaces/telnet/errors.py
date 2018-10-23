"""
Library which contains Errors

Error classes are contained within Errors because
... you cannot do 'import .errors as errors'
... so instead you can do 'from .errors import Errors as errors'
... this is to avoid having to do 'from .errors import ...'
Error classes all inherit from Exception, then just 'pass'
So all they do is just change the name of the exception being raised

Contains:
    <InvalidExecutionMode>
    <LoginFailed>
    <TimeoutError>
    <ConnectionRefusedError>
"""

class InvalidExecutionMode(Exception): pass
class LoginFailed(Exception): pass
class TimeoutError(Exception): pass
class ConnectionRefusedError(Exception): pass
