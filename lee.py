from collections import deque

def lee_algorithm(matrix, start, end):
    queue = deque()
    visited = set()
    distance = {start: 0}
    prev = {}

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.popleft()

        # Explore the neighboring nodes
        for neighbor in get_neighbors(matrix, node):
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[node] + 1
                prev[neighbor] = node
                queue.append(neighbor)

            if neighbor == end:
                return get_shortest_path(prev, start, end)

    return None

def get_neighbors(matrix, node):
    neighbors = []
    row, col = node

    # Check the top neighbor
    if row > 0 and matrix[row - 1][col] != 1:
        neighbors.append((row - 1, col))

    # Check the bottom neighbor
    if row < len(matrix) - 1 and matrix[row + 1][col] != 1:
        neighbors.append((row + 1, col))

    # Check the left neighbor
    if col > 0 and matrix[row][col - 1] != 1:
        neighbors.append((row, col - 1))

    # Check the right neighbor
    if col < len(matrix[0]) - 1 and matrix[row][col + 1] != 1:
        neighbors.append((row, col + 1))

    return neighbors

def get_shortest_path(prev, start, end):
    path = []
    node = end

    while node != start:
        path.append(node)
        node = prev[node]

    path.append(start)
    path.reverse()

    return path

# Testing the implementation
matrix = [
    [-1, 0, -1, 0, -1, 0, 0, -1],
    [-1,-2, -1, 0, -1, 0, 0, -1],
    [-1, 0, -1, 0, -1,-1, 0, -1],
    [-1, 0,  0, 0,  0, 0, 0, -1],
    [-1, 0, -1,-1, -1, 0, 0, -1],
    [-1, 0,  0, 0,  0, 0, 0, -1],
    [-1, 0, -1, 0, -1, 0,-2, -1],
    [-1, 0, -1, 0, -1,-1, 0, -1]
]
start = (1, 1)
end = (6, 6)

shortest_path = lee_algorithm(matrix, start, end)
print(shortest_path)  