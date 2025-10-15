"""
8-Puzzle Problem
====================================================

This code defines the 8-puzzle state space and the structure
of a general search algorithm. Students must implement the
search strategy (BFS, DFS, A*) by completing the designated
sections below.

💡 Encouragement for creativity:
   You are welcome (and encouraged!) to implement your own
   search strategies.
   See the "EXTENDING WITH NEW STRATEGIES" section below.
"""

import copy
from typing import List, Tuple, Optional
from collections import deque

# ------------------------------------------------------------
# State Representation
# ------------------------------------------------------------

class PuzzleState:
    """
    Represents a state in the 8-puzzle.
    State is represented as a list of 9 integers (0 = blank tile).
    Example goal: [1, 2, 3, 4, 5, 6, 7, 8, 0]
    """

    def __init__(self, tiles: List[int], parent=None, action=None, cost=0):
        self.tiles = tiles
        self.parent = parent
        self.action = action
        self.cost = cost

    def __eq__(self, other):
        return isinstance(other, PuzzleState) and self.tiles == other.tiles

    def __hash__(self):
        return hash(tuple(self.tiles))

    def __str__(self):
        """Pretty-print 3x3 layout."""
        return "\n".join([
            f"{self.tiles[0:3]}",
            f"{self.tiles[3:6]}",
            f"{self.tiles[6:9]}"
        ])

# ------------------------------------------------------------
# Initial States (by Difficulty) and Goal State
# ------------------------------------------------------------

EASY_INITIAL_STATE = PuzzleState([
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
])  

MEDIUM_INITIAL_STATE = PuzzleState([
    1, 3, 6,
    5, 0, 2,
    4, 7, 8
])  

HARD_INITIAL_STATE = PuzzleState([
    7, 2, 4,
    5, 0, 6,
    8, 3, 1
])  

GOAL_STATE = [1, 2, 3,
              4, 5, 6,
              7, 8, 0]

# ------------------------------------------------------------
# Actions and Helper Functions
# ------------------------------------------------------------

ACTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]

def successor_function(state: PuzzleState) -> List[Tuple[str, PuzzleState]]:
    """Return list of (action, next_state) pairs reachable from the given state."""
    successors = []
    index = state.tiles.index(0)
    row, col = divmod(index, 3)

    def swap_and_create(new_row, new_col, action):
        new_tiles = copy.deepcopy(state.tiles)
        new_index = new_row * 3 + new_col
        new_tiles[index], new_tiles[new_index] = new_tiles[new_index], new_tiles[index]
        return (action, PuzzleState(new_tiles, parent=state, action=action,
                                    cost=state.cost + cost_function(state, action, new_tiles)))

    if row > 0:
        successors.append(swap_and_create(row - 1, col, "UP"))
    if row < 2:
        successors.append(swap_and_create(row + 1, col, "DOWN"))
    if col > 0:
        successors.append(swap_and_create(row, col - 1, "LEFT"))
    if col < 2:
        successors.append(swap_and_create(row, col + 1, "RIGHT"))

    return successors

def cost_function(current_state: PuzzleState, action: str, next_state_tiles: List[int]) -> int:
    """Uniform step cost of 1 for all actions."""
    return 1

def goal_test(state: PuzzleState) -> bool:
    """Check if the current state is the goal."""
    return state.tiles == GOAL_STATE

# ------------------------------------------------------------
# Heuristic Function for A* (and other informed strategies)
# ------------------------------------------------------------

def heuristic(state: PuzzleState) -> int:
    """
    TODO: Implement a heuristic function for A*.
    Must return an integer estimate of the cost from `state` to the goal.
    """
    pass 

# ------------------------------------------------------------
# General Search Algorithm
# ------------------------------------------------------------

def general_search(strategy_name: str, initial_state: PuzzleState) -> Optional[PuzzleState]:
    """
    General search algorithm framework for 8-puzzle.
    
    Parameters:
      - strategy_name: e.g., "BFS", "DFS", "A*", or your own custom name
      - initial_state: one of EASY/MEDIUM/HARD_INITIAL_STATE
    
    Students must implement the frontier logic for required strategies.
    You may also add your own strategy (see instructions below).
    """

    # --------------------------------------------------------
    # Initialization (same for all strategies)
    # --------------------------------------------------------
    explored = set()
    nodes_traversed = 0
    nodes_expanded = 0
    frontier = None

    # --------------------------------------------------------
    # STRATEGY-SPECIFIC SECTION
    # --------------------------------------------------------
    # Initialize the frontier based on the search strategy.
    # You may use deque, list, heapq, etc., as appropriate.

    if strategy_name == "BFS":
        # TODO: Initialize frontier for BFS (FIFO queue)
        pass

    elif strategy_name == "DFS":
        # TODO: Initialize frontier for DFS (LIFO stack)
        pass

    elif strategy_name == "A*":
        # TODO: Initialize frontier for A* (priority queue ordered by f(n) = g(n) + h(n))
        pass

    # --------------------------------------------------------
    # 💡 EXTENDING WITH NEW STRATEGIES
    # --------------------------------------------------------
    # To add your own strategy:
    #   1. Add a new `elif strategy_name == "NEW_STRATEGIE":` block below.
    #   2. Implement frontier initialization and node selection.
    #   3. Call your strategy in main() like: general_search("NEW_STRATEGIE", initial)

    else:
        raise ValueError(f"Unknown strategy: {strategy_name}. "
                         f"To add a new strategy, extend the STRATEGY-SPECIFIC SECTION above.")

    # --------------------------------------------------------
    # General Search Loop
    # --------------------------------------------------------
    while frontier:
        # STRATEGY-SPECIFIC: Remove a node from the frontier
        if strategy_name == "BFS":
            # TODO: Pop from the left (FIFO)
            node = None
        elif strategy_name == "DFS":
            # TODO: Pop from the right (LIFO)
            node = None
        elif strategy_name == "A*":
            # TODO: Pop the node with lowest f(n) = cost + heuristic
            node = None

        # 💡For custom strategies, add your pop logic here

        if node is None:
            raise RuntimeError("You must assign `node` in the strategy-specific pop step.")

        nodes_traversed += 1
        print(f"\nTraversed Node #{nodes_traversed}:\n{node}\n")

        if goal_test(node):
            print("\n Goal found!")
            print(f"Total Nodes Traversed: {nodes_traversed}")
            print(f"Total Nodes Expanded: {nodes_expanded}")
            return node

        explored.add(node)

        # Expand node
        successors = successor_function(node)
        nodes_expanded += 1
        print(f"Expanded Node #{nodes_expanded} — Generated {len(successors)} successors.\n")

        for action, child in successors:
            if child not in explored:
                # STRATEGY-SPECIFIC: Add child to frontier
                if strategy_name == "BFS" or strategy_name == "DFS":
                    # TODO: Append child to frontier
                    pass
                elif strategy_name == "A*":
                    # TODO: Add child with priority = child.cost + heuristic(child)
                    pass

                # 💡For custom strategies, handle insertion here

    print("Search failed. No solution found.")
    print(f"Total Nodes Traversed: {nodes_traversed}")
    print(f"Total Nodes Expanded: {nodes_expanded}")
    return None

# ------------------------------------------------------------
# Helper: Reconstruct Solution Path
# ------------------------------------------------------------

def reconstruct_path(state: PuzzleState) -> List[str]:
    """Reconstruct the sequence of actions from initial to goal."""
    path = []
    while state.parent is not None:
        path.append(state.action)
        state = state.parent
    path.reverse()
    return path

# ------------------------------------------------------------
# Main
# ------------------------------------------------------------

if __name__ == "__main__":
    # Choose your puzzle difficulty
    initial = EASY_INITIAL_STATE  # Try MEDIUM_INITIAL_STATE or HARD_INITIAL_STATE too!

    print("Initial State:")
    print(initial)
    print("\nGoal State:")
    print(GOAL_STATE)

    # Choose your strategy: "BFS", "DFS", "A*", or your own!
    result = general_search("BFS", initial)

    if result:
        path = reconstruct_path(result)
        print("\n Solution found!")
        print("Number of steps:", len(path))
        print("Actions:", path)
        print("\nFinal state:")
        print(result)
    else:
        print(" No solution found.")