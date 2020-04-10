# Write a class to hold player information, e.g. what room they are in
# currently.
from bin import Bin

class Player(Bin):

    def __init__(self, name, c_room, items=None):
        super().__init__(items)
        self.name = name
        self.c_room = c_room

    def __str__(self):
        p = "Thou art in"+str(self.c_room) + "\n" + "In thy bag ye have:\n" + "\n".join([str(i) for i in self.items])
        return p

    # def move(self, inp_dir):
    #     n_room = getattr(self.c_room.__dict__[f'(inp_dir)_to'])
    #
