import RPi.GPIO as GPIO

import time

import smbus

def getlight():
  bus = smbus.SMBus(1)
  addr = 0x23
  data = bus.read_i2c_block_data(addr,0x11)
  return "Luminosity:" + str((data[1] + (256 * data[0])) / 1.2) + "lx"
if __name__ == '__main__':
    print(getlight())

