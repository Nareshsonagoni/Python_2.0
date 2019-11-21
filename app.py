# In order to create a common interface between different streams, we need to use abstract base class.
# It will provide some common code to its derivates.

from abc import ABC, abstractmethod

# Simple inheritance example

''' Here we are dealing with stream of data, opening from different sources.
like network, file from pc, etc..'''


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
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

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading from the file stream")


class NetworkStream(Stream):
    def read(self):
        print("Reading from the Network stream")


class MemoryStream(Stream):
    def read(self):
        print("Reading from a memory stream")


# We should keep the inheritance to 2 to 3 levels, behond that things will get complicated.

# stream = Stream() We can instance an abstract base class, like a normal class
memory = MemoryStream()
memory.read()

#
#
