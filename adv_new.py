from room import Room
from player import Player
from world import World
from ast import literal_eval
import random

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


# Load world
world = World()
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
player = Player(world.starting_room)



def backtrack_to_unexplored(player, movesQueue):
    q = Queue()
    visited = set()
    q.enqueue([player.current_room.id])
    while q.size() > 0:
        path = q.dequeue()
        last_room = path[-1]
        if last_room not in visited:
            visited.add(last_room)
            for exit in graph[last_room]:
                if graph[last_room][exit] == "?":
                    return path
                else:
                    dup_path = list(path)
                    dup_path.append(graph[last_room][exit])
                    q.enqueue(dup_path)
    return []  # Algorithm done!


def enqueue_moves(player, movesQueue):
    currentRoomExits = graph[player.current_room.id]
    unexploredExits = []
    for direction in currentRoomExits:
        if currentRoomExits[direction] == "?":
            unexploredExits.append(direction)
    if len(unexploredExits) == 0:
        path_to_unexplored = backtrack_to_unexplored(player, movesQueue)
        room_on_path = player.current_room.id
        for next_room in path_to_unexplored:
            for direction in graph[room_on_path]:
                if graph[room_on_path][direction] == next_room:
                    movesQueue.enqueue(direction)
                    room_on_path = next_room
                    break
    else:
        movesQueue.enqueue(unexploredExits[random.randint(0, len(unexploredExits) - 1)])


# Current best solution
# 957
# ['s', 'e', 'e', 'e', 'n', 'e', 's', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'e', 's', 'e', 's', 'n', 'w', 'n', 'n', 's', 'e', 'e', 's', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'w', 'w', 's', 'w', 'w', 'w', 'w', 'w', 'w', 's', 'w', 'w', 's', 'e', 'e', 'e', 's', 'n', 'e', 's', 'n', 'e', 'e', 'w', 's', 'e', 's', 'n', 'e', 'e', 'n', 'e', 'e', 'e', 'w', 'w', 's', 'e', 's', 'n', 'e', 'w', 'w', 'n', 'w', 's', 'w', 's', 'e', 'e', 'w', 'w', 'n', 'w', 'w', 's', 'w', 's', 's', 'e', 'e', 'w', 's', 's', 'w', 'e', 'n', 'e', 'e', 's', 'n', 'w', 's', 's', 'n', 'n', 'w', 'n', 'w', 's', 'n', 'n', 'e', 'e', 'e', 'e', 's', 's', 'e', 'w', 'n', 'e', 'w', 'n', 'w', 's', 'n', 'w', 'w', 'w', 'n', 'e', 'n', 'n', 'w', 'w', 'w', 's', 's', 'e', 's', 'w', 'e', 's', 'n', 'n', 'w', 'n', 'n', 'w', 'w', 's', 'e', 's', 'n', 'w', 's', 'n', 'n', 'n', 'w', 's', 's', 's', 'n', 'w', 's', 's', 's', 's', 'n', 'e', 'w', 'n', 'e', 'e', 's', 's', 'w', 's', 'n', 'e', 's', 's', 'w', 'w', 'w', 'w', 'n', 'n', 'n', 'e', 's', 's', 'e', 'w', 'n', 'n', 'w', 'w', 's', 's', 's', 's', 'e', 's', 'n', 'w', 'n', 'w', 's', 'n', 'e', 'n', 'n', 'w', 's', 'n', 'e', 'n', 'w', 'e', 'e', 'n', 'w', 'e', 'n', 'n', 'e', 's', 'n', 'n', 'e', 'n', 'n', 'e', 'n', 'w', 'w', 'n', 'n', 'n', 'w', 'n', 's', 'e', 's', 's', 'w', 'n', 's', 'w', 'n', 'n', 'n', 'n', 'w', 'w', 'e', 'e', 's', 's', 's', 's', 'w', 'n', 'w', 'n', 'n', 's', 's', 'w', 'n', 'n', 's', 's', 'e', 'e', 'n', 'n', 's', 's', 's', 'e', 'e', 'e', 's', 'w', 'e', 'e', 'n', 'n', 's', 's', 'e', 'e', 'e', 'e', 'e', 'n', 'e', 'w', 's', 'e', 'e', 'n', 'e', 'n', 'e', 'w', 's', 'e', 'e', 'e', 'w', 'n', 'e', 'e', 'n', 'e', 'n', 's', 'e', 'n', 's', 'w', 'w', 'n', 's', 's', 's', 'n', 'e', 's', 'n', 'e', 's', 'n', 'w', 'w', 'w', 'w', 's', 'w', 's', 'n', 'w', 'w', 's', 'w', 'w', 'w', 'n', 's', 'w', 'w', 'w', 'n', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'e', 'n', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'n', 's', 'w', 'w', 'w', 'n', 'e', 'e', 'n', 'e', 'e', 'w', 'w', 's', 'w', 'w', 's', 'w', 'w', 'w', 'n', 'n', 'e', 'e', 'n', 'n', 'n', 'e', 'n', 'w', 'n', 'n', 'n', 'w', 's', 'n', 'n', 's', 'e', 'n', 's', 's', 'e', 'n', 'n', 'n', 's', 's', 's', 'w', 's', 's', 'e', 'e', 's', 'e', 'n', 's', 's', 'e', 'w', 'n', 'w', 'n', 'w', 'n', 'e', 'e', 'e', 'n', 's', 's', 'e', 'w', 'n', 'w', 'w', 'n', 'e', 'n', 's', 'w', 'n', 'n', 's', 's', 's', 'w', 's', 's', 'w', 's', 's', 'e', 'n', 'e', 's', 's', 'n', 'e', 'e', 'e', 'e', 's', 'n', 'e', 'w', 'w', 'n', 'e', 'e', 'e', 'w', 'w', 'w', 'n', 'w', 'e', 'e', 'w', 's', 's', 'w', 'w', 'w', 'n', 'w', 's', 'w', 's', 'e', 'w', 'w', 'w', 'n', 'e', 'n', 'n', 'n', 'w', 'e', 'n', 'w', 'n', 'w', 'e', 's', 'e', 's', 's', 's', 's', 'w', 'n', 'n', 's', 'w', 'n', 'n', 'n', 's', 's', 's', 'w', 'e', 'e', 's', 's', 's', 'e', 'e', 'w', 'w', 's', 's', 'e', 'e', 'w', 'w', 'n', 'w', 'n', 'n', 'n', 'w', 'e', 's', 's', 's', 's', 'w', 'w', 'n', 'n', 'n', 'n', 'n', 'n', 'w', 'e', 'e', 'n', 'n', 's', 's', 'w', 'n', 'n', 'n', 's', 's', 'w', 'w', 'n', 'n', 's', 's', 'w', 'n', 'n', 'n', 'n', 's', 'e', 'n', 's', 'w', 's', 's', 's', 's', 's', 'w', 'n', 'n', 'n', 'w', 's', 'n', 'n', 'n', 'e', 'n', 's', 'w', 's', 's', 'e', 'n', 's', 's', 's', 's', 's', 'w', 'n', 'n', 'w', 'e', 's', 's', 'w', 'n', 's', 'e', 'e', 'e', 's', 'w', 'e', 's', 'e', 'n', 's', 's', 'e', 'n', 'n', 'n', 'w', 'e', 'n', 'w', 'n', 's', 'e', 's', 's', 's', 's', 's', 'e', 'n', 'e', 'n', 'n', 's', 's', 'w', 's', 'w', 's', 's', 's', 'e', 'e', 'w', 'w', 'w', 'w', 's', 'w', 's', 'n', 'w', 's', 's', 'w', 'e', 's', 'w', 's', 'w', 'w', 'e', 's', 'w', 's', 's', 'n', 'w', 'e', 'n', 'w', 'e', 'e', 's', 's', 's', 's', 'n', 'n', 'n', 'n', 'n', 'e', 'n', 'e', 'n', 'n', 'w', 'e', 'n', 'w', 'w', 's', 'w', 'w', 'e', 'n', 'w', 'e', 's', 'e', 's', 's', 'w', 'e', 'n', 'w', 'w', 's', 's', 'n', 'w', 'w', 'w', 'e', 'e', 's', 'w', 's', 'w', 'w', 'e', 'e', 'e', 's', 'n', 'w', 'n', 'w', 'w', 'e', 'e', 'e', 'n', 'e', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 'e', 'e', 'n', 'n', 'n', 's', 'e', 'n', 's', 'e', 'e', 'e', 'n', 'w', 'w', 'n', 'w', 'w', 'w', 'w', 'w', 'n', 'n', 'n', 'e', 'n', 's', 'w', 'n', 's', 's', 'w', 'w', 'e', 'n', 'n', 'n', 'e', 'e', 'w', 'n', 'w', 'e', 's', 'w', 's', 's', 'w', 'w', 's', 'n', 'n', 'n', 's', 's', 'w', 'e', 'e', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 'e', 's', 'e', 's', 'w', 'w', 'w', 'w', 'n', 'w', 'w', 'e', 'e', 's', 'e', 'e', 'e', 'e', 's', 'w', 'w', 's', 'w', 'w', 'e', 'e', 'n', 'w', 'w', 'e', 'e', 'e', 'e', 'e', 'n', 'e', 'w', 'n', 's', 's', 's', 'w', 's', 'w', 'w', 'e', 'e', 's', 'w', 'w', 'e', 'e', 'n', 'n', 'w', 'e', 'e', 'n', 'e', 's', 'n', 'e', 'n', 's', 'e', 'e', 's', 'e', 'e', 'e', 'e', 's', 's', 's', 'w', 's', 's', 'w', 'e', 'e', 'e', 'e', 's', 'e', 's', 's', 'n', 'e', 's', 's', 'n', 'n', 'w', 'n', 'w', 's', 's', 's', 'e', 's', 'w', 'w', 'e', 's']


numTrials = 100

bestLen = 99999999999
bestPath = []
for i in range(numTrials):
    player = Player(world.starting_room)
    graph = {}

    newRoom = {}
    for direction in player.current_room.get_exits():
        newRoom[direction] = "?"
    graph[world.starting_room.id] = newRoom

    movesQueue = Queue()
    totalMoves = []
    enqueue_moves(player, movesQueue)

    inverse_directions = {"n": "s", "s": "n", "e": "w", "w": "e"}

    while movesQueue.size() > 0:
        startRoom = player.current_room.id
        nextMove = movesQueue.dequeue()
        player.travel(nextMove)
        totalMoves.append(nextMove)
        endRoom = player.current_room.id
        graph[startRoom][nextMove] = endRoom
        if endRoom not in graph:
            graph[endRoom] = {}
            for exit in player.current_room.get_exits():
                graph[endRoom][exit] = "?"
        graph[endRoom][inverse_directions[nextMove]] = startRoom
        if movesQueue.size() == 0:
            enqueue_moves(player, movesQueue)
    if len(totalMoves) < bestLen:
        bestPath = totalMoves
        bestLen = len(totalMoves)


# print(bestPath)
# print(bestLen)

# totalMoves = bestPath

# bestPath = ['s', 'e', 'e', 'e', 'n', 'e', 's', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'e', 's', 'e', 's', 'n', 'w', 'n', 'n', 's', 'e', 'e', 's', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'w', 'w', 's', 'w', 'w', 'w', 'w', 'w', 'w', 's', 'w', 'w', 's', 'e', 'e', 'e', 's', 'n', 'e', 's', 'n', 'e', 'e', 'w', 's', 'e', 's', 'n', 'e', 'e', 'n', 'e', 'e', 'e', 'w', 'w', 's', 'e', 's', 'n', 'e', 'w', 'w', 'n', 'w', 's', 'w', 's', 'e', 'e', 'w', 'w', 'n', 'w', 'w', 's', 'w', 's', 's', 'e', 'e', 'w', 's', 's', 'w', 'e', 'n', 'e', 'e', 's', 'n', 'w', 's', 's', 'n', 'n', 'w', 'n', 'w', 's', 'n', 'n', 'e', 'e', 'e', 'e', 's', 's', 'e', 'w', 'n', 'e', 'w', 'n', 'w', 's', 'n', 'w', 'w', 'w', 'n', 'e', 'n', 'n', 'w', 'w', 'w', 's', 's', 'e', 's', 'w', 'e', 's', 'n', 'n', 'w', 'n', 'n', 'w', 'w', 's', 'e', 's', 'n', 'w', 's', 'n', 'n', 'n', 'w', 's', 's', 's', 'n', 'w', 's', 's', 's', 's', 'n', 'e', 'w', 'n', 'e', 'e', 's', 's', 'w', 's', 'n', 'e', 's', 's', 'w', 'w', 'w', 'w', 'n', 'n', 'n', 'e', 's', 's', 'e', 'w', 'n', 'n', 'w', 'w', 's', 's', 's', 's', 'e', 's', 'n', 'w', 'n', 'w', 's', 'n', 'e', 'n', 'n', 'w', 's', 'n', 'e', 'n', 'w', 'e', 'e', 'n', 'w', 'e', 'n', 'n', 'e', 's', 'n', 'n', 'e', 'n', 'n', 'e', 'n', 'w', 'w', 'n', 'n', 'n', 'w', 'n', 's', 'e', 's', 's', 'w', 'n', 's', 'w', 'n', 'n', 'n', 'n', 'w', 'w', 'e', 'e', 's', 's', 's', 's', 'w', 'n', 'w', 'n', 'n', 's', 's', 'w', 'n', 'n', 's', 's', 'e', 'e', 'n', 'n', 's', 's', 's', 'e', 'e', 'e', 's', 'w', 'e', 'e', 'n', 'n', 's', 's', 'e', 'e', 'e', 'e', 'e', 'n', 'e', 'w', 's', 'e', 'e', 'n', 'e', 'n', 'e', 'w', 's', 'e', 'e', 'e', 'w', 'n', 'e', 'e', 'n', 'e', 'n', 's', 'e', 'n', 's', 'w', 'w', 'n', 's', 's', 's', 'n', 'e', 's', 'n', 'e', 's', 'n', 'w', 'w', 'w', 'w', 's', 'w', 's', 'n', 'w', 'w', 's', 'w', 'w', 'w', 'n', 's', 'w', 'w', 'w', 'n', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'e', 'n', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'n', 's', 'w', 'w', 'w', 'n', 'e', 'e', 'n', 'e', 'e', 'w', 'w', 's', 'w', 'w', 's', 'w', 'w', 'w', 'n', 'n', 'e', 'e', 'n', 'n', 'n', 'e', 'n', 'w', 'n', 'n', 'n', 'w', 's', 'n', 'n', 's', 'e', 'n', 's', 's', 'e', 'n', 'n', 'n', 's', 's', 's', 'w', 's', 's', 'e', 'e', 's', 'e', 'n', 's', 's', 'e', 'w', 'n', 'w', 'n', 'w', 'n', 'e', 'e', 'e', 'n', 's', 's', 'e', 'w', 'n', 'w', 'w', 'n', 'e', 'n', 's', 'w', 'n', 'n', 's', 's', 's', 'w', 's', 's', 'w', 's', 's', 'e', 'n', 'e', 's', 's', 'n', 'e', 'e', 'e', 'e', 's', 'n', 'e', 'w', 'w', 'n', 'e', 'e', 'e', 'w', 'w', 'w', 'n', 'w', 'e', 'e', 'w', 's', 's', 'w', 'w', 'w', 'n', 'w', 's', 'w', 's', 'e', 'w', 'w', 'w', 'n', 'e', 'n', 'n', 'n', 'w', 'e', 'n', 'w', 'n', 'w', 'e', 's', 'e', 's', 's', 's', 's', 'w', 'n', 'n', 's', 'w', 'n', 'n', 'n', 's', 's', 's', 'w', 'e', 'e', 's', 's', 's', 'e', 'e', 'w', 'w', 's', 's', 'e', 'e', 'w', 'w', 'n', 'w', 'n', 'n', 'n', 'w', 'e', 's', 's', 's', 's', 'w', 'w', 'n', 'n', 'n', 'n', 'n', 'n', 'w', 'e', 'e', 'n', 'n', 's', 's', 'w', 'n', 'n', 'n', 's', 's', 'w', 'w', 'n', 'n', 's', 's', 'w', 'n', 'n', 'n', 'n', 's', 'e', 'n', 's', 'w', 's', 's', 's', 's', 's', 'w', 'n', 'n', 'n', 'w', 's', 'n', 'n', 'n', 'e', 'n', 's', 'w', 's', 's', 'e', 'n', 's', 's', 's', 's', 's', 'w', 'n', 'n', 'w', 'e', 's', 's', 'w', 'n', 's', 'e', 'e', 'e', 's', 'w', 'e', 's', 'e', 'n', 's', 's', 'e', 'n', 'n', 'n', 'w', 'e', 'n', 'w', 'n', 's', 'e', 's', 's', 's', 's', 's', 'e', 'n', 'e', 'n', 'n', 's', 's', 'w', 's', 'w', 's', 's', 's', 'e', 'e', 'w', 'w', 'w', 'w', 's', 'w', 's', 'n', 'w', 's', 's', 'w', 'e', 's', 'w', 's', 'w', 'w', 'e', 's', 'w', 's', 's', 'n', 'w', 'e', 'n', 'w', 'e', 'e', 's', 's', 's', 's', 'n', 'n', 'n', 'n', 'n', 'e', 'n', 'e', 'n', 'n', 'w', 'e', 'n', 'w', 'w', 's', 'w', 'w', 'e', 'n', 'w', 'e', 's', 'e', 's', 's', 'w', 'e', 'n', 'w', 'w', 's', 's', 'n', 'w', 'w', 'w', 'e', 'e', 's', 'w', 's', 'w', 'w', 'e', 'e', 'e', 's', 'n', 'w', 'n', 'w', 'w', 'e', 'e', 'e', 'n', 'e', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 'e', 'e', 'n', 'n', 'n', 's', 'e', 'n', 's', 'e', 'e', 'e', 'n', 'w', 'w', 'n', 'w', 'w', 'w', 'w', 'w', 'n', 'n', 'n', 'e', 'n', 's', 'w', 'n', 's', 's', 'w', 'w', 'e', 'n', 'n', 'n', 'e', 'e', 'w', 'n', 'w', 'e', 's', 'w', 's', 's', 'w', 'w', 's', 'n', 'n', 'n', 's', 's', 'w', 'e', 'e', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 'e', 's', 'e', 's', 'w', 'w', 'w', 'w', 'n', 'w', 'w', 'e', 'e', 's', 'e', 'e', 'e', 'e', 's', 'w', 'w', 's', 'w', 'w', 'e', 'e', 'n', 'w', 'w', 'e', 'e', 'e', 'e', 'e', 'n', 'e', 'w', 'n', 's', 's', 's', 'w', 's', 'w', 'w', 'e', 'e', 's', 'w', 'w', 'e', 'e', 'n', 'n', 'w', 'e', 'e', 'n', 'e', 's', 'n', 'e', 'n', 's', 'e', 'e', 's', 'e', 'e', 'e', 'e', 's', 's', 's', 'w', 's', 's', 'w', 'e', 'e', 'e', 'e', 's', 'e', 's', 's', 'n', 'e', 's', 's', 'n', 'n', 'w', 'n', 'w', 's', 's', 's', 'e', 's', 'w', 'w', 'e', 's']

totalMoves = bestPath

visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
for move in totalMoves:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == 500:
    print("TESTS PASSED!")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")

print(len(totalMoves))

print(len(visited_rooms))