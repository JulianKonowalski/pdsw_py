from src.spi.SpiBus import SpiBus
from src.spi.CarData import CarData
from src.interface.Interface import Interface 

class App():

    def __init__(self) -> None:
        self.spi_bus: SpiBus = SpiBus()
        self.interface: Interface = Interface()

    def __handleButtons__(self, button_state: int) -> None:
        if button_state & 1: self.interface.previousScreen()
        if button_state & 1 << 1: self.interface.nextScreen()
        elif button_state & 1 << 2: self.interface.tickSocDeltaTimer()

    def __updateInterface__(self) -> None:
        car_data: CarData = self.spi_bus.getCarData()
        self.interface.setCarData(car_data)
        self.__handleButtons__(car_data.getValue("BUTTON_STATE"))

    def run(self) -> None:
        self.interface.run(self.__updateInterface__)