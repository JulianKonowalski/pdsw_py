# from src.gui.Interface import Interface
from src.spi.SpiBus import SpiBus

if __name__ == "__main__":
    # interface: Interface = Interface()
    # interface.run()

    spibus = SpiBus()


    while True:
        print(spibus.getCarData())