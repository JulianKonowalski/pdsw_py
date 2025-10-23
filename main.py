import logging
from src.gui.Interface import Interface

LOGGER: logging.Logger = logging.getLogger(__name__)
logging.basicConfig(filename="interface.log", level=logging.INFO)

if __name__ == "__main__":
    LOGGER.info("Starting main")

    interface: Interface = Interface()
    interface.run()