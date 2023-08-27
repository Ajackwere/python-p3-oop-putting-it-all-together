#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.size = size
        self.brand = brand
    @property
    def sizeSet(self):
        return self.size
    
    @sizeSet.setter
    def sizeSet(self, value):
        if not isinstance(value, int):
            print("size must be an integer\n")
        else:
            self.size = value
    def cobble(self):
        print("says that the shoe has been repaired.")
    def cobble_makes_new(self, condition):
        self.condition = condition
        if self.condition == "New":
            print("New")
    

