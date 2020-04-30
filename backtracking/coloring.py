"""
    Graph Coloring also called "m coloring problem"
    consists of coloring given graph with at most m colors
    such that no adjacent vertices are assigned same color
"""


def util_color(graph, max_colors, colored_vertices, index):
    """ 
    Pseudo-Code

    BaseCase:
    1. Check if coloring is complete 
        1.1 If complete return True (meaning that we successfully colored graph)

    RecursiveStep:
    2. Itterates over each color:
        Check if current coloring is valid:
            2.1. Color given vertex
            2.2. Do recursive call check if this coloring leads to solving problem
            2.4. if current coloring leads to solution return
            2.5. Uncolor given vertex

    >>> graph = [[0, 1, 0, 0, 0],
    ...          [1, 0, 1, 0, 1],
    ...          [0, 1, 0, 1, 0],
    ...          [0, 1, 1, 0, 0],
    ...          [0, 1, 0, 0, 0]]
    >>> total_colors = 3
    >>> colored_vertices = [0, 1, 0, 0, 0]
    >>> index = 3
    
    >>> util_color(graph, max_colors, colored_vertices, index)
    True

    >>> total_colors = 2
    >>> util_color(graph, max_colors, colored_vertices, index)
    False
    """


def color(graph, max_colors):
    """ 
    Wrapper function to call subroutine called util_color
    which will either return True or False.
    If True is returned colored_vertices list is filled with correct colorings
        
    >>> graph = [[0, 1, 0, 0, 0],
    ...          [1, 0, 1, 0, 1],
    ...          [0, 1, 0, 1, 0],
    ...          [0, 1, 1, 0, 0],
    ...          [0, 1, 0, 0, 0]]

    >>> total_colors = 3
    >>> color(graph, total_colors)
    (True, [1, 2, 1, 3, 1])

    >>> total_colors = 2
    >>> color(graph, total_colors)
    (False, None)
    """
    colored_vertices = [-1] * len(graph)

    if util_color(graph, max_colors, colored_vertices, 0):
        return True, colored_vertices

    return False, None
