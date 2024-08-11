from node import *

# RoutingProtocol Base Class
class RoutingProtocol:
    def establish_route(self, node: Node, destination: Node) -> List[Node]:
        raise NotImplementedError("This method should be overridden by subclasses")

    def route_packet(self, node: Node, destination: Node, data: str):
        raise NotImplementedError("This method should be overridden by subclasses")


# Flooding Protocol
class Flooding(RoutingProtocol):
    def establish_route(self, node: Node, destination: Node) -> List[Node]:
        return node.neighbors

    def route_packet(self, node: Node, destination: Node, data: str):
        neighbors = self.establish_route(node, destination)
        for neighbor in neighbors:
            node.send_data(data, neighbor)


# AODV Protocol (Simplified)
class AODV(RoutingProtocol):
    def establish_route(self, node: Node, destination: Node) -> List[Node]:
        return [destination] if destination in node.neighbors else []

    def route_packet(self, node: Node, destination: Node, data: str):
        route = self.establish_route(node, destination)
        if route:
            node.send_data(data, route[0])
        else:
            print(f"No route found from Node {node.id} to Node {destination.id}")

class DSR(RoutingProtocol):
    def __init__(self):
        # Cache to store discovered routes
        self.route_cache = {}

    def establish_route(self, source: Node, destination: Node) -> List[Node]:
        # If a route exists in the cache, use it
        if (source.id, destination.id) in self.route_cache:
            return self.route_cache[(source.id, destination.id)]

        # Otherwise, initiate route discovery
        route = self.route_discovery(source, destination)
        if route:
            self.route_cache[(source.id, destination.id)] = route
        return route

    def route_discovery(self, source: Node, destination: Node) -> List[Node]:
        # Flooding the network with route requests (RREQ)
        visited = set()
        path = []
        route_found = self._flood_rreq(source, destination, visited, path)
        return path if route_found else []

    def _flood_rreq(self, current_node: Node, destination: Node, visited: set, path: List[Node]) -> bool:
        visited.add(current_node.id)
        path.append(current_node)

        if current_node.id == destination.id:
            return True  # Route to the destination found

        for neighbor in current_node.neighbors:
            if neighbor.id not in visited:
                if self._flood_rreq(neighbor, destination, visited, path):
                    return True

        path.pop()  # Backtrack if destination is not reached
        return False

    def route_packet(self, node: Node, destination: Node, data: str):
        route = self.establish_route(node, destination)
        if route:
            for hop in route:
                node.send_data(data, hop)
        else:
            print(f"No route found from Node {node.id} to Node {destination.id}")