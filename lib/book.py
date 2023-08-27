#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count, prize=0):
        self.title = title
        self._prize = prize
        self.page_count = page_count
    
    @property
    def pageCount(self):
        return self.page_count
    
    @pageCount.setter
    def pageCount(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer\n")
        else:
            self.page_count = value
    @property
    def prize(self):
        return self._prize
    
    @prize.setter
    def prize(self, value):
        if value <= 0:
            raise ValueError("prize must be a positive number")
        self._prize = value

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

Book1 = Book("Learn Python in Weeks", 32, 100)
Book2 = Book("Learn JavaScript", 122, 100)



    
        