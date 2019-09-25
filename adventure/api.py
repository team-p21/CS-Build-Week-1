from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
from util.sample_generator import World
from django.http import HttpRequest,HttpResponse
from json import dumps
from django.core import serializers

import json

# instantiate pusher
# pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))

@csrf_exempt
@api_view(["GET"])
def initialize(request):
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.room()
    players = room.playerNames(player_id)
    return JsonResponse({'uuid': uuid, 'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players}, safe=True)

@csrf_exempt
@api_view(["GET"])
def rooms(request):
    num_rooms = 100
    width = 10
    height = 10
    rooms1 = World().generate_rooms(10,10,100)
    print(f"{rooms1}")
    test = [{"id": 0, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 0, "cords y": 0}, {"id": 1, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 1, "cords y": 0}, {"id": 2, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 2, "cords y": 0}, {"id": 3, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 3, "cords y": 0}, {"id": 4, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 4, "cords y": 0}, {"id": 5, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 5, "cords y": 0}, {"id": 6, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 6, "cords y": 
0}, {"id": 7, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 7, "cords y": 0}, {"id": 8, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 8, "cords y": 0}, {"id": 9, "name": "Track", "description": "left-turn", "room_direction": "e", "cords x": 9, "cords y": 0}, {"id": 10, "name": "Track", "description": "left-turn", "room_direction": "n", "cords x": 9, "cords y": 1}, {"id": 11, "name": "Track", "description": "stra", 
"room_direction": "w", "cords x": 8, "cords y": 1}, {"id": 12, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 7, "cords y": 1}, {"id": 13, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 6, "cords y": 1}, {"id": 14, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 5, "cords y": 1}, {"id": 15, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 4, "cords y": 1}, {"id": 16, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 3, "cords y": 1}, {"id": 17, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 2, "cords y": 1}, {"id": 18, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 1, "cords y": 1}, {"id": 19, "name": "Track", "description": "right-turn", "room_direction": "w", "cords x": 0, "cords y": 1}, {"id": 20, "name": "Track", "description": "right-turn", "room_direction": "n", "cords x": 0, "cords y": 2}, {"id": 21, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 1, "cords y": 2}, {"id": 22, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 2, "cords y": 2}, {"id": 23, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 3, "cords y": 2}, {"id": 24, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 4, "cords y": 2}, {"id": 25, "name": 
"Track", "description": "stra", "room_direction": "e", "cords x": 5, "cords y": 2}, {"id": 26, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 6, "cords y": 2}, {"id": 27, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 7, "cords y": 2}, {"id": 28, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 8, "cords y": 2}, {"id": 29, "name": "Track", "description": "left-turn", "room_direction": "e", "cords x": 9, "cords y": 2}, {"id": 30, "name": "Track", "description": "left-turn", "room_direction": "n", "cords x": 9, "cords y": 3}, {"id": 31, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 8, "cords y": 3}, {"id": 32, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 7, "cords y": 3}, {"id": 33, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 6, "cords y": 3}, {"id": 34, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 5, "cords y": 3}, {"id": 35, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 4, "cords y": 3}, {"id": 36, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 3, "cords y": 3}, {"id": 37, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 2, "cords y": 3}, {"id": 38, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 1, "cords y": 3}, {"id": 39, "name": "Track", "description": "right-turn", "room_direction": "w", "cords x": 0, "cords y": 3}, {"id": 40, "name": "Track", "description": "right-turn", "room_direction": "n", "cords x": 0, "cords y": 4}, {"id": 41, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 1, "cords y": 4}, {"id": 42, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 2, "cords y": 4}, {"id": 43, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 3, "cords y": 4}, {"id": 44, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 4, "cords y": 4}, {"id": 45, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 5, "cords y": 4}, {"id": 46, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 6, "cords y": 4}, {"id": 47, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 7, "cords y": 4}, {"id": 48, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 8, "cords y": 4}, {"id": 49, "name": "Track", "description": "left-turn", "room_direction": "e", "cords x": 9, "cords y": 4}, {"id": 50, "name": "Track", "description": "left-turn", "room_direction": "n", "cords x": 9, "cords y": 5}, {"id": 51, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 8, "cords y": 5}, {"id": 52, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 7, "cords y": 5}, {"id": 53, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 6, "cords y": 5}, {"id": 54, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 5, "cords y": 5}, {"id": 55, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 4, "cords y": 5}, {"id": 56, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 3, "cords y": 5}, {"id": 57, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 2, "cords y": 5}, {"id": 58, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 1, "cords y": 5}, {"id": 59, "name": "Track", "description": "right-turn", "room_direction": "w", "cords x": 0, "cords y": 5}, {"id": 60, "name": "Track", "description": "right-turn", "room_direction": "n", "cords x": 0, "cords y": 6}, {"id": 61, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 1, "cords y": 6}, {"id": 62, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 2, "cords y": 6}, {"id": 63, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 3, "cords y": 6}, {"id": 64, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 4, "cords y": 6}, {"id": 65, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 5, "cords y": 6}, {"id": 66, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 6, "cords y": 6}, {"id": 67, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 7, "cords y": 6}, {"id": 68, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 8, "cords y": 6}, {"id": 69, "name": "Track", "description": "left-turn", "room_direction": "e", "cords x": 9, "cords y": 6}, {"id": 70, "name": "Track", "description": "left-turn", "room_direction": "n", "cords x": 9, "cords y": 7}, {"id": 71, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 8, "cords y": 7}, {"id": 72, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 7, "cords y": 7}, {"id": 73, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 6, "cords y": 7}, {"id": 74, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 5, "cords y": 7}, {"id": 75, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 4, "cords y": 7}, {"id": 76, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 3, "cords y": 7}, {"id": 77, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 2, "cords y": 7}, {"id": 78, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 1, "cords y": 7}, {"id": 79, "name": "Track", "description": "right-turn", "room_direction": "w", "cords x": 
0, "cords y": 7}, {"id": 80, "name": "Track", "description": "right-turn", "room_direction": "n", "cords x": 0, "cords y": 8}, {"id": 81, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 1, "cords y": 8}, {"id": 
82, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 2, "cords y": 8}, {"id": 83, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 3, "cords y": 8}, {"id": 84, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 4, "cords y": 8}, {"id": 85, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 5, "cords y": 8}, {"id": 86, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 6, "cords y": 8}, {"id": 87, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 7, "cords y": 8}, {"id": 88, "name": "Track", "description": "stra", "room_direction": "e", "cords x": 8, "cords y": 8}, {"id": 89, "name": "Track", "description": "left-turn", "room_direction": "e", "cords x": 9, "cords y": 8}, {"id": 90, "name": "Track", "description": "left-turn", "room_direction": "n", "cords x": 9, "cords y": 9}, {"id": 91, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 8, "cords y": 9}, {"id": 92, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 7, "cords y": 9}, {"id": 93, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 6, "cords y": 9}, {"id": 94, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 5, "cords y": 9}, {"id": 95, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 4, "cords y": 9}, {"id": 96, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 3, "cords y": 9}, {"id": 97, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 2, "cords y": 9}, {"id": 98, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 1, "cords y": 9}, {"id": 99, "name": "Track", "description": "stra", "room_direction": "w", "cords x": 0, "cords y": 9}]
    #print(rooms1)
    #data = json.dumps(rooms1, indent=0, sort_keys=True, default=str)
    return JsonResponse(test, safe=False)
    


# @csrf_exempt
@api_view(["POST"])
def move(request):
    dirs={"n": "north", "s": "south", "e": "east", "w": "west"}
    reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    data = json.loads(request.body)
    direction = data['direction']
    room = player.room()
    nextRoomID = None
    if direction == "n":
        nextRoomID = room.n_to
    elif direction == "s":
        nextRoomID = room.s_to
    elif direction == "e":
        nextRoomID = room.e_to
    elif direction == "w":
        nextRoomID = room.w_to
    if nextRoomID is not None and nextRoomID > 0:
        nextRoom = Room.objects.get(id=nextRoomID)
        player.currentRoom=nextRoomID
        player.save()
        players = nextRoom.playerNames(player_id)
        currentPlayerUUIDs = room.playerUUIDs(player_id)
        nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)
        # for p_uuid in currentPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has walked {dirs[direction]}.'})
        # for p_uuid in nextPlayerUUIDs:
        #     pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
        return JsonResponse({'name':player.user.username, 'title':nextRoom.title, 'description':nextRoom.description, 'players':players, 'error_msg':""}, safe=True)
    else:
        players = room.playerNames(player_id)
        return JsonResponse({'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'error_msg':"You cannot move that way."}, safe=True)


@csrf_exempt
@api_view(["POST"])
def say(request):
    # IMPLEMENT
    return JsonResponse({'error':"Not yet implemented"}, safe=True, status=500)
