#
# Test script for Raspberry pi 2017-09-16
# using APA102 144 strip
#
import wiringpi
import time
import struct
SPIchannel = 0 #SPI Channel
SPIspeed = 16000000 #Clock Speed in Hz
wiringpi.wiringPiSetupGpio()
wiringpi.wiringPiSPISetup(SPIchannel, SPIspeed)

sendData = struct.pack("BBBB",0x00,0x00,0x00,0x00)
wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)

for i in range(48):
    sendData = struct.pack("BBBB",0xff,48-i,0,i)
    wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)

for i in range(48):
    sendData = struct.pack("BBBB",0xff,0,i,48-i)
    wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)

for i in range(48):
    sendData = struct.pack("BBBB",0xff,i,48-i,0)
    wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)

sendData = struct.pack("BBBB",0x00,0x00,0x00,0x00)
wiringpi.wiringPiSPIDataRW(SPIchannel, sendData)
