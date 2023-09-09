import socket
import struct
import binascii

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket. htons(0x0800)) # creating socket
while True:
    packet = s.recvfrom(46)

# criminology
tcp_header = packet[0][0:31] # Get first line of the packet
unpacked_tcp_header = struct.unpack("!6s6s", tcp_header)
print ("Destination MAC:" + binascii.hexlify(unpacked_tcp_header[0]) + " Source MAC:" + binascii.hexlify(unpacked_tcp_header[1]))) # finding the crook MAC address
