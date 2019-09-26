#from django.contrib.auth.models import User as ModelUser
#from adventure.models import Player as PlayerModel, Room as RoomModel
import json

# Sample Python code that can be used to generate rooms in
# a zig-zag pattern.
#
# You can modify generate_rooms() to create your own
# procedural generation algorithm and use print_rooms()
# to see the world.

# For turns we need four turns
# For room names
# Otherwise, the description can be straight away
# e -> n
# n -> w
# w -> n
# n -> e

class Room:
    def __init__(self, id, title, description, x, y, room_d):
        self.id = id
        self.title = title
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y
        self.room_d = room_d
    def __repr__(self):
        #if self.e_to is not None:
         #   return f"{self.room_d} ({self.x}, {self.y}) -> ({self.e_to.x}, {self.e_to.y})"
        room_json = {
            "model": "adventure.Room",
            "pk": self.id,
            "fields": {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'n_to': self.n_to,
            's_to': self.s_to,
            'e_to': self.e_to,
            'w_to': self.w_to,
            'room_d': self.room_d,
            'x': self.x,
            'y': self.y,
            }
        }
        
        room_json2 = json.dumps(room_json)
        #print(room_json2)
        return room_json2
    def connect_rooms(self, connecting_room, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
        reverse_dir = reverse_dirs[direction]
        setattr(self, f"{direction}_to", connecting_room)
        setattr(connecting_room, f"{reverse_dir}_to", self)
    def get_room_in_direction(self, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        return getattr(self, f"{direction}_to")


class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0
        self.listOfRooms = []
    def generate_rooms(self, size_x, size_y, num_rooms):
        '''
        Fill up the grid, bottom to top, in a zig-zag pattern
        '''

        # Initialize the grid
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range( len(self.grid) ):
            self.grid[i] = [None] * size_x

        # Start from lower-left corner (0,0)
        x = -1 # (this will become 0 on the first step)
        y = 0
        room_count = 0

        # Start generating rooms to the east
        direction = 1  # 1: east, -1: west

        # If the current direction is different from the previous direction
        # go back one in the list (take the length of the list, subtract 1), change that items name to something turn (depend on which direction is turning)
        # the current rooms name will be changed to something turn

        # While there are rooms to be created...
        previous_room = None
        while room_count < num_rooms:
            # Calculate the direction of the room to be created
            if direction > 0 and x < size_x - 1:
                room_direction = "e"
                x += 1
            elif direction < 0 and x > 0:
                room_direction = "w"
                x -= 1
            else:
                # If we hit a wall, turn north and reverse direction
                room_direction = "n"
                y += 1
                direction *= -1

            
            # Create a room in the given direction
            room = Room(room_count, "A Generic Room", "This is a generic room.", x, y, room_direction)
            if previous_room is None:
                room1 = Room(room_count, "Track", "stra", x, y, room_direction)
            # connect and append rooms to json list    
            if room.room_d is "n":
                if previous_room.room_d is "e":
                    #bottom number on right side of grid
                    self.listOfRooms[len(self.listOfRooms)-1].description = "left-turn"
                    self.listOfRooms[len(self.listOfRooms)-1].w_to = previous_room.id-1
                    self.listOfRooms[len(self.listOfRooms)-1].n_to = previous_room.id+1
                    self.listOfRooms[len(self.listOfRooms)-1].e_to = None
                    #top number on right side of grid
                    room1 = Room(room_count, "Track", "left-turn", x, y, room_direction)
                    room1.s_to = previous_room.id
                    room1.w_to = room1.id+1
                        ## from model
                    self.listOfRooms.append(room1)
                else:
                    #bottom number on left side of grid
                    self.listOfRooms[len(self.listOfRooms)-1].description = "right-turn"
                    self.listOfRooms[len(self.listOfRooms)-1].e_to = previous_room.id-1
                    self.listOfRooms[len(self.listOfRooms)-1].n_to = previous_room.id+1
                    self.listOfRooms[len(self.listOfRooms)-1].w_to = None
                    # top number on left side of grid
                    room1 = Room(room_count, "Track", "right-turn", x, y, room_direction)
                    room1.s_to = previous_room.id
                    room1.e_to = room1.id+1
                        ## from model
                    self.listOfRooms.append(room1)
            else:
                ## from model
                
                if room_direction is "e":
                    room1 = Room(room_count, "Track", "straight", x, y, room_direction)
                    if room1.id-1 == -1:
                        room1.id = 0
                        room1.e_to = room1.id+1
                    else:
                        room1.w_to = room1.id-1
                        room1.e_to = room1.id+1
                    self.listOfRooms.append(room1)
                else:
                    room1 = Room(room_count, "Track", "straight", x, y, room_direction)
                    if room1.id+1 == 100:
                        room1.id = 99
                        room1.e_to = room1.id-1
                    else: 
                        room1.w_to = room1.id+1
                        room1.e_to = room1.id-1
                    self.listOfRooms.append(room1)

            # Note that in Django, you'll need to save the room after you create it

            # Save the room in the World grid
            
            self.grid[y][x] = room
            
            # Connect the new room to the previous room
            if previous_room is not None:
                ## from sample_generator
                previous_room.connect_rooms(room, room_direction)
                ## from model
              
            # Update iteration variables
            previous_room = room
            room_count += 1
        return self.listOfRooms



    def print_rooms(self):
        '''
        Print the rooms in room_grid in ascii characters.
        '''

        # Add top border
        str = "# " * ((3 + self.width * 5) // 2) + "\n"

        # The console prints top to bottom but our array is arranged
        # bottom to top.
        #
        # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid) # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"

        # Add bottom border
        str += "# " * ((3 + self.width * 5) // 2) + "\n"

        # Print string
        print(str)


w = World()
num_rooms = 100
width = 10
height = 10
data = w.generate_rooms(width, height, num_rooms)
#w.print_rooms()
print(w.generate_rooms(width, height, num_rooms))



#with open('testfile.json', 'w', encoding='utf-8') as outfile:
 # json.dump(data, outfile, ensure_ascii=False, indent=4)


#print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")
