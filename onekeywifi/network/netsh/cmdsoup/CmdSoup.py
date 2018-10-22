"""
Contains:
    <CmdSoup>
"""

class CmdSoup(object):
    """
    Class to parse cmd output
    Tailored to 'netsh {interface} show networks mode=bssid'
    Also works for showing interfaces
    """

    def __init__(self, data, delimiter=':', indent='    ', sep='\n\n'):
        """
        Initialises self.
        """

        self._init_attrs()

        self.data = data
        self.delimiter = delimiter
        self.indent = indent
        self.sep = sep

    def as_dict(self):
        """
        Parses self.data, returning a dictionary of its contents
        """

        data = self.data.strip()
        sections = data.split(self.sep)

        ret_dict = {}

        for section in sections:
            section_data = self._parse_as_dict(section)

            ret_dict.update(section_data)

        return ret_dict

    def _parse_as_dict(self, data):
        """
        Parses a section of self.data, returning a dictionary of its contents
        """

        data = data.strip()

        if not data:
            return {}

        header, *nested_attrs = data.splitlines()
        header = header.strip()

        ret_data = {}

        header_data = self._parse_line_as_dict(header)

        ret_key = list(header_data.keys())[0]
        ret_data[ret_key] = header_data

        nested_nested_attrs = []
        nested_attr_last = None

        for nested_attr in nested_attrs:
            if nested_attr.startswith(self.indent * 2):
                nested_nested_attrs.append(nested_attr[len(self.indent) * 2 - 1:])

                continue
            else:
                nested_attr_data = self._parse_line_as_dict(nested_attr)

                ret_data[ret_key].update(nested_attr_data)

                if nested_nested_attrs:
                    nested_nested_data = self._parse_as_dict('\n'.join([nested_attr_last] + nested_nested_attrs))

                    ret_data[ret_key].update(nested_nested_data)

                    nested_nested_attrs = []
            nested_attr_last = nested_attr

        if nested_nested_attrs:
            nested_nested_data = self._parse_as_dict('\n'.join([nested_attr_last] + nested_nested_attrs))

            ret_data[ret_key].update(nested_nested_data)

            nested_nested_attrs = []

        return ret_data

    def _parse_line_as_dict(self, line):
        """
        Parses a line of self.data, returning a dictionary of its contents
        """

        line = line.strip()
        key, *vals = line.split(self.delimiter)
        key = key.strip()
        val = self.delimiter.join(vals).strip()

        return {key: val}

    def _init_attrs(self):
        """
        Initialise class attributes
        """

        self.data = None
        self.delimiter = None
        self.indent = None
        self.sep = None
