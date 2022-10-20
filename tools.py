from lxml.etree import tostring as _lxml_etree_tostring

def str_from_elt(elt):
    return _lxml_etree_tostring(elt).decode()


def stream(data):
    for char in data:
        yield char
    while True:
        yield b''
            

class FakeFile:

    def __init__(self, data):
        self._stream = stream(data)

    def read(self, size):
        return next(self._stream)
