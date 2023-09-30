"""

Sending screenshots by email at intervals of a minute

Author: Dmytro Zuiev
Version: 1.0

"""

import re
from classes.RepeatableTimer import RepeatableTimer
from classes.ScreenshotSender import ScreenshotSender



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
