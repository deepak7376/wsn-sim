# import pyyaml module
import yaml
from yaml.loader import SafeLoader


class YamlParser:
    @staticmethod
    def load_yaml(path):    
        # Open the file and load the file
        with open(path) as f:
            data = yaml.load(f, Loader=SafeLoader)
            return data


class Config:
    def __init__(self, path) -> None:
        self.config_data = YamlParser.load_yaml(path)

    @property
    def get_no_of_nodes(self):
        return self.config_data['NO_OF_NODES']

    @property
    def get_area(self):
        return self.config_data['X_MAX'], self.config_data['Y_MAX']

    @property
    def get_tx_range(self):
        return self.config_data['TX_RANGE_OF_NODE']

    @property
    def get_remaining_power_of_node(self):
        return self.config_data['INITIAL_POWER']


if __name__ == "__main__":
    c = Config("config.yaml")
    print(c.get_no_of_nodes, c.get_area, c.get_tx_range)