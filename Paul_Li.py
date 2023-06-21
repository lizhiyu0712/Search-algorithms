# Node with weight
# costs initialized with zeros to make calculations efficient.
def get_node(name, weight=0, heuristic=0):
    node = {}
    node['name'] = name
    node['children'] = []
    node['weight'] = weight
    node['heuristic'] = heuristic
    node['path'] = []

    return node

def add_child(node, name, weight=0, heuristic=0):
    node['children'].append(get_node(name, weight,heuristic))

# Building the entire search tree based on the assignment
init_state = 'Kitchener'
goal_name = 'Listowel'

tree = get_node(init_state, 0, 130)

# Children of Kitchener: Guelph, New Hamburg
add_child(tree, 'Guelph', weight=30, heuristic=160)
add_child(tree, 'New Hamburg', weight=90, heuristic=110)

# Children of Guelph: Drayton
add_child(tree['children'][0], 'Drayton', weight=100, heuristic=100)

# Children of Drayton: Listowel
add_child(tree['children'][0]['children'][0], 'Listowel', weight=100, heuristic=0)

# Children of New Hamburg: Stratford
add_child(tree['children'][1], 'Stratford', weight=25, heuristic=100)

# Children of Stratford: St. Marys, Drayton
add_child(tree['children'][1]['children'][0], 'St. Marys', weight=30, heuristic=130)
add_child(tree['children'][1]['children'][0], 'Drayton', weight=200, heuristic=100)

# Children of St. Marys: Mitchell
add_child(tree['children'][1]['children'][0]
          ['children'][0], 'Mitchell', weight=80, heuristic=100)

# Children of Mitchell: Listowel
add_child(tree['children'][1]['children'][0]['children']
          [0]['children'][0], 'Listowel', weight=100, heuristic=0)

# Children of Drayton: Listowel
add_child(tree['children'][1]['children'][0]
          ['children'][1], 'Listowel', weight=100, heuristic=0)



#-------- 1.1
# Depth-first search
def DFS(init_state, goal_name):
    """Depth-First Search (DFS)
    Arguments
    ---------
    init_state : the root node of a search tree
    goal_name : A string, the name of a node, e.g. tree.childrend[0].name
    """
    frontier = [init_state]
    explored = []
     
    print('Test DFS!!!!!! ')
    while len(frontier):
        state = frontier.pop() # dequeue
        explored.append(state['name'])
        print('DFS: ' + state['name']) #check question 1.1
        if state['name'] == goal_name:
            return True
        for child in reversed(state['children']): # reverse the list to make it as lifo
            if child['name'] not in explored:
                # enqueue: insert node at the beginning
                frontier.append(child) # appened the child to the list
    return False

DFS(tree, goal_name)



#-------- 1.2
# Greedy helper
def find_min_heuristic(frontier):
# Helper func to find min of h (the heuristic function)
    min_h_i = 0
    if len(frontier) > 1:
        min_h = frontier[min_h_i]['heuristic']
        for i, state in enumerate(frontier):
            if state['heuristic'] < min_h:
                min_h_i = i
                min_h = state['heuristic']
    return min_h_i

def GreedySearch(init_state, goal_name):
    frontier = [init_state]
    explored = []

    print('Test Greedy Search!!!!!! ')
    while len(frontier):
        state = frontier.pop(find_min_heuristic(frontier))
        explored.append(state['name'])
        
        print('Greedy Search: ' + state['name']) #check question 1.2
        if state['name'] == goal_name:
            return True      
        for child in state['children']:
            if child['name'] not in explored:
                frontier.append(child)
    return False

GreedySearch(tree, goal_name)



#-------- 1.3.1
# Breadth-first search
def BFS(init_state, goal_name):
    """Breadth-First Search (BFS)
    Arguments
    ---------
    init_state : the root node of a search tree
    goal_name : A string, the name of a node, e.g. tree.childrend[0].name
    """
    #-------- init 
    print("BFS")    
    frontier = [init_state]
    explored = []
    totalWeight = 0
    
    #------- Iterating to find the goal 
    while len(frontier):
        state = frontier.pop() # dequeue
        state['path'].append(state['name'])
        explored.append(state['name'])
        # print(state['name'])
        if state['name'] == goal_name:
            # print('total: ', child['weight'])
            print('path: ', state['path'])
            return state['weight']
        for child in state['children']:
            if child['name'] not in explored:
                # enqueue: insert node at the beginning
                # print("Child:" + child['name'])
                child['path'].extend(state['path'])
                child['weight'] += state['weight']
                frontier.insert(0, child)
    return False
    
print('total:', BFS(tree, goal_name))



#-------- 1.3.2
# UCS helper
def find_min_weight(frontier):
    # Helper func to find min weight/distance
    min_weight_i = 0
    if len(frontier) > 1:
        min_weight = frontier[min_weight_i]['weight']
        for i, state in enumerate(frontier):
            if state['weight'] < min_weight:
                min_weight_i = i
                min_weight = state['weight']
    return min_weight_i

def UCS(init_state, goal_name):
    """Uniform Cost Search (UCS)
    Arguments
    ---------
    3
    init_state : the root node of a search tree
    goal_name : A string, the name of a node, e.g. tree.childrend[0].name
    """
    print("UCS") 
    frontier = [init_state]
    explored = []

    while len(frontier):
        # next state -> state w lowest cost/weight/distance
        state = frontier.pop(find_min_weight(frontier))
        state['path'].append(state['name'])
        explored.append(state['name'])
        
        if state['name'] == goal_name:
            print('path: ', state['path'])
            return state['weight']

        for child in state['children']:
            if child['name'] not in explored:
                child['path'].extend(state['path'])
                child['weight'] += state['weight']
                frontier.append(child)
    return False
    
# Node with weight
# costs initialized with zeros to make calculations efficient.
def get_node(name, weight=0, heuristic=0):
    node = {}
    node['name'] = name
    node['children'] = []
    node['weight'] = weight
    node['heuristic'] = heuristic
    node['path'] = []

    return node

def add_child(node, name, weight=0, heuristic=0):
    node['children'].append(get_node(name, weight,heuristic))

# Building the entire search tree based on the assignment
init_state = 'Kitchener'
goal_name = 'Listowel'

tree = get_node(init_state, 0, 130)

# Children of Kitchener: Guelph, New Hamburg
add_child(tree, 'Guelph', weight=30, heuristic=160)
add_child(tree, 'New Hamburg', weight=90, heuristic=110)

# Children of Guelph: Drayton
add_child(tree['children'][0], 'Drayton', weight=100, heuristic=100)

# Children of Drayton: Listowel
add_child(tree['children'][0]['children'][0], 'Listowel', weight=100, heuristic=0)

# Children of New Hamburg: Stratford
add_child(tree['children'][1], 'Stratford', weight=25, heuristic=100)

# Children of Stratford: St. Marys, Drayton
add_child(tree['children'][1]['children'][0], 'St. Marys', weight=30, heuristic=130)
add_child(tree['children'][1]['children'][0], 'Drayton', weight=200, heuristic=100)

# Children of St. Marys: Mitchell
add_child(tree['children'][1]['children'][0]
          ['children'][0], 'Mitchell', weight=80, heuristic=100)

# Children of Mitchell: Listowel
add_child(tree['children'][1]['children'][0]['children']
          [0]['children'][0], 'Listowel', weight=100, heuristic=0)

# Children of Drayton: Listowel
add_child(tree['children'][1]['children'][0]
          ['children'][1], 'Listowel', weight=100, heuristic=0)

print('total:', UCS(tree, goal_name))



#-------- 1.3.3
# Greedy helper
def find_min_heuristic(frontier):
# Helper func to find min of h (the heuristic function)
    min_h_i = 0
    if len(frontier) > 1:
        min_h = frontier[min_h_i]['heuristic']
        for i, state in enumerate(frontier):
            if state['heuristic'] < min_h:
                min_h_i = i
                min_h = state['heuristic']
    return min_h_i

def GreedySearch(init_state, goal_name):
    print("Greedy Search")
    frontier = [init_state]
    explored = []

    while len(frontier):
        state = frontier.pop(find_min_heuristic(frontier))
        state['path'].append(state['name'])
        explored.append(state['name'])

        if state['name'] == goal_name:
            print('path: ', state['path'])
            return state['weight']     
        for child in state['children']:
            if child['name'] not in explored:
                child['path'].extend(state['path'])
                child['weight'] += state['weight']
                frontier.append(child)
    return False

# Node with weight
# costs initialized with zeros to make calculations efficient.
def get_node(name, weight=0, heuristic=0):
    node = {}
    node['name'] = name
    node['children'] = []
    node['weight'] = weight
    node['heuristic'] = heuristic
    node['path'] = []

    return node

def add_child(node, name, weight=0, heuristic=0):
    node['children'].append(get_node(name, weight,heuristic))

# Building the entire search tree based on the assignment
init_state = 'Kitchener'
goal_name = 'Listowel'

tree = get_node(init_state, 0, 130)

# Children of Kitchener: Guelph, New Hamburg
add_child(tree, 'Guelph', weight=30, heuristic=160)
add_child(tree, 'New Hamburg', weight=90, heuristic=110)

# Children of Guelph: Drayton
add_child(tree['children'][0], 'Drayton', weight=100, heuristic=100)

# Children of Drayton: Listowel
add_child(tree['children'][0]['children'][0], 'Listowel', weight=100, heuristic=0)

# Children of New Hamburg: Stratford
add_child(tree['children'][1], 'Stratford', weight=25, heuristic=100)

# Children of Stratford: St. Marys, Drayton
add_child(tree['children'][1]['children'][0], 'St. Marys', weight=30, heuristic=130)
add_child(tree['children'][1]['children'][0], 'Drayton', weight=200, heuristic=100)

# Children of St. Marys: Mitchell
add_child(tree['children'][1]['children'][0]
          ['children'][0], 'Mitchell', weight=80, heuristic=100)

# Children of Mitchell: Listowel
add_child(tree['children'][1]['children'][0]['children']
          [0]['children'][0], 'Listowel', weight=100, heuristic=0)

# Children of Drayton: Listowel
add_child(tree['children'][1]['children'][0]
          ['children'][1], 'Listowel', weight=100, heuristic=0)

print('total:', GreedySearch(tree, goal_name))