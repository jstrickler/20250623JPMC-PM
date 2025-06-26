class Months:
    MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
    def __init__(self):
        self._index = -1

    def __next__(self):
        if self._index < (len(self.MONTHS) - 1):
            self._index += 1
            return self.MONTHS[self._index]
        else:
            raise StopIteration()

    def __iter__(self):
        return self

m = Months()
for month in m:
    print(month)