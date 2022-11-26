from src.config import Config
from src.dsfd import DSFD

    

def main():
    config = Config("config.yaml")
    dsfd = DSFD(config)
    print(dsfd.detection_accuracy())

if __name__ == "__main__":
    main()