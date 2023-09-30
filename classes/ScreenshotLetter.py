"""

Author: Dmytro Zuiev
Version: 1.0

"""

from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate, formataddr
from datetime import datetime



class ScreenshotLetter():
    """
    The class encapsulates the formation and preparation of a letter for sending
    """
    
    def __init__(self, mail_from: str, mail_to: str):
        self._message = MIMEMultipart()
        self._message['To'] = formataddr((mail_to, mail_to))
        self._message['From'] = formataddr(('Watch screen', mail_from))
        self._message['Date'] = formatdate(localtime = True)
        self._datetime = datetime.now()
        self._subject = 'Screenshot {}'.format(self._datetime.strftime('%d.%m.%Y %H:%M'))
        self._content = 'Here we go:'

    def attach_image(self, image_data):
        attachment = MIMEBase('application', "octet-stream")
        attachment.set_payload(image_data)
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition',
            'attachment; filename="screenshot_{}.jpg"'.format(self._datetime.time()))
        self._message.attach(attachment)

    def get_content(self) -> str:
        self._message['Subject'] = self._subject
        self._message.attach(MIMEText(self._content))
        return self._message.as_string()

    def failed(self, message: str):
        self._subject = 'Failed to send screenshot'
        self._content = 'Our team is already working on solving this problem (it isn\'t)'
