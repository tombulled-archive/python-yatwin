"""
Library which contains errors

All errors inherit from <Exception>, then pass
... essentially just renaming the <Exception>

Contains:
    <FileDoesNotExist>
    <InvalidArgument>
    <ParseError>
"""

class FileDoesNotExist(Exception): pass
class InvalidArgument(Exception): pass
class ParseError(Exception): pass
