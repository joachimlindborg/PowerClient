# This is the main file used by the ESP8266 aftre the boot.py
# be sure to have network enabled so we can reach internet
# If you don't want the I2C bus for acessing displays etc
# just comment that out

import machine

blinkpin = machine.Pin(2, machine.Pin.OUT)
def toggle(state=None):
    blinkpin.value(not blinkpin.value())

def blink(times=1,pause=300):
    while times > 0:
        times-=1
        toggle()
        time.sleep_ms(pause)
        toggle()
        time.sleep_ms(pause)

SCL_PIN_ID=5
SDA_PIN_ID=4
I2C_FREQ=100000

#scl = machine.Pin(SCL_PIN_ID,machine.Pin.OUT)
scl = machine.Pin(SCL_PIN_ID)
sda = machine.Pin(SDA_PIN_ID)

#i2c = machine.I2C(scl = machine.Pin(SCL_PIN_ID,machine.Pin.OUT),
i2c = machine.I2C(scl = machine.Pin(SCL_PIN_ID),
                  sda = machine.Pin(SDA_PIN_ID),
                  freq = I2C_FREQ)

import powertrend
#from powertrend import *
D=powertrend.Powertrend(i2c)
D.main_run()
