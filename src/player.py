# Write a class to hold player information, e.g. what room they are in
# currently.
from bin import Bin

class Player(Bin):

    def __init__(self, name, c_room, items=None):
        super().__init__(items)
        self.name = name
        self.c_room = c_room

    def __str__(self):
        return f'{self.name}, {self.c_room}'

    # def move(self, inp_dir):
    #     new_room = self.c_room.__dict__[f'(inp_dir)_to']
