# Implement a class to hold room information. This should have name and
# description attributes.
from bin import Bin

class Room(Bin):

    def __init__(self, name, description, items = None):
        super().__init__(items)
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = []

    def __str__(self):
        return f'{self.name}, {self.description}'
