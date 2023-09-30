# Test task ― Screenshot sender
It is a simple Python console app for screen activity tracking.\
The app works in a background thread, takes a screenshot every minute, and then sends it to a chosen email address. 

The program was written in such a way that you can easily change every part of the program with minimal impact on other parts―changing a delivery method to send screenshots, time intervals of taking screenshots, or the structure of a letter, etc.

Please note that the scripts have dependencies on the popular *pillow* module, which may require additional installation:

```sh
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --upgrade Pillow
```
