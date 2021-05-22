import random
from functools import reduce

class Array:
    def __init__(self, capacity, fill_value=None):
        self.capacity = capacity
        self.items=list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, new_item):
        self.items[index] = new_item

    def __randReplace__(self):
        return [self.__setitem__(i,random.randint(0,self.capacity)) for i in range(self.capacity)]
    
    def __sum__(self):
        return reduce(lambda start, finish: start+finish, self.items)