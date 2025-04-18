from PyMath import _utils

class Constant:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"Constant: {self.value}"

    __str__ = __repr__

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def _cmp(self, val2):
        if isinstance(val2, Constant):
            return _utils._cmp(self.value, val2.value)

        elif isinstance(val2, (int, float)):
            return _utils._cmp(self.value, val2)

        else:
            raise TypeError(f"Can't compare a Constant to a {type(val2)}. Must be Constant, int, or float.")

    def __lt__(self, b):
        return True if self._cmp(b) == -1 else False

    def __eq__(self, b):
        return True if self._cmp(b) == 0 else False

    def __gt__(self, b):
        return True if self._cmp(b) == 1 else False

    def __le__(self, b):
        return self.__lt__(b) or self.__eq__(b)

    def __ne__(self, b):
        return not self.__eq__(b)

    def __ge__(self, b):
        return self.__gt__(b) or self.__eq__(b)
