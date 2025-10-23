class CarData:

    def __init__(self, data: list[int] = None) -> None:
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
            self.button_state: int  = data[0]
            self.dial_0: int        = data[1]
            self.dial_1: int        = data[2]
            self.dial_2: int        = data[3]
            self.soc: int           = data[4]
            self.temp: int          = data[5]
            self.curr_msb: int      = data[6]
            self.curr_lsb: int      = data[7]
            self.volt_msb: int      = data[8]
            self.volt_lsb: int      = data[9]
            self.map: int           = data[10]
            self.pwr: int           = data[11]