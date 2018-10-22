from . import constants
from .Email import Email
import imaplib
import email

"""
Imports:
    .constants
    .Email.Email
    imaplib
    email

Contains:
    <Imap>
"""

class Imap(object):
    """
    Indirect wrapper for imaplib.IMAP4_SSL
    """

    def __init__ \
            (
                self,
                email,
                password,
                domain = constants.DEFAULT_DOMAIN,
                port = constants.DEFAULT_PORT
            ):
        """
        Initialises self and imaplib
        Automatically logs into the email account

        Default domain: constants.DEFAULT_DOMAIN
        Default port: constants.DEFAULT_PORT
        """

        self._init_attrs()

        self.email = email
        self.password = password
        self.domain = domain
        self.port = port

        address_name, address_domain = self._parse_email_address(self.email)

        self.address_name = address_name
        self.address_domain = address_domain

        self.Mail = imaplib.IMAP4_SSL(domain)
        self.Mail.login(email, password)

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name(username:password@imap_domain[domain])>
        """

        return \
        (
            f'<{self.__class__.__name__}'
                f'({self.address_name}:{self.password}@{self.domain})'
                    f'[{self.address_domain}]'
            '>'
        )

    def get_inbox(self, limit=5, filter=None):
        """
        Returns a list of email.Message's
        retrieved from the accounts inbox.

        :param limit - Limit the number of emails to return
        :param filter - Function to filter the messages
            Should return True if the message is to be kept
        """

        self.Mail.select(constants.IMAPLIB_INBOX)

        status_code, indexs = self.Mail.search(None, constants.IMAPLIB_ALL)
        indexs = indexs[0].split()

        messages = []

        for index_iter, index in enumerate(indexs):
            if index_iter == limit:
                break

            status_code_index, fetched = self.Mail.fetch(index, constants.IMAPLIB_RFC_822)

            fetched_string = fetched[0][1]

            message = email.message_from_string(fetched_string.decode())

            email_message = Email(message)

            if filter is None or filter(email_message):
                messages.append(email_message)

        return messages

    def _parse_email_address(self, email):
        """
        Returns 'email' as:
        ... (address_name, address_domain)
        E.g. _parse_email_address('account@dom.com')
        ... will return: ('account', 'dom.com')
        Essentially just splits the string at '@'
        """
        return email.split('@')

    def _init_attrs(self):
        """
        Initialises the class attributes
        It creates them, then fills them with a default/null value (usually None)
        """

        self.Mail = None

        self.email = None
        self.password = None
        self.domain = None
        self.port = None

        self.address_name = None
        self.address_domain = None
