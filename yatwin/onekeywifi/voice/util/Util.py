"""
Lots of this code was (pain-stakingly) converted
... from Java to Python from the Java APK Source Code

Contains:
    <Util>
"""

class Util(object):
    """
    Class containing utility functions for 'voice'
    """

    def __init__(self, *args, **kwargs):
        """
        Initialises self.
        """

        pass

    @staticmethod
    def isDigit(char):
        """
        Taken From Java APK Source Code

        Returns:
            True: 'char' is a digit
            False: 'char' is not a digit
        """

        return chr(char).isdigit()

    @staticmethod
    def isLowerChar(char):
        """
        Taken From Java APK Source Code

        Returns:
            True: 'char' is a lower-case character
            False: 'char' is not a lower-case character
        """

        return chr(char).islower()

    @staticmethod
    def isUpperChar(char):
        """
        Taken From Java APK Source Code

        Returns:
            True: 'char' is an upper-case character
            False: 'char' is not an upper-case character
        """

        return chr(char).isupper()

    @staticmethod
    def is64Char(char):
        """
        Taken From Java APK Source Code

        Returns:
            True: 'char' is a '64' character
            False: 'char' is not a '64' character
        """

        return chr(char).islower() or chr(char).isupper() or chr(char).isdigit() or chr(char) in ('_', '-')

    @staticmethod
    def char64ToInt(char):
        """
        Taken From Java APK Source Code
        """

        if Util.isUpperChar(char):
            return char - 65
        if Util.isLowerChar(char):
            return char - 97 + 26
        if Util.isDigit(char):
            return char - 48 + 52
        if chr(char) == '_':
            return 62
        if chr(char) == '-':
            return 63

        return -1

    @staticmethod
    def hexChar2Int(_c):
        """
        Taken From Java APK Source Code
        """

        if Util.isDigit(_c):
            return _c - 48
        if Util.isLowerChar(_c):
            return _c - 97 + 10
        if Util.isUpperChar(_c):
            return _c - 65 + 10

        return -1

    @staticmethod
    def int2Char64(_hex):
        """
        Taken From Java APK Source Code
        """

        if _hex >= 0 and _hex < 26:
            return 65 + _hex
        if _hex >= 26 and _hex < 52:
            return 97 + _hex - 26
        if _hex >= 52 and _hex < 62:
            return 48 + _hex - 52
        if _hex == 62:
            return 95
        if _hex == 63:
            return 45

        return -1
