# Test task ― Screenshot sender
A simple Python console app to make and send screenshots every minute to an email.

The app works in a background thread, takes a screenshot every minute, and then sends it to an email address you pick.

Please note that the scripts have dependencies on the popular *pillow* module, which may require additional installation:

```sh
$ python3 -m pip install --upgrade pip
$ python3 -m pip install --upgrade Pillow
```
