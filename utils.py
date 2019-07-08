"""Sudoku utils."""

# Local imports
from config import COLS, NUM_VALUES, ROWS, RULES


def read_file(path):
    """Read txt file."""
    file = open(path, 'r')
    return file.readlines()


def get_match_groups(node):
    """Return groups of rules to which the node belongs."""
    matches = []
    for groups in RULES.values():
        for group in groups:
            for item in group:
                row, col = (int(x) for x in item.split())
                if node.row == row and node.col == col:
                    matches.append(group)
    return matches


def show_game_board(graph):
    """Show the game board with each cell value."""
    for row in range(0, ROWS):
        for col in range(0, COLS):
            value = [node.value for node in graph.nodes
                     if node.row == row and node.col == col][0]
            print(value, end=" ")
        print()


def execute(graph, index=0):
    """Execute the strategy."""
    def is_end():
        """Verify that the game can finish.

        The game may end if there are no zero values on the board.
        """
        for node in graph.nodes:
            if node.value == 0:
                return False
        return True

    def get_possible_values(adj_values):
        """Get possible values that a node can have.

        Returns values that aren't adjacent to the node.
        """
        values = []
        for value in range(1, NUM_VALUES+1):
            if value not in adj_values:
                values.append(value)
        return values

    if is_end():
        show_game_board(graph)
        exit(0)
    if index == ROWS * COLS:  # Verify if the index extrapolate dimension
        return
    node = graph.nodes[index]
    if node.value == 0:
        adj_values = [adj.value for adj in node.adjacents if adj.value > 0]
        values = get_possible_values(adj_values)
        for value in values:  # Tests each possible value for the node
            node.value = value
            execute(graph, index+1)  # Run this method for the next node
            node.value = 0
    else:
        execute(graph, index+1)  # Run this method for the next node
