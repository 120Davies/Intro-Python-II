from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

guide = """Ye find theyself upon adventure. Move ye to different rooms using 'n', 'e', 's', or 'w'. Pick up yonder items
as thou goest. Press 'q' to quit. Or just get up depart yonder."""

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

p_name = input("What is your name? ")
if p_name == '':
    print("That's not going to work. Let's call you Pants, the unspeaking.\n")
    p_name = 'Pants'


p_items = [Item("Taco", "Thy luncheon.")]
r_items = [Item("Flask", "An iron flask for portable beverage.")]
player = Player(p_name, room['outside'], items = p_items)
room['outside'].items = r_items

print(f'Hello {player.name}.\n')

wrapper = textwrap.TextWrapper(width = 50)
[print(i) for i in wrapper.wrap(text = guide)]
print('\n')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.


done=False

while not done: # Or 'while not done:'
    print(f'Ye find thyself in yon {player.c_room.name}.\n'
    f'{player.c_room.description}\n')
    inp = input()
    if inp[0] == "q":
        done = True
    elif inp[0] == "n":


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
