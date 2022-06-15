class SparseArray:
    def __init__(self, arr, size) -> None:
        self._arr = {}
        self._size = size
        for i, x in enumerate(arr):
            if x != 0:
                self._arr[i] = x

    def set(self, i, val):
        if i < 0 or i >= self._size:
            raise IndexError("array index our of range")

        if val == 0:
            del self._arr[i]
            return

        self._arr[i] = val

    def get(self, i):
        if i < 0 or i >= self._size:
            raise IndexError("array index out of range")
        return self._arr[i]


a = [1, 0, 0, 2, 0, 0, 0, -1]
s = SparseArray(a, len(a))
print(s._arr)
s.set(1, 30)
print(s._arr)
print(s.get(1))
