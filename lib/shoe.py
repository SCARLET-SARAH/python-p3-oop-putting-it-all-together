#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        if isinstance(size, int):
            self.size = size
        else:
            raise ValueError("size must be an integer")
        self.condition = "New"

    def __str__(self):
        return f"{self.brand} shoe, size {self.size}"

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

def test_requires_int_size(self):
    stan_smith = Shoe("Adidas", 9)
    with self.assertRaises(ValueError):
        stan_smith.size = "not an integer"
    