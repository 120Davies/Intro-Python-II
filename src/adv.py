from room import Room
from player import player
from item import item
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

guide = """Move to different rooms using 'n', 'e', 's', or 'w'. Pick up items
as you go. Press 'q' to quit. Or just get up and leave, I guess."""

def move(current_room, direction):
    pass

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

name = input("what is your name? ")
if name == '':
    print("That's not going to work. Let's call you Pants, the unspeaking.\n")
    name = 'Pants'
player = Player(name, room['outside'])

print(f'Hello {name}.\n')

wrapper = textwrap.TextWrapper(width = 100)
[print(i) for i in wrapper.wrap(text = guide)]
print('\n')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

player_room = player.c_room



# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
