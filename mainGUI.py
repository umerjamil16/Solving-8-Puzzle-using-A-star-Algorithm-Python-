'''
Qazi Umer Jamil
317920
NUST RIME SMME
'''

# All the libraries required
import pygame #for GUI framework
import time
import copy 

#Import GUI related functions/vars from guiFuncs.file
from guiFuncs import convertArray, displayPuzzzle, displayGoalState, displayStartState, displayTitles, diplayResult
from guiFuncs import screen, clock, done

#Import A* - algorithms related functions/vars from algoFuncs.file
from algoFuncs import puzzleSize, exploredStates
from algoFuncs import getInputState, heuristic1, checkState, genChildNodes, printSTATE, heuristic2
from algoFuncs import genPossibleMoves, getBarPos, printArrow, Node, sortSecond, checkIfExplored

startState = []
goalState = [
        [1,2,3], 
        [4,5,6], 
        [7,8,0]]

print("8 Puzzle Problem using A*- Search") 

# Get input from the user
'''

print("Please input Goal State row by row")
goalState = getInputState()
'''
print("Please input Initial State row by row")
startState = getInputState()

# Copy startState so that we can continously display it on PyGame window
startStateInitial = copy.deepcopy(startState)

#Print user entered GOAL state
print("Goal State")
printSTATE(goalState)

#Print user entered START state
print("Start State")
printSTATE(startState)

# level count is basically the aggregated step cost or depth of tree
level_count = 1

#Here check if start State is already reached
# log the explored states
exploredStates.append(startState)

#Time step for moving the block
timeStep = 0.1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Close the program incase the window is closed
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            #Close the program if Escape Key is pressed
            done = True
    #Based on the last explored state, generate a frontier of child nodes
    childNodes = genChildNodes(startState, goalState, level_count)

    #Sort the frontier w.r.t decreasing Net Cost
    childNodes.sort(key = sortSecond, reverse = False) 

    #Initialize the next start state
    startState = []

    #Iterate over the frontier, and pick a state one by one
    for i in range(len(childNodes)):
        #If the picked child state from frontier is not in the explored set,
        if checkIfExplored(childNodes[i][2]):
            #Choose it as the next start stage for next iteration
            startState = childNodes[i][2]
            #Also, append it to the Explored State set
            exploredStates.append(startState)
            #Break from the for loop, since the next start state is found
            break

    #If no next start state found in the previous for loop, that means
    #all set of possible states have been explored
    #This happends due to the odd number of inversions in the input
    #arrangements of puzzle
    if len(startState) ==0:
        print("PUZZLE NOT SOLVEABLE")
        print("ODD NUMBERS OF INVERSIONS IN THE GIVEN INPUT STATE")
        print("PLEASE ENTER A DIFFERENT ARRANGEMENT")
        #Break from the outer while loop if no startState exist
        break

    #Print the current selected state to the terminal
    printArrow()
    printSTATE(startState)
    print("Depth of tree: " + str(level_count))
    
    #For displaying the Current Selected State, Goal State, and Inital State in PyGame Window

    #Fill the screen with white background
    screen.fill((255, 255, 255))
    #Display titles, inital, current and goal state puzzle arrangements
    displayTitles()
    displayPuzzzle(startState)
    displayStartState(startStateInitial)
    displayGoalState(goalState)
    #Update the display window
    pygame.display.update()
    clock.tick(60) #minimum 40 frames per second.

    #Wait till next iteration
    time.sleep(timeStep)

    #Check if the current selected start state is equal to the goal state
    if checkState(startState, goalState):
        print("GOAL STATE REACHED")
        break

    #Keep track of the depth of tree
    level_count = level_count+1

#wait of 10 sec before quitting pygame window
time.sleep(10)