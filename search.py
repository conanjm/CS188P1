# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and Pieter 
# Abbeel in Spring 2013.
# For more info, see http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    def constructNode(parent, child):
        nodeDirection = child[1]
        print ('nodeDirection: ' + str(nodeDirection))
        parentPath = parent[1]
        print ('parentPath: ' + str(parentPath))

        parentCost = parent[2]
        childCost = child[2]

        newDirection = nodeDirection.lower()[:1]
        print('newDirection: ' + newDirection)
        newPath = parentPath + newDirection + ','
        print('New path: ' + str(newPath))
        
        cost = parentCost + childCost

        newNode = ((child[0]), newPath, cost)
        return newNode


    #node ((x, y),path,cost)
    def insertIntoFringe(node, fringe):
        fringe.push(node)
        return fringe

    def graphSearch(problem, fringe):

        from game import Directions
        s = Directions.SOUTH
        w = Directions.WEST
        n = Directions.NORTH
        e = Directions.EAST

        closed = {}
        fringe =insertIntoFringe((problem.getStartState(), '', 0), fringe)
        print "Start:", (problem.getStartState(), '', 0)

        while True:
            if fringe.isEmpty():
                return []

            node = fringe.pop()
            print('Node: ' + str(node))

            if problem.isGoalState(node[0]):
                result = [node[1][:-1]]
                print('Result: ' + str(result).replace("'", ""))
                return eval(str(result).replace("'", ""))
               
            if node[0] not in closed:

                closed[node[0]] = node
                print('Adding node to closed: ' + str(node[0]))
                for childNode in problem.getSuccessors(node[0]):
                    newNode = constructNode(node, childNode)
                    print('Adding child node: ' + str(newNode))
                    fringe = insertIntoFringe(newNode, fringe)
                    print('=======================================')

            #raw_input('=======================================================================')

    fringe = util.Queue()
    return graphSearch(problem, fringe)    

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
