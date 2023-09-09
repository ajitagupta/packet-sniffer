# Sniffing in Python - Tutorial
Coming from a security background (I did a Master's in Computer and Network Security) here is a glimpse of what we used to do in our labs all the time: packet sniffing or wiretapping. Packets contain data that is exchanged between devices connected to the internet. Packet sniffing gives us a feeling of what kind of data is arriving at our end and how we can control, analyze, and work on it better. 

Building a packet sniffer is an opportunity to practice my networking and programming skills. A simple packet sniffer in Python needs a socket (a socket to a computer is like a door to a house, an opening) module. After configuring the socket module to capture packets from the network, we write a Python script to extract those captured packets.
So, let's get started!

## What is packet sniffing?
The packet sniffer that I will create and walk you through monitors network traffic. This is done to detect suspicious activity like hacking, capture and analyze data packets that flow between devices within the same network, and monitor packets that are exchanged between devices and the internet. Examples of what is contained in these packets are
- Emails
- Passwords
- Browser surfing
- Chat sessions
- Router configuration (internet routes)
- DNS traffic (internet configurations on a computer)

A sniffer can continuously monitor all the traffic to a computer through the network interface card by decoding the information encapsulated in the data packets.

## How does a packet look like?
The internet consists of multiple layers which are best described using the famous OSI Reference Model. Each layer of the model is its own protocol used for communication amongst nodes, or networked devices. This is how a data packet is structured at Layer 4: Transmission Control Protocol (TCP).
![TCP packet](https://i.ibb.co/CM4SVX4/tcppacket.gif "TCP packet")


