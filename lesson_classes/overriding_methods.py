class RandomRange:
    from random import randint
    def __init__(self, start, stop, step):
        self.next = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        return self
    def __next__(self):
        if self.next > self.stop:
            raise StopIteration
        next_item = self.next
        self.next += self.step
        return next_item

for i in RandomRange(1, 10, 2):
    print(i, end=' ')
