# Simple inheritance example

''' Here we are dealing with stream of data, opening from different sources.
like network, file from pc, etc..'''


class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            # here if the file is already opened we are throwing an error. to do this we need to create a custom Exception.
            raise InvalidOperationError("Stream already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            # here if the file is not opened we are throwing an error. to do this we need to create a custom Exception.
            raise InvalidOperationError("Stream not opened")
        self.opened = False


class FileStream(Stream):
    def read(self):
        print("Reading from the file stream")


class NetworkStream(Stream):
    def read(self):
        print("Reading from the Network stream")

# We should keep the inheritance to 2 to 3 levels, behond that things will get complicated.


file_stream = FileStream()
