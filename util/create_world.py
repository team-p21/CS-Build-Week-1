from django.contrib.auth.models import User
from adventure.models import Player, Room
from sample_generator import World

Room.objects.all().delete()

newWorld = World()
num_rooms = 100
width = 10
height = 10
thing = newWorld.generate_rooms(10,10,100)
testList = []
for world in thing:
  testList.append(world)

print(f"{testList} AAAAAAAAAAAAA") 

