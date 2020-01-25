from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

from util import Queue
import random
# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def bft(self, starting_vertex):
    queue = Queue()
    queue.enqueue(starting_vertex)
    # Create an empty Set to store visited vertices
    visited = {}
    # While the que is not empty..
    while queue.size() > 0:
        # Deqeue the first vertex
        vertex = queue.dequeue()
        # If that vertex hasn't been visited..
        if vertex not in visited:
            # Mark it as visited
            # print(v)
            visited.add(vertex)
            # Then add all of its neighbors to the back of the queue
            for neighbor in self.vertices[vertex]:
                queue.enqueue(neighbor)

rooms_visited = {}
not_visited = set()
prev_dir = None
while len(rooms_visited) < len(room_graph):
    if player.current_room.id not in rooms_visited:
        rooms_visited[player.current_room.id] = {}
        current = rooms_visited[player.current_room.id]
        if player.current_room.n_to:
            current['n'] = player.current_room.n_to.id
        if player.current_room.s_to:
            current['s'] = player.current_room.s_to.id
        if player.current_room.w_to:
            current['w'] = player.current_room.w_to.id
        if player.current_room.n_to:
            current['e'] = player.current_room.e_to.id
        
    directions = []
    if current['n']=='?' and prev_dir != 's':
        directions.append('n')
    if x > 0 and prev_dir != 'n':
        directions.append('s')
    if y > 0 and prev_dir != 'e':
        directions.append('w')
    if y < size_y - 1 and prev_dir != 'w':
        directions.append('e')

    direction = random.choice(directions)    
    prev_dir = direction
    player.travel(direction)
    traversal_path.append(direction)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    print(player.current_room.get_exits())
    print(player.current_room.n_to.id)
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
