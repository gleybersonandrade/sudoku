"""Sudoku graph."""

# Local imports
from config import COLS, ROWS
from utils import get_match_groups


class Graph():
    """Class to manage Graph Model."""

    def __init__(self, values):
        """Create a new graph.

        Parameters:
            values (list): values of a new graph.

        """
        self.nodes = []
        for row in range(0, ROWS):
            for col in range(0, COLS):
                value = int(values[row][col])
                node = Node(value, row, col)
                self.nodes.append(node)  # Create each graph node
        for node in self.nodes:
            groups = get_match_groups(node)
            for group in groups:
                for item in group:
                    row, col = (int(x) for x in item.split())
                    if node.row == row and node.col == col:
                        continue  # Continue if the item is the node itself
                    target = self.find_node(row, col)
                    node.add_adjacent(target)  # Add adjacents to graph node

    def find_node(self, row, col):
        """Find a node by row and col."""
        for node in self.nodes:
            if node.row == row and node.col == col:
                return node
        return None


class Node():
    """Class to manage Node Model."""

    def __init__(self, value, row, col):
        """Create a new node.

        Parameters:
            value (integer): value of a new node.
            row (integer): row that new node belongs to.
            col (integer): column that new node belongs to.

        """
        self.value = value
        self.row = row
        self.col = col
        self.adjacents = []

    def add_adjacent(self, node):
        """Add an ajacent to node."""
        for adjacent in self.adjacents:
            if node == adjacent:  # Discards if the node already exists
                return
        if isinstance(node, Node):  # Add only if the node is a Node instance
            self.adjacents.append(node)
