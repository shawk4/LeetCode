# Knight_to_E5
# Given the starting location of a knight on a chessboard and a target location,
# determine the minimum number of moves required to get from the starting location
# to the target location.
# assume an infinitly large chessboard in all directions
# assume the knight can only move in an L shape +-2 squares in the first axis
# and +-1 square in the second axis 

from collections import deque

# not robust enough may not find shortest path
# def direct_path(pos, target):
#   if abs(target[0] - pos[0])/2 == abs(target[1] - pos[1]):
#     return abs(target[1]-pos[1])
#   elif abs(target[1] - pos[1])/2 == abs(target[0] - pos[0]):
#     return abs(target[0]-pos[0])

# Create a n branched tree to track the breadth first search
class TreeNode():
    def __init__(self, name=[0,0], parent=None, children=None):
        self.name = name
        self.childern = []
        if name == [0,0]:
            self.parent = None
        else:
            # assert isinstance(parent, TreeNode)
            self.parent = parent
        # if children is not None:
        #     for child in children:
        #         self.add_child(child)

    def __repr__(self):
        return str(self.name)
    
    def add_child(self, node):
        # assert isinstance(node, TreeNode)
        self.childern.append(node)
       

def node_to_root(node:TreeNode):
   L = []
   que = deque()
   que.append(node)
   level_counter = 0
   while que[0].parent is not None:
      L.append(que[0].name)
      level_counter += 1
      que.appendleft(que[0].parent)
      que.pop()
    
   L.append(que[0].name)
   L[:] = reversed(L[:])
   return level_counter, L



def search(start, target):
  # Create a helper function 
  # perform a breadth first search using a while loop
  path = False
  tree = TreeNode()
  queue = deque()
  queue.append(tree)
  current_pos = tree
  positions = [[0,0]]
  move_axis1 = [2,  2,  1, -1, -2, -2, 1, -1] # !!! can be made into for loops
  move_axis2 = [1, -1, -2, -2,  1, -1, 2, 2]
  counter = 0
  
  while not path: 
    # check if the current location has a direct path to the target
    # path = direct_path(current_pos.name, target)
    if current_pos.name == target:
      levels, route = node_to_root(current_pos)
      return levels, route
    # proceed to the next eight possible locations by adding them to the tree
    for m1, m2 in zip(move_axis1, move_axis2):
      pos = [current_pos.name[0]+m1, current_pos.name[1]+m2]
      if pos not in positions:
        positions.append(pos)
        tree.add_child(TreeNode(name=pos,parent=current_pos))
        queue.appendleft(TreeNode(name=pos, parent=current_pos))
    current_pos = queue.pop()
    counter += 1
    

start = [0,0]
target = [0,1]

moves, route = search(start, target)
print(f"Number of Moves: {moves}")
print(f"Path: {route}")
        

