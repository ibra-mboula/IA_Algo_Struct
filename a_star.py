# astar.py
import heapq

class AStar:
    def __init__(self, nodes):
        self.nodes = nodes

    def heuristic(self, node, goal):
        # Simple Euclidean distance heuristic
        return ((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2) ** 0.5

    def find_path(self, start, goal):
        open_set = []
        closed_set = set()

        start_node = next(node for node in self.nodes if node.id == start)
        goal_node = next(node for node in self.nodes if node.id == goal)

        heapq.heappush(open_set, (0, start_node))
        came_from = {start_node: None}
        cost_so_far = {start_node: 0}

        while open_set:
            current_cost, current_node = heapq.heappop(open_set)

            if current_node.id == goal:
                # Reconstruct path
                path = []
                while current_node is not None:
                    path.insert(0, current_node.id)
                    current_node = came_from[current_node]
                return path

            closed_set.add(current_node)

            for neighbor in current_node.neighbors:
                if neighbor in closed_set:
                    continue

                new_cost = cost_so_far[current_node] + 1  # Assuming a constant cost for simplicity

                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + self.heuristic(neighbor.id, goal)
                    heapq.heappush(open_set, (priority, neighbor))
                    came_from[neighbor] = current_node

        return None  # No path found
