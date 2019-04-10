import os.path


class PlaylistReader(object):

    def __init__(self, config):
        """Create an instance of a file reader that just reads a single
        directory on disk.
        """
        self._load_config(config)

    def _load_config(self, config):
        self._path = config.get('playlist', 'path')
        if os.path.isfile(self._path):
            self._time_modified = os.path.getmtime(self._path)
        else:
            self._time_modified = 0

    def search_paths(self):
        """Return a list of paths to search for files."""
        return [self._path]

    def is_changed(self):
        """Return true if the playlist file has been modified."""
        if not os.path.isfile(self._path):
            return True
        timeModified = os.path.getmtime(self._path)
        if timeModified > self._time_modified:
            self._time_modified = timeModified
            return True
        else:
            return False

    def idle_message(self):
        """Return a message to display when idle and no files are found."""
        return 'No playlist found in {0}'.format(self._path)


def create_file_reader(config):
    """Create new file reader based on reading a directory on disk."""
    return PlaylistReader(config)
