from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("in yon Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("at yon Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("in yon Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("in yon Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. Thy only exit is to the south."""),
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

guide = """Ye find theyself upon adventure. Move ye to different rooms using 'n', 'e', 's', or 'w'. Inspect yon rooms with 'l'. Pick up yonder items as thou goest by 'get ye item'. Drop thy items by 'drop ye item' Press thy 'b' to access thy bag. Press 'q' to quit. Or just get up depart yonder."""

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

p_name = input("What is your name? ")
if p_name == '':
    print("That's not going to work. Let's call you Pants, the unspeaking.\n")
    p_name = 'Pants'


# Player starts with a sandwich. Outside starts with a flask.
player = Player(p_name, room['outside'], items = [Item("sandwich", "thy luncheon.")])
room['outside'].items = [Item("flask", "an iron flask for portable beverage.")]

print(f'Hello {player.name}.\n')

wrapper = textwrap.TextWrapper(width = 50)
[print(i) for i in wrapper.wrap(text = guide)]
print('\n')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
def drop_get(thing, giver, taker):
    here = False
    index = 0
    while not here and index < len(giver.items):
        if giver.items[index].name == thing:
            here = True

        else:
            index = index+1
    if not here:
        return False

    item = giver.items.pop(index)
    taker.items.append(item)

    return True

done=False

while not done:
    print(f'Ye find thyself {player.c_room.name}.\n'
    f'{player.c_room.description}\n')
    inp = input().split()
    if inp[0] == "q":
        done = True
    elif inp[0] == "n":
        n_room = player.c_room.n_to
        if n_room:
            player.c_room = n_room
        else:
            print("Ye can't go ye north.")
    elif inp[0] == "e":
        n_room = player.c_room.e_to
        if n_room:
            player.c_room = n_room
        else:
            print("Ye can't go ye eastward.")
    elif inp[0] == "s":
        n_room = player.c_room.s_to
        if n_room:
            player.c_room = n_room
        else:
            print("Ye can't go ye southward.")
    elif inp[0] == "w":
        n_room = player.c_room.w_to
        if n_room:
            player.c_room = n_room
        else:
            print("Ye can't go ye westward.")
    elif inp[0] == "b":
        print("In thy bag thou hast:")
        bag = [ print(i.name, i.description + "\n") for i in player.items ]
        if len(bag) == 0:
            print("...nothing.")

    elif inp[0] == "l":
        print("Here ye see on the ground:")
        bag = [print(i.name, i.description + ":\n") for i in player.c_room.items]
        if len(bag) == 0:
            print("...nothing.")

    elif inp[0] in ["get", "get ye"]:
        thing = " ".join(inp[-1:])
        if drop_get(thing, player.c_room, player):
            print(f'Ye got ye {thing}.')
        else:
            print(f'Ye cant get ye {thing}.')

    elif inp[0] in ["drop", "drop ye"]:
        thing = " ".join(inp[-1:])
        if drop_get(thing, player, player.c_room):
            print(f'Ye dropped ye {thing}.')
        else:
            print(f'Ye dont have ye {thing}.')

    else:
        print("I know not what ye mean.")






# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
#
#
