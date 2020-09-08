from room import Room
from player import Player

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
earlier adventurers. The only exit is to the south or quit with 'q'."""),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player1 = Player(room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# TODO Input parser REPL
while True:
    # print current location and room description
    print()
    print(f"Current Location: {player1.room.name}")
    print(f"Hint: {player1.room.description}")
    print()
    # take in user input
    move = str(input("Which direction would you like to go?: ")).lower()
    moves = ["n", "s", "e", "w", "q"]
    # parse through input and evaluate
    if move in moves:
        if move == 'n':
            if hasattr(player1.room, 'n_to'):
                player1.room = player1.room.n_to
            else:
                print(f"Oops nothing there still at {player1.room.name}")

        elif move == 's':
            if hasattr(player1.room, 's_to'):
                player1.room = player1.room.s_to
            else:
                print(f"Oops nothing there still at {player1.room.name}")
        elif move == 'e':
            if hasattr(player1.room, 'e_to'):
                player1.room = player1.room.e_to
            else:
                print(f"Oops nothing there still at {player1.room.name}")
        elif move == 'w':
            if hasattr(player1.room, 'w_to'):
                player1.room = player1.room.w_to
            else:
                print(f"Oops nothing there still at {player1.room.name}")
        elif move == 'q':
            print('Thanks for playing!')
            break
    else:
        print("Please enter proper command (n, s, e, w)")
