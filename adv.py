from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
print(room_graph)
# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


class Queue():
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


dead_end_rooms = []
for room in room_graph:
    if len(room_graph[room][1]) == 1:
        dead_end_rooms.append(room)


def bfs(starting_room, rooms):
        # Create an empty queue and enqueue A PATH TO starting vertext ID
    queue = Queue()
    queue.enqueue([starting_room])
    # Create an empty Set to store visited vertices
    visited = set()
    path_list = []
    # While the que is not empty..
    while queue.size() > 0:
        # Deqeue the first PATH
        path = queue.dequeue()
        room_id = path[-1]
        # Grab last vertex from the PATH
        # If that vertex hasn't been visited..
        if room_id not in visited:
            if room_id not in rooms:
                path_list.append(path)
                if len(path) > len(path_list[0]):
                    break
                elif room_id in dead_end_rooms:
                    print(room_id)
                    return path
            else:
                # Then add A PATH to its neighbors to the back of the queue
                for direction in rooms[room_id]:
                    # COPY THE PATH
                    new_path = path.copy()
                    # APPEND THE NEIGHBOR TO THE BACK
                    new_path.append(rooms[room_id][direction])
                    queue.enqueue(new_path)
            # Mark it as visited
            visited.add(room_id)
    return path_list[0]


rooms_visited = {}
traversal_path = []
# """
while len(rooms_visited) < len(room_graph):
    # print(len(rooms_visited))
    if player.current_room.id not in rooms_visited:
        rooms_visited[player.current_room.id] = {}
        if len(rooms_visited) == len(room_graph):
            break
        current = rooms_visited[player.current_room.id]
        if player.current_room.n_to:
            current['n'] = player.current_room.n_to.id
        if player.current_room.s_to:
            current['s'] = player.current_room.s_to.id
        if player.current_room.w_to:
            current['w'] = player.current_room.w_to.id
        if player.current_room.e_to:
            current['e'] = player.current_room.e_to.id

    directions = []
    for direction in current:
        # If adjacent room.id not visited yet, add that direction
        if current[direction] not in rooms_visited:
            directions.append(direction)

    if len(rooms_visited) < 2:
        directions = ['n']
    elif len(rooms_visited) < 3:
        directions = ['s']
    # If all adjacent rooms have been visited
    if len(directions) == 0:
        # print(player.current_room.id)
        # print(traversal_path)
        # Find the path to the closest unexplored room
        path = bfs(player.current_room.id, rooms_visited)
        # print(path)
        for room_id in path:
            # print(room_id)
            # print(current)
            # print("exits", player.current_room.get_exits())
            for direction in current:
                if current[direction] == room_id:
                    # print(direction)
                    player.travel(direction)
                    traversal_path.append(direction)
                    break
            # print(traversal_path)
            if room_id in rooms_visited:
                current = rooms_visited[room_id]

    else:
        direction = random.choice(directions)
        # print(direction)
        player.travel(direction)
        traversal_path.append(direction)
# """
# print(traversal_path)
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    # print(player.current_room.get_exits())
    # print(player.current_room.n_to.id)
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
