import random


class Insect:
    def __init__(self, n, w, l):
        self.type = n
        self.wings = w
        self.legs = l
        self.flight = 0

    def length_of_travel(self):
        self.flight = random.randint(1, 10)

    def get_travel(self):
        return self.flight

    # def get_legs(self):
    #     return self.legs

    def insect_type(self):
        if random.randint(0, 1) == 0:
            self.type = "Housefly"
        else:
            self.type = "Mosquito"

    def get_type(self):
        return self.type

    # def get_wings(self):
    #     return self.wings
