# python-yatwin: /yatwin/interfaces/imap/

## Contents:
* [constants](#example-constants)
* [Email.EmailFile](#example-emailemailfile)
* [Email.Email](#example-emailemail)
* [imap.Imap](#example-imapimap)

### Example: constants
```python
>>> from yatwin.interfaces.imap import constants
>>> from pprint import pprint
>>> 
>>> # Have a look at what constants are available
>>> pprint([attr for attr in dir(constants) if not attr.startswith('_') and attr.isupper()])
['DEFAULT_DOMAIN',
 'DEFAULT_PORT',
 'DOMAIN_GMAIL',
 'IMAPLIB_ALL',
 'IMAPLIB_INBOX',
 'IMAPLIB_RFC_822']
>>> 
>>> # Get a constants value
>>> constants.DEFAULT_DOMAIN
'imap.gmail.com'
>>> 
>>> # Change a constants value
>>> constants.DEFAULT_PORT = 999
>>> 
```

### Example: Email.EmailFile
```python
>>> # First see documentation for <imap.Imap> and <Email.Email> for how to get an Email
>>>
>>> # Display the email
>>> email
<Email(Alert Motion)>
>>>
>>> from pprint import pprint
>>>
>>> # Get files attached to the email
>>> files = email.get_files()
>>> files
[<EmailFile(VSTA805364XZTYY_2_20180826135952_1.jpg)>]
>>>
>>> # Pick a file
>>> file = files[0]
>>> file
<EmailFile(VSTA805364XZTYY_2_20180826135952_1.jpg)>
>>>
>>> # Call some methods
>>> pprint(file.get_headers())
{'Content-Disposition': 'attachment;\r\n'
                        ' filename="VSTB805264YZTYY_2_20180836135954_1.jpg"',
 'Content-Transfer-Encoding': 'base64',
 'Content-Type': 'application/octet-stream'}
 >>> raw_file_contents = file.get_contents()
 >>> len(raw_file_contents)
 45162
 >>>
```

### Example: Email.Email
```python
>>> # First see documentation for <imap.Imap> to get the inbox
>>>
>>> # View the contents of the inbox
>>> inbox
[<Email(mail test)>, <Email(Alert Motion)>, <Email(Alert Motion)>, <Email(Alert Motion)>, <Email(Alert Motion)>]
>>>
>>> from pprint import pprint
>>>
>>> # Pick an email
>>> email = inbox[1]
>>> email
<Email(Alert Motion)>
>>>
>>> # Call some methods
>>> email.get_files()
[<EmailFile(VSTA805364XZTYY_2_20180826135952_1.jpg)>]
>>> email.get_message()
'2018-08-26 13:59:52->Motion trigger\r\n'
>>> pprint(email.get_headers())
{'Content-Type': 'multipart/mixed;\r\n'
                 ' '
                 'boundary="=_5b82b259.tuOQinlj85uuT/aRTknNdytiQD6euuFiznydFJb2Kr9HvB84"',
 'Date': 'Mon, 24 Jul 2017 11:56:54 +0000',
 'From': '"Administrator" <myipcam@gmail.com>',
 'MIME-Version': '1.0',
 'Message-ID': '<5b72b24d.1c59fb91.f4579.95cd@mx.google.com>',
 'Received': 'by smtp.gmail.com (sSMTP sendmail emulation); Mon, 24 Jul 2017 '
             '11:56:54 +0000',
 'Return-Path': '<myipcam@gmail.com>',
 'Subject': 'Alert Motion',
 'To': 'myipcam@gmail.com',
 'User-Agent': 'Heirloom mailx 12.4 7/29/08'}
>>>
```

### Example: imap.Imap
```python
>>> from yatwin.interfaces import Imap
>>> 
>>> # Imap information
>>> EMAIL = 'myipcam@gmail.com'
>>> PASSWORD = 'Password1'
>>> DOMAIN = 'imap.gmail.com'
>>> PORT = 993
>>> 
>>> # Create the Imap instance
>>> imap = Imap(EMAIL, PASSWORD, domain = DOMAIN, port = PORT)
>>> imap
<Imap(myipcam:Password1@imap.gmail.com)[gmail.com]>
>>> 
>>> # Get the contents of the accounts inbox
>>> inbox = imap.get_inbox()
>>> inbox
[<Email(mail test)>, <Email(Alert Motion)>, <Email(Alert Motion)>, <Email(Alert Motion)>, <Email(Alert Motion)>]
>>> 
```
