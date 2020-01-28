'''
Qazi Umer Jamil
317920
NUST RIME SMME
'''

import time
import copy 

puzzleSize = 3

#Puzzle size
puzzleSize = 3

#Initialize the set of explored states
exploredStates = []


def getInputState():
    rslt = [
        [1,2,3], 
        [4,5,6], 
        [7,8,0]]

    x, y, z = input("Enter first row: ").split() 
    if x == "_":
        x =0
    if y == "_":
        y =0
    if z == "_":
        z=0
    rslt[0][0] = int(x)
    rslt[0][1] = int(y)
    rslt[0][2] = int(z)

    x, y, z = input("Enter 2nd row: ").split() 
    if x == "_":
        x =0
    if y == "_":
        y =0
    if z == "_":
        z=0
    rslt[1][0] = int(x)
    rslt[1][1] = int(y)
    rslt[1][2] = int(z)

    x, y, z = input("Enter 3rd row: ").split() 
    if x == "_":
        x =0
    if y == "_":
        y =0
    if z == "_":
        z=0
    rslt[2][0] = int(x)
    rslt[2][1] = int(y)
    rslt[2][2] = int(z)

    return rslt

def checkIfExplored(child):
    for i in range(len(exploredStates)):
        if child == exploredStates[i]:
            return 0
    return 1

#Heuristic based on manhattan distace metric
def heuristic1(startState, goalState):
     cdist = 0
     for i in range(len(startState)):
          for j in range(len(startState)):
               for k in range(len(goalState)):
                    for l in range(len(goalState)):
                         if (startState[i][j] == goalState[k][l]) and startState[i][j] != 0:
                              cdist = cdist + abs(i-k) + abs(j- l)

     return cdist

#Heuristic based on the no of misplaced tiles in a given puzzle arrangements
def heuristic2(start,goal):
        """ Calculates the different between the given puzzles """
        temp = 0
        for i in range(len(start)):
            for j in range(len(start)):
                if start[i][j] != goal[i][j] and start[i][j] != 0:
                    temp += 1
        return temp

#Check whether the chils state is equal to goal state
def checkState(child, goal):
    if child == goal:
        return 1
    else: 
        return 0

#Generate child nodes
def genChildNodes(startState, goalState, curSTEP_COST):
    parentSTATE = startState #The startState of each level will become parentState
    barX, barY = getBarPos(parentSTATE)
    validMoves = genPossibleMoves(barX, barY)
    # based on valid moves, we will manupulate the/copy parentSTATE and 
    # gen CHILD NODES
    #childNODES =  Q.PriorityQueue()
    childNODES = []
#    print("Valid Moves: " + str(validMoves))
    for i in range(0,len(validMoves)):
        #Copy the parent states as in Python variables are indexly stores
        childSTATE = copy.deepcopy(parentSTATE) 
        
        #Get position of bar '_'
        move_x = validMoves[i][0]
        move_y = validMoves[i][1]

        #To swap '_' and the respective block
        temp0 = childSTATE[move_x][move_y] 
        temp1 = childSTATE[barX][barY]
        childSTATE[move_x][move_y] = temp1
        childSTATE[barX][barY] = temp0

        # Heuristic Calculation based on the number of misplaced tiles
        hVal = heuristic1(childSTATE, goalState)

        #Net cost calculation
        fval = hVal + curSTEP_COST

        #Create a Child Node with a State, parentState, and Cost taken to reach the state
        child_NODE = Node(parentSTATE, childSTATE, fval)

        #Append the child node to ChilNODES array (frontier)
        childNODES.append(child_NODE)
    
    #Return the frontier
    return childNODES

#Print States in the terminal
def printSTATE(a):
    print("_____________")
    for i in range(len(a)):
        for j in range(len(a[i])):
            if (str(a[i][j]) != "0"):
                print("| " + str(a[i][j]) , end=" ")
            else:
                print("| " + "_" , end=" ")
        print("|")
    print("_____________")

# Function to generate valid possible moves
def genPossibleMoves(x, y):
    moves = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
    validMoves = []
    for i in range(len(moves)):
        if not (moves[i][0] >= puzzleSize or moves[i][0] < 0 or moves[i][1] >= puzzleSize or moves[i][1] < 0):
            validMoves.append(moves[i])
    #return the valid moves
    return validMoves

# Get '_' Bar position
def getBarPos(a):
    x = 0
    y = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == 0:
                x = i
                y = j
    return x, y

#Print Arrow (for terminal)
def printArrow():
    print("\n")
    print("  | ")
    print(" \\'/ \n")

# Generic Node function
def Node(PARENT, STATE, fVal):
    #Initialize the node with the STATE, STEP_COST of the node and the calculated fvalue
    PARENT = PARENT #[0]
    STATE = STATE #[1]
    fVal = fVal  #[2]
    return fVal, PARENT, STATE
    #we can use array indexing for accessing returning val

#For sorting
def sortSecond(val): 
    return val[0] 


