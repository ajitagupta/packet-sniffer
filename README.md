# Sniffing in Python - Tutorial
![Static Badge](https://img.shields.io/badge/Network%20Security-Tutorial-blue)

Coming from a security background (I did a Master's in Computer and Network Security) here is a glimpse of what we used to do in our labs all the time: packet sniffing or wiretapping. Packets contain data that is exchanged between devices connected to the internet. Packet sniffing gives us a feeling of what kind of data is arriving at our end and how we can detect potential security threats and suspicious activities better. 

Building a packet sniffer is an opportunity to practice my networking and programming skills. A simple packet sniffer in Python needs a socket (a socket to a computer is like a door to a house, an opening) module. After configuring the socket module to capture packets from the network or *tapping the connection*, we write a Python script to extract information from the captured packets.
So, let's get started!

## What is packet sniffing?
The packet sniffer that I will create and walk you through monitors and analyzes network traffic. A sniffer can continuously monitor all the traffic to a computer through the network interface card by decoding the information encapsulated in the data packets. Examples of what is contained in these data packets are
- Emails
- Passwords
- Browser surfing
- Chat sessions
- Router configuration (internet routes)
- DNS traffic (internet configurations on a computer)

## How does a packet look like?
The internet consists of multiple layers which are best described using the famous [OSI Reference Model](https://www.educative.io/blog/osi-model-layers). Each layer of the model is its own protocol used for communication amongst nodes, or networked devices. This is how a data packet is structured at Layer 4: Transmission Control Protocol (TCP).
<br>
![TCP packet](https://i.ibb.co/CM4SVX4/tcppacket.gif "TCP packet")
<br>

## The Code
### 1. First we load our libraries
```
import socket
import struct
import binascii
```
### 2. Now we tap
```
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0800)) #Creating socket
packet = s.recvfrom(46)
```
We first open a socket or *tap* and grab 46 bits in length. In the socket function, we will need to pass three variables: the first specifying a windows packet interface (AF_INET); the second specifying that we are opening a raw socket, and the third specifying the protocol we are interested in, which is the IPv4 protocol in this case. We will then rely on the recvfrom function to receive a packet (of size 46).
### 3. We finally output the hacker
```
tcp_header = packet[0][0:31] # Get first line of the packet
unpacked_tcp_header = struct.unpack("!6s6s", tcp_header)
print ("Destination MAC:" + binascii.hexlify(unpacked_tcp_header[0]) + " Source MAC:" + binascii.hexlify(unpacked_tcp_header[1])))
```
We still need to print the formatted packet data, and we will make that happen using the struct and binascii imports above. Given that in this tutorial, we are only interested in the source and destination IP addresses, we only care about the first line in the packet (as demonstrated in the diagram). We grab the first line (row size 0, column size 0 to 31) of that header and printing them as follows: Return a pair with two hex values, converted by hexify in the binascii module. The first being the destination, the second the source. MAC stands for Media Access Control address, sometimes referred to as a hardware or physical address, and is a unique, 12-character alphanumeric attribute that is used to identify individual electronic devices on a network.

## Criminology report
Do the investigation on the guy at destination and inform the person at source if the former is unidentifiable.

## Docker
This program support Docker: dockerfile contains the code to download Docker and configure. docker.sh is a Shell script that opens a Docker container and executes the Python program in it.



