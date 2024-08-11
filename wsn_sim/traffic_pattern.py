from node import *
from routing_protocol import RoutingProtocol

# TrafficPattern Base Class
class TrafficPattern:
    def generate_traffic(self, nodes: List[Node], base_station: BaseStation):
        raise NotImplementedError("This method should be overridden by subclasses")


# # Example TrafficPattern: Periodic
# class PeriodicTraffic(TrafficPattern):
#     def generate_traffic(self, nodes: List[Node], base_station: BaseStation):
#         for node in nodes:
#             if node.energy > 0:
#                 data = f"Data from Node {node.id}"
#                 node.send_data(data, base_station)
# Updated TrafficPattern: PeriodicTraffic using the selected routing protocol
class PeriodicTraffic(TrafficPattern):
    def __init__(self):
        self.routing_protocol = None

    def set_routing_protocol(self, routing_protocol: RoutingProtocol):
        self.routing_protocol = routing_protocol

    def generate_traffic(self, nodes: List[Node], base_station: BaseStation):
        for node in nodes:
            if node.energy > 0:
                data = f"Data from Node {node.id}"
                # Use the routing protocol to send data to the base station
                self.routing_protocol.route_packet(node, base_station, data)