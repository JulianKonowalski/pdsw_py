import tkinter as tk

class SpiDev:
    def __init__(self):
        self.mode = 0
        self.max_speed_hz = 1000
        self.mockVal = 0

        self.__setup_test_data__()
        self.__setup_test_window__()  # for capturing user inputs

    def open(self, bus, device):
        print(f"Opening mock SPI device on bus {bus}, device {device}")

    def close(self):
        print("Closing mock SPI device")

    def xfer2(self, data):
        response = [  # this is slow, but left as a proof of concept
            self.buttonState,
            self.dial1,
            self.dial2,
            self.dial3,
            self.bms_soc,
            self.bms_temp,
            self.bms_currMSB,
            self.bms_currLSB,
            self.volt >> 8 & 0xFF,
            self.volt & 0xFF,
            # self.bms_voltMSB,
            # self.bms_voltLSB,
            self.pedal_map,
            self.power_limit,
        ]
        self.buttonState = 0  # to avoid unwanted button clicks
        return response

    def button1press(self, event):
        self.buttonState = self.buttonState | 1

    def button2press(self, event):
        self.buttonState = self.buttonState | 1 << 1

    def button3press(self, event):
        self.buttonState = self.buttonState | 1 << 2

    def button4press(self, event):
        self.buttonState = self.buttonState | 1 << 3

    def button5press(self, event):
        self.buttonState = self.buttonState | 1 << 4

    def button6press(self, event):
        self.buttonState = self.buttonState | 1 << 5

    def dial1inc(self, event):
        if self.dial1 < 2:
            self.dial1 += 1

    def dial1dec(self, event):
        if self.dial1 > 0:
            self.dial1 -= 1

    def dial2inc(self, event):
        if self.dial2 < 2:
            self.dial2 += 1

    def dial2dec(self, event):
        if self.dial2 > 0:
            self.dial2 -= 1

    def dial3inc(self, event):
        if self.dial3 < 2:
            self.dial3 += 1

    def dial3dec(self, event):
        if self.dial3 > 0:
            self.dial3 -= 1

    def __setup_test_data__(self):
        self.buttonState = 0
        self.dial1 = 0
        self.dial2 = 0
        self.dial3 = 0
        self.bms_soc = 79
        self.bms_temp = 150
        self.bms_currMSB = 0x00
        self.bms_currLSB = 0x01 
        self.bms_voltMSB = 0x00
        self.bms_voltLSB = 0x00
        self.pedal_map = 0
        self.power_limit = 0

        self.volt = 0

    def __update__(self):
        if self.buttonState & 1 and self.volt < 100: self.volt += 2
        elif self.buttonState & 2 and self.volt > 5: self.volt -= 4

        # self.bms_soc -= 1
        # self.bms_temp += int(
        #     5 * math.sin(self.testSinArg)
        # )  # again slow, but left as a proof of concept

        # curr = self.bms_currMSB << 8 | self.bms_currLSB
        # curr += int(20 * math.cos(self.testSinArg))
        # self.bms_currLSB = curr & 0xFF
        # self.bms_currMSB = (curr >> 8) & 0xFF

        # self.testSinArg += 3.14 / 6

        self.window.after(self.timestep, self.__update__)

    def __setup_test_window__(self):
        self.timestep = 1
        self.testSinArg = 0

        self.window = tk.Tk()
        self.window.title("SPI_CONTROL")

        self.window.bind("q", self.button1press)
        self.window.bind("w", self.button2press)
        self.window.bind("e", self.button3press)
        self.window.bind("r", self.button4press)
        self.window.bind("t", self.button5press)
        self.window.bind("y", self.button6press)

        self.window.bind("a", self.dial1inc)
        self.window.bind("z", self.dial1dec)
        self.window.bind("s", self.dial2inc)
        self.window.bind("x", self.dial2dec)
        self.window.bind("d", self.dial3inc)
        self.window.bind("c", self.dial3dec)

        self.window.after(self.timestep, self.__update__)