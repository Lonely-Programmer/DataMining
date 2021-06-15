class zList:
    full = 0
    
    def __init__(self,x):
        self.list = x

    def __and__(self, other):
        return zList(sorted(set(self.list) & set(other.list)))

    def __or__(self, other):
        return zList(sorted(set(self.list) | set(other.list)))

    def __invert__(self):
        return zList(sorted(set(range(zList.full)) - set(self.list)))
    def emptyset():
        return zList([])