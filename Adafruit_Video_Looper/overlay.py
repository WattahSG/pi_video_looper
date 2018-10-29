import os
import subprocess


class Overlay(object):

    def __init__(self, config, name, layer=2):
        self._process = None
        self._load_config(config, name)
        self._layer = layer

    def _load_config(self, config, name):
        self._overlay_photo = config.get(name, 'path')
        self._x = config.get(name, 'x')
        self._y = config.get(name, 'y')

    def display(self):
        args = ['/home/pi/raspidmx/pngview/pngview', '-b 0']
        args.extend(['-l {0}'.format(self._layer), '-x {0}'.format(self._x),
                     '-y {0}'.format(self._y), self._overlay_photo])
        self._process = subprocess.Popen(args,
                                         stdout=open(os.devnull, 'wb'),
                                         close_fds=True)

    def stop(self):
        # Stop showing logo
        if self._process is not None and self._process.returncode is None:
            subprocess.call(['killall', '-s', 'SIGKILL', 'pngview'])
        # Let the process be garbage collected.
        self._process = None
