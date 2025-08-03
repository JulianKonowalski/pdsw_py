from src.spi.CarData import CarData

try:
    import spidev
except ImportError:
    import mock.mockSpidev as spidev

k_spi_bus       = 0
k_spi_rate      = 9600
k_spi_mode      = 0  
k_spi_device    = 0

class SpiBus:

    def __init__(self) -> None:
        buffer_size: int = len(CarData.getDataframe())
        self.dummy_data = [0x00 for i in range(buffer_size)]
        self.spi = spidev.SpiDev()
        self.spi.open(k_spi_bus, k_spi_device)
        self.spi.max_speed_hz = k_spi_rate
        self.spi.mode = k_spi_mode

    def __normalize__(self, car_data: CarData) -> CarData:
        temp: int = car_data.getValue("TEMP")
        temp_normalized: int = temp if temp < 128 else temp - 256 

        curr: int = int(car_data.getValue("CURR_MSB") << 8 | car_data.getValue("CURR_LSB"))
        curr_normalized: int =  curr if curr < 128 else curr - 256 
        
        volt_normalized: float = int(car_data.getValue("VOLT_MSB") << 8 | car_data.getValue("VOLT_LSB")) * 0.1
        pwr_output: float = curr_normalized * volt_normalized

        car_data.setValue("TEMP", temp_normalized)
        car_data.setValue("CURR", curr_normalized)
        car_data.setValue("VOLT", volt_normalized)
        car_data.setValue("PWR_OUTPUT", pwr_output)

        return car_data

    def getCarData(self) -> CarData:
        spi_response: list = self.spi.xfer2(self.dummy_data)
        car_data: CarData = CarData()
        dataframe: dict = CarData.getDataframe()
        for idx, key in enumerate(dataframe):
            car_data.setValue(key, spi_response[idx])
        return self.__normalize__(car_data)
