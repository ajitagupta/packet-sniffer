import socket
import struct
import binascii

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket. htons(0x0800)) # creating socket
while True:
    packet = s.recvfrom(2048)

# a bit more criminology
ethernet_header = packet[0][0:14] # Get Ethernet Header
eth_header = struct.unpack("!6s6s2s", ethernet_header)
print ("Destination MAC:" + binascii.hexlify(eth_header[0]) + " Source MAC:" + binascii.hexlify(eth_header[1]))) # finding the crook
