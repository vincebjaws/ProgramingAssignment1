"""
Author: Vince Bjazevic
Class: CPSC 481
Due Date: Sept 28, 2023
"""
class ticTacToeState:
    def __init__(self,state,player,parent=None):
        self.state = state
        self.parent = parent
        self.player = player
        self.children = []

#implement bfs on tictactoe(state,player) object
def bfs(root_node):
    #create queue and visited list
    visited = []
    queue = []
    queue.append(root_node)

    #while queue is not empty traverse laterally
    while queue:
        #remove root node
        state_to_examine = queue.pop(0)
        #check if not a repeating board state
        board_state = state_to_examine.state
        if board_state in visited:
            continue
        visited.append(state_to_examine)
        #check if tree ends do to winner
        if end_state(state_to_examine.state):
            continue
        #print current state
        print("current node:")
        print_current_state(root_node.state)
        #get children of state
        state_to_examine.children = create_new_states(state_to_examine.state, state_to_examine.player)
        for i in range(len(state_to_examine.children)):
            queue.append(state_to_examine.children[i])
        print("current adjecent node(s):")
        print_adj_states(state_to_examine.children)

#implement dfs on tictactoe(state, player)
def dfs(root_node):
    #create queue and visited list
    visited = []
    queue = []

    #while queue is not empty traverse laterally
    while queue:
        #remove first state
        state_to_examine = queue.pop(0)
        #check if not a repeating board state
        board_state = state_to_examine.state
        if board_state in visited:
            continue
        visited.append(state_to_examine)
        #check if tree ends do to winner
        if end_state(state_to_examine.state):
            continue
        #print current state
        print("current node:")
        print_current_state(root_node.state)
        #get children of state
        state_to_examine.children = create_new_states(state_to_examine.state, state_to_examine.player)
        for i in range(len(state_to_examine.children)):
            queue.append(state_to_examine.children[i])
        print("current adjecent node(s):")
        print_adj_states(state_to_examine.children)

    #traverse one first child first then so on

#check if winning state
def end_state(test_end_state):
    if test_end_state[0] != " " and test_end_state[0] == test_end_state[1] and test_end_state[0] == test_end_state[2]:
        print("case 1")
        return True
    elif test_end_state[3] != " " and test_end_state[3] == test_end_state[4] and test_end_state[3] == test_end_state[5]:
        print("case 2")
        return True
    elif test_end_state[6] != " " and test_end_state[6] == test_end_state[7] and test_end_state[6] == test_end_state[8]:
        print("case 3")
        return True
    elif test_end_state[0] != " " and test_end_state[0] == test_end_state[3] and test_end_state[0] == test_end_state[6]:
        print("case 4")
        return True 
    elif test_end_state[1] != " " and test_end_state[1] == test_end_state[4] and test_end_state[1] == test_end_state[7]:
        print("case 5")
        return True
    elif test_end_state[2] != " " and test_end_state[2] == test_end_state[5] and test_end_state[2] == test_end_state[8]:
        print("case 6")
        return True
    elif test_end_state[0] != " " and test_end_state[0] == test_end_state[4] and test_end_state[0] == test_end_state[8]:
        print("case 7")
        return True
    elif test_end_state[2] != " " and test_end_state[2] == test_end_state[4] and test_end_state[6] == test_end_state[2]:
        print("case 8")
        return True
    else:
        print("case 9")
        return False

#print current state
def print_current_state(cur_state):
    for i in range(9):
        if i%3 == 0 and i != 0:
            print("")
        print("|", cur_state[i],"|", end="")
    print("",end="\n\n")

#print adj states
def print_adj_states(states_to_be_printed):
    for states in range(len(states_to_be_printed)):
        print_current_state(states_to_be_printed[states].state)


#create adjecent states
def create_new_states(cur_state, player):
    child_states = []
    next_player = player
    #switch player
    if next_player == "X":
        next_player = "O"
    else:
        next_player = "X"
    #iterate through all adj states
    for i in range(9):
        if cur_state[i] == " ":
            #create new state
            state_to_be_added = cur_state.copy()
            state_to_be_added[i] = player
            child_states.append(ticTacToeState(state_to_be_added, next_player, parent=cur_state))
    return child_states
             

def main():

    start = ticTacToeState([" ", " ", " ", " ", " ", " ", " ", " ", " "], "O")





    """
    # TESTS

    #Test create new state
    states_to_be_printed = create_new_states(start.state, "O")

    #Test prints
    print("current node:")
    print_current_state(start.state)
    print("current adjecent node(s):")
    print_adj_states(states_to_be_printed)


    
    test_state = ticTacToeState(["O","X","O","O", "X", "X", "O"," ", " "],"O")

    #test winning state
    if(end_state(test_state.state)):
        print("Winning state")
        print_current_state(test_state.state)
    else:
        print("Not winning state")
        print_current_state(test_state.state)
    """
    #test bfs
    test_state = ticTacToeState(["O","X","O","O", "X", "X", " "," ", " "],"O")
    bfs(test_state)
if __name__ == "__main__":
    main()  