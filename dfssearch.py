# Depth-first search
from os import stat

def DFS(init_state, goal_name):

    frontier = [init_state]
    explored = []
    
    for item in frontier:
        state = item
        # state = frontier.pop() # dequeue
        explored.append(state['name'])
        
        
        state = frontier.index()
        
        
        if state['name'] == goal_name:
            return True
        for child in state['children']:
            if child['name'] not in explored:
                # enqueue: insert node at the beginning
                frontier.insert(0, child)
    return False

    # while len(frontier):
    #     state = frontier.index(idx)
    #     idx += 1
    #     # state = frontier.pop() # dequeue
    #     explored.append(state['name'])
        
        
    #     state = frontier.index()
        
        
    #     if state['name'] == goal_name:
    #         return True
    #     for child in state['children']:
    #         if child['name'] not in explored:
    #             # enqueue: insert node at the beginning
    #             frontier.insert(0, child)
    # return False


        