"""

Sending screenshots by email at intervals of a minute

Author: Dmytro Zuiev
Version: 1.0

"""

from smtplib import SMTP
from datetime import datetime
from RepeatableTimer import RepeatableTimer
from ScreenshotLetter import ScreenshotLetter
from PIL import ImageGrab
import tempfile
import re



class ScreenshotSender():
    """ Sender of screenshots.
    Establishes a single (singleton) connection with the mail server, 
    takes a screenshot and sends it to the specified address.
    """

    _server = None
    
    _sender = 'noreply@dmytro.info'

    def __init__(self, recipient_email: str):
        """ Initializes the sender instance

        Args:
            recipient_email -- recipient's email address
        """
        self.recipient_email = recipient_email
        if type(self)._server is not None:
            return
        for port in [2525, 25, 465]:
            try:
                print('Connecting to the server via port', port)
                type(self)._server = SMTP('mail.adm.tools', port)
                type(self)._server.starttls()
                type(self)._server.login(type(self)._sender, '0F4Rzn9l5EBz-test')
                print('Connected.')
                break
            except TimeoutError:
                continue
            
    def __enter__(self):
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.quit()

    def quit(self):
        type(self)._server.quit()
            
    def _make_screenshot(self, temp_directore_path: str) -> str:
        file_path = temp_directore_path + '/screenshot.jpg'
        screenshot = ImageGrab.grab()
        screenshot.save(file_path, 'JPEG')
        return file_path
        
    def send_screenshot(self):
        letter = ScreenshotLetter(type(self)._sender, self.recipient_email)
        with tempfile.TemporaryDirectory() as temp_directory:
            file_path = self._make_screenshot(temp_directory)
            try:
                with open(file_path, 'rb') as image:
                    data = image.read()        
                letter.attach_image(data)        
            except IOError:        
                letter.failed()
        type(self)._server.sendmail(type(self)._sender, self.recipient_email, letter.get_content())


def get_email() -> str:
    """ Reads and validates an email

    Returns:
        The entered email
    """
    while True:
        recipient_email = input('Enter your email: ')
        recipient_email = recipient_email.strip()
        if re.fullmatch(r'[^@ ]+@([^@\. ]+\.)+[^@\. ]+', recipient_email) is None:
            print('Oopsy-doopsy. It seems like the entered email address is invalid.')
            continue
        return recipient_email




if __name__ == '__main__':

    recipient_email = get_email()
    
    with ScreenshotSender(recipient_email) as sender:
        send_timer = RepeatableTimer(60, sender.send_screenshot)
        send_timer.start()
        answer = ''
        while answer != 'y':
            answer = input('Stop monitor tracking? (y\\n): ')          
        send_timer.stop()
