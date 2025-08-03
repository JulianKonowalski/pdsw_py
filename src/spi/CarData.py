k_car_dataframe: dict = {
    "BUTTON_STATE"  : 0,
    "DIAL_0"        : 0,
    "DIAL_1"        : 0,
    "DIAL_2"        : 0,
    "SOC"           : 0,
    "TEMP"          : 0,
    "CURR_MSB"      : 0,
    "CURR_LSB"      : 0,
    "VOLT_MSB"      : 0,
    "VOLT_LSB"      : 0,
    "MAP"           : 0,
    "PWR"           : 0
}

class CarData:

    def __init__(self) -> None:
        self.data: dict = dict.copy(k_car_dataframe)

    def getDataframe() -> dict:
        return dict.copy(k_car_dataframe)

    def getData(self) -> dict:
        return dict.copy(self.data)

    def getValue(self, key: str) -> int:
        try: return self.data[key]
        except KeyError: return None

    def setValue(self, key: str, value: int) -> None:
        self.data[key] = value # the value will be added even if the key doesn't exist