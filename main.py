from collections import defaultdict
from heapq import heappush, heappop 
from math import sqrt

def prim(graph):
    def prim_helper(start, visited):
        frontier = []
        heappush(frontier, (0, start, start))
        tree = set()
        while frontier:
            weight, node, parent = heappop(frontier)
            if node in visited:
                continue
            visited.add(node)
            tree.add((weight, node, parent))
            for neighbor, w in graph[node]:
                if neighbor not in visited:
                    heappush(frontier, (w, neighbor, node))
        tree.remove((0, start, start))  # remove dummy edge
        return tree

    visited = set()
    trees = []
    for node in graph:
        if node not in visited:
            trees.append(prim_helper(node, visited))
    return trees

def test_prim():    
    graph = {
            's': {('a', 4), ('b', 8)},
            'a': {('s', 4), ('b', 2), ('c', 5)},
            'b': {('s', 8), ('a', 2), ('c', 3)}, 
            'c': {('a', 5), ('b', 3), ('d', 3)},
            'd': {('c', 3)},
            'e': {('f', 10)}, # e and f are in a separate component.
            'f': {('e', 10)}
        }

    trees = prim(graph)
    assert len(trees) == 2
    # since we are not guaranteed to get the same order
    # of edges in the answer, we'll check the size and
    # weight of each tree.
    len1 = len(trees[0])
    len2 = len(trees[1])
    assert min([len1, len2]) == 2
    assert max([len1, len2]) == 5

    sum1 = sum(e[0] for e in trees[0])
    sum2 = sum(e[0] for e in trees[1])
    assert min([sum1, sum2]) == 10
    assert max([sum1, sum2]) == 12
    ###



def mst_from_points(points):
    """
    Return the MST for a list of points using Prim's algorithm
    and Euclidean distance as edge weights.
    """
    # Build the graph as an adjacency list
    graph = defaultdict(set)
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            p1 = points[i]
            p2 = points[j]
            dist = euclidean_distance(p1, p2)
            graph[p1[0]].add((p2[0], dist))
            graph[p2[0]].add((p1[0], dist))

    # Run Prim’s algorithm on the graph (it's fully connected, so one component)
    trees = prim(graph)
    return list(trees[0])


def euclidean_distance(p1, p2):
    return sqrt((p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def test_euclidean_distance():
    assert round(euclidean_distance(('a', 5, 10), ('b', 7, 12)), 2) == 2.83

def test_mst_from_points():
    points = [('a', 5, 10), #(city_name, x-coord, y-coord)
              ('b', 7, 12),
              ('c', 2, 3),
              ('d', 12, 3),
              ('e', 4, 6),
              ('f', 6, 7)]
    tree = mst_from_points(points)
    # check that the weight of the MST is correct.
    assert round(sum(e[0] for e in tree), 2) == 19.04


