import SerialWombat
import time
from smbus2 import SMBus, i2c_msg

class SerialWombatChip_cp_i2c(SerialWombat.SerialWombatChip):
    i2c  = 0
    def __init__(self,i2c_port,address):
        super().__init__()
        self.i2c = i2c_port
        self.address = address

    def sendReceivePacketHardware (self,tx):
        try:

            if (isinstance(tx,bytearray)):
                tx = list(tx)

            with SMBus(self.i2c) as bus:

                msg = i2c_msg.write(self.address, tx)
                bus.i2c_rdwr(msg)

                msg = i2c_msg.read(self.address, 8)
                bus.i2c_rdwr(msg)

            rx = bytearray(list(msg))
            
            if (len(rx) < 8 ):
                return (-len(rx))
            return 8,rx  
        except OSError:
            return -48,bytes("E00048UU",'utf-8')

    def sendPacketToHardware (self,tx):
        try:
            """
            if (isinstance(tx,bytearray)):
                tx = list(tx)
            """

            if (isinstance(tx,bytearray)):
                tx = list(tx)
            
            with SMBus(self.i2c) as bus:
                msg = i2c_msg.write(self.address, tx)
                bus.i2c_rdwr(msg)
                    
            return 8,bytes("E00048UU",'utf-8')
        except OSError:
            return -48,bytes("E00048UU",'utf-8')

