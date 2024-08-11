from typing import List, Tuple
import random


# Node Class
class Node:
    def __init__(self, node_id: int, position: Tuple[int, int], energy: float = 100.0):
        self.id = node_id
        self.position = position
        self.energy = energy
        self.neighbors: List[Node] = []
        self.packets_sent = 0
        self.packets_received = 0
        self.packets_missed = 0
        self.routing_table = {}

    def send_packet(self):
        self.packets_sent += 1

    def receive_packet(self):
        self.packets_received += 1

    def miss_packet(self):
        self.packets_missed += 1

    def send_data(self, data: str, destination: 'Node'):
        if self.energy > 0:
            self.energy -= 0.5  # Energy cost for sending data
            print(f"Node {self.id} sent data to Node {destination.id}: {data}")
            destination.receive_data(data)
        else:
            print(f"Node {self.id} has no energy left.")

    def receive_data(self, data: str):
        if self.energy > 0:
            self.energy -= 0.2  # Energy cost for receiving data
            print(f"Node {self.id} received data: {data}")
        else:
            print(f"Node {self.id} has no energy left.")

    def move(self, mobility_enabled: bool):
        if mobility_enabled and self.energy > 0:
            new_position = (self.position[0] + random.randint(-1, 1), self.position[1] + random.randint(-1, 1))
            self.position = new_position
            self.energy -= 0.1  # Energy cost for moving
            print(f"Node {self.id} moved to {self.position}.")
        elif not mobility_enabled:
            print(f"Node {self.id} remains stationary at {self.position}.")
        else:
            print(f"Node {self.id} has no energy left.")

    def update_energy(self):
        pass

# BaseStation Class
class BaseStation(Node):
    def __init__(self, node_id: int, position: Tuple[int, int]):
        super().__init__(node_id, position)

    def receive_data(self, data: str):
        print(f"BaseStation {self.id} received data: {data}")