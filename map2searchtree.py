# Node with weight
# costs initialized with zeros to make calculations efficient.

from os import stat

def get_node(name, weight=0):
    node = {}
    node['name'] = name
    node['children'] = []
    node['weight'] = weight

    return node


def add_child(node, name, weight=0):
    node['children'].append(get_node(name, weight))

# def DFS(init_state, goal_name):
    
#     frontier = [init_state]
#     explored = []
    
#     for item in frontier:
#         state = item
#         # state = frontier.pop() # dequeue
#         explored.append(state['name'])
        
#         state = frontier.index()
        
#         if state['name'] == goal_name:
#             print(state)
#             return True
#         for child in state['children']:
#             if child['name'] not in explored:
#                 # enqueue: insert node at the beginning
#                 frontier.insert(0, child)
#     return False

def BFS(init_state, goal_name):
    frontier = [init_state]
    explored = []
    while len(frontier):
        state = frontier.pop() # dequeue
        explored.append(state['name'])
        if state['name'] == goal_name:
            return True
        for child in state['children']:
            if child['name'] not in explored:
            # enqueue: insert node at the beginning
                frontier.insert(0, child)
    return False

# Building the entire search tree based on the assignment
init_state = 'Kitchener'
goal_name = 'Listowel'

tree = get_node(init_state)

# Children of Kitchener: Guelph, New Hamburg
add_child(tree, 'Guelph', weight=30)
add_child(tree, 'New Hamburg', weight=90)

# Children of Guelph: Drayton
add_child(tree['children'][0], 'Drayton', weight=100)

# Children of Drayton: Listowel
add_child(tree['children'][0]['children'][0], 'Listowel', weight=100)

# Children of New Hamburg: Stratford
add_child(tree['children'][1], 'Stratford', weight=25)

# Children of Stratford: St. Marys, Drayton
add_child(tree['children'][1]['children'][0], 'St. Marys', weight=300)
add_child(tree['children'][1]['children'][0], 'Drayton', weight=200)

# Children of St. Marys: Mitchell
add_child(tree['children'][1]['children'][0]
          ['children'][0], 'Mitchell', weight=80)

# Children of Mitchell: Listowel
add_child(tree['children'][1]['children'][0]['children']
          [0]['children'][0], 'Listowel', weight=100)

# Children of Drayton: Listowel
add_child(tree['children'][1]['children'][0]
          ['children'][1], 'Listowel', weight=100)

BFS(init_state,goal_name)