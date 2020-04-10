# Rooms and players can both hold items.
# Making a bin class for things that hold items.

class Bin():
    def __init__(self, items = None):
        if not items:
            self.items = []
        else:
            self.items = items
