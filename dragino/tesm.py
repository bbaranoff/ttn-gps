# importing the module
import socket
import cayenneLPP
import lora

# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 0)
s.setblocking(True)

# creating Cayenne LPP packet
lpp = cayenneLPP.CayenneLPP(size = 100, sock = s)

# adding 2 digital outputs, the first one uses the default channel
lpp.add_digital_input(True)
lpp.add_digital_input(False, channel = 112)

# sending the packet via the socket
lpp.send()
