"""

Author: Dmytro Zuiev
Version: 1.0

"""

from threading import Thread
import time



class RepeatableTimer(Thread):
    """ A timer that, in a separate thread, initiates calling a given method 
    exactly once every N seconds.
    """
    
    def __init__(self, seconds: float, callback):
        """ 
        Args:
            seconds -- repetition time in seconds
            callback -- callback method
        """
        Thread.__init__(self)
        self.active = False
        self.seconds = seconds
        self.callback = callback

    def run(self):
        self.active = True
        self.next_time = time.time()
        while self.active:
            self.callback()
            if self.next_time + self.seconds <= time.time():
                continue
            self.next_time = self.next_time + self.seconds
            time.sleep(self.next_time - time.time())

    def stop(self):
        self.active = False
