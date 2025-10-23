# from src.gui.Interface import Interface
from src.spi.SpiBus import SpiBus

if __name__ == "__main__":
    # interface: Interface = Interface()
    # interface.run()

    spibus = SpiBus()


    while True:
        carData = spibus.getCarData()
        print(carData.getData())