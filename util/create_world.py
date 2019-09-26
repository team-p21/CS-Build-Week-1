from django.contrib.auth.models import User
from adventure.models import Player, Room


r_start = Room(title="Outside The race track", description="Press N to start", n_to=0, s_to=None, w_to=None, e_to=None, x = 0, y = -1, room_d = 'n')

r_start.save()

players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()