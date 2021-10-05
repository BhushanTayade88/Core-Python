class Myrange:   #Iterable class
    def __init__(self,n):
        self.n = n
        self.i = 0
    def __iter__(self):
        return Myrange_itr(self.n)
    
class Myrange_itr:  #Iterator class
    def __init__(self,n):
        self.n = n
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i<self.n:
            x = self.i
            self.i += 1
            return x
        else:
            raise StopIteration()
