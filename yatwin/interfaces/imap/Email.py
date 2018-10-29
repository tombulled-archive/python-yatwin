import re

"""
Imports:
    re

Contains:
    <EmailFile>
    <Email>
"""

class EmailFile(object):
    """
    File attached to an email

    Essentially a wrapper for email.message.Message
    """

    def __init__(self, message):
        """
        Initialise self
        """

        self._init_attrs()

        self.Message = message

    def __repr__(self):
        """
        Return a string representation of the object
        ... in the form: <class_name(file_name)>
        """

        headers = self.get_headers()

        filename = self._get_filename()

        return f'<{self.__class__.__name__}({filename})>'

    def get_raw(self):
        """
        Wrapper for self.Message.as_string

        Returns the raw, string of the email
        ... this includes the headers, message,
        ... and any attachments
        """

        return self.Message.as_string()

    def get_contents(self):
        """
        Wrapper for self.Message.get_payload

        Returns the contents of the file (the raw file contents)
        """

        return self.Message.get_payload()

    def get_headers(self):
        """
        Returns a dict of self.Message._headers

        Where self.Message._headers is equivelant
        ... to self.Message.items()
        """

        return dict(self.Message._headers)

    def _get_filename(self):
        """
        Attempts to extract the filename from the
        ... Content-Disposition header
        """

        headers = self.get_headers()

        content_disposition = headers.get('Content-Disposition', None)

        if content_disposition is None:
            return

        regex_filename = r'filename="(?P<filename>.*?)"'

        search_filename = re.search(regex_filename, content_disposition)

        if search_filename is None:
            return

        filename = search_filename.group('filename')

        if filename is None:
            return

        return filename

    def _init_attrs(self):
        """
        Initialise class attributes
        """

        self.Message = None

class Email(object):
    """
    Indirect wrapper for email.message.Message
    """

    def __init__(self, message):
        """
        Initialise self
        """

        self._init_attrs()

        self.Message = message

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form: <class_name(subject)>


        Where:
            class_name -> self.__class__.__name__
            subject -> The contents of the 'Subject' header
        """

        headers = self.get_headers()

        header_subject = headers.get('Subject', '')

        return f'<{self.__class__.__name__}({header_subject})>'

    def get_raw(self):
        """
        Wrapper for self.Message.as_string

        Returns the raw, string of the email
        ... this includes the headers, message,
        ... and any attachments
        """

        return self.Message.as_string()

    def get_files(self):
        """
        Returns a list of <EmailFile>'s from the emails
        ... payload
        """

        payload = self.Message.get_payload()

        if not isinstance(payload, list):
            return []

        files = payload[1:]

        email_files = []

        for file in files:
            email_file = EmailFile(file)

            email_files.append(email_file)

        return email_files

    def get_message(self):
        """
        Returns the message part of the emails
        ... payload
        """

        payload = self.Message.get_payload()

        if isinstance(payload, str):
            return payload
        elif isinstance(payload, list):
            return payload[0].get_payload()

    def get_headers(self):
        """
        Returns a dict of self.Message._headers

        Where self.Message._headers is equivelant
        ... to self.Message.items()
        """

        return dict(self.Message._headers)

    def _init_attrs(self):
        """
        Initialises class attributes
        """

        self.Message = None
