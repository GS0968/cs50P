class Jar:
    def __init__(self, capacity=12):
        if capacity>=0:
            self.limit=capacity
        else:
            raise ValueError
        self.amount=0

    def __str__(self):
        string=str("")
        for _ in range(self.amount):
            string=string+"🍪"
        return string

    def deposit(self, n):
        size=self.amount+n
        if size>self.limit:
            raise ValueError
        else:
            self.amount=size

    def withdraw(self, n):
        size=self.amount-int(n)
        if size<0:
            raise ValueError
        else:
            self.amount=size

    @property
    def capacity(self):
        return self.limit

    @property
    def size(self):
        return self.amount
