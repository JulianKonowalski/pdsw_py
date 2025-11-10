class CarData:

    def __init__(self, data: bytearray = None) -> None:
        if data == None:
            self.button_state: int  = 0
            self.dial_0: int        = 0
            self.dial_1: int        = 0
            self.dial_2: int        = 0
            self.soc: int           = 0
            self.temp: int          = 0
            self.curr_msb: int      = 0
            self.curr_lsb: int      = 0
            self.volt_msb: int      = 0
            self.volt_lsb: int      = 0
            self.map: int           = 0
            self.pwr: int           = 0
        else:
            self.button_state: int  = int.from_bytes(data[0])
            self.dial_0: int        = int.from_bytes(data[1])
            self.dial_1: int        = int.from_bytes(data[2])
            self.dial_2: int        = int.from_bytes(data[3])
            self.soc: int           = int.from_bytes(data[4])
            self.temp: int          = int.from_bytes(data[5])
            self.curr_msb: int      = int.from_bytes(data[6])
            self.curr_lsb: int      = int.from_bytes(data[7])
            self.volt_msb: int      = int.from_bytes(data[8])
            self.volt_lsb: int      = int.from_bytes(data[9])
            self.map: int           = int.from_bytes(data[10])
            self.pwr: int           = int.from_bytes(data[11])