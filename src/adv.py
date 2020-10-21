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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("Please input name: ")
player = Player(name, room['outside'], [])
# Write a loop that:
#
direction = None
cur_room = None
print("You must go find the treasure because of reasons!")
input("Press any key to begin: ")

# While game is playing
while direction != "q":
    # If player has not moved
    if cur_room == player.location:
        #Current room stays stable
        cur_room = cur_room
    else:
        #current room updates to players new location
        cur_room = player.location

#print player name & location

    print(f"{player.name} is in {player.location.name}")



# * Prints the current room name
    print(f"{player.location.name}")
# * Prints the current description (the textwrap module might be useful here).
    print(place[1])

# * Waits for user input and decides what to do.
    direction = input("Please input direction: ")

# If the user enters a cardinal direction, attempt to move to the room there.
    if direction.lower() not in :

# Print an error message if the movement isn't allowed.
    else:
        print("movement not allowed")
#
# If the user enters "q", quit the game.
