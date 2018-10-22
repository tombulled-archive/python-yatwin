"""
Library which contains error classes

Error classes all inherit from Exception, then just 'pass'
So all they do is just change the name of the exception being raised

Contains:
    <LoginFailed>
    <TimeoutError>
    <ConnectionRefusedError>
"""

class LoginFailed(Exception): pass
class TimeoutError(Exception): pass
class ConnectionRefusedError(Exception): pass
