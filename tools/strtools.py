# TODO: Hide str methods, such as str.upper.

class OpaqueStr(str):

    # Provide easy access to otherwise hidden str methods.
    _str = property(str.__str__)
    _repr = property(str.__repr__)

    def __repr__(self):
        name = self.__class__.__name__
        return f'{name}({self._repr})'

    # Needed to prevent str.__str__ being called.
    __str__ = __repr__
