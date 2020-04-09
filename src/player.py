# Write a class to hold player information, e.g. what room they are in
# currently.

class player:

    def __init__(self, name, c_room):
        self.name = name
        self.c_room = c_room
        self.inventory = []
    def __str__(self):
        return f'{self.name}, {self.c_room}'
