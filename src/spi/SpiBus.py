try: import spidev
except ImportError: import mock.mockSpidev as spidev

from src.spi.CarData import CarData

SPI_BUS: int        = 0
SPI_RATE: int       = 9600
SPI_MODE: int       = 0  
SPI_DEVICE: int     = 0
BUFFER_SIZE: int    = 12

class SpiBus:

    def __init__(self) -> None:
        self.dummy_data = [0x00 for i in range(BUFFER_SIZE)]
        self.spi = spidev.SpiDev()
        self.spi.open(SPI_BUS, SPI_DEVICE)
        self.spi.max_speed_hz = SPI_RATE
        self.spi.mode = SPI_MODE

    def getCarData(self) -> CarData:
        return CarData(self.spi.xfer2(self.dummy_data))
    
        # spi_response: list[int] = self.spi.xfer2(self.dummy_data)
        # car_data: CarData = CarData()
        # dataframe: dict = CarData.getDataframe()
        # for idx, key in enumerate(dataframe):
        #     car_data.setValue(key, spi_response[idx])
        # return car_data