# Wiretapping in Python - Tutorial
Coming from a security background (I did a Master's in Computer and Network Security) here is a glimpse of what we used to do all the time: packet sniffing or wiretapping. This was done to get a feeling of what kind of data is arriving at our end (host) and how we can control, analyze, and work on it better. 

Building a packet sniffer is an opportunity to practice my networking and programming skills. A simple packet sniffer in Python needs a socket module. After configuring the socket module to capture packets from the network, we write a Python script to extract those captured packets.
So, let's get started!

## What is packet sniffing, i.e. wiretapping?
The packet sniffer that I will create and walk you through monitors network traffic. This is done to detect suspicious activity, capture and analyze data packets that flow between devices within the same network, and monitor packets that are exchanged between networked devices and the internet. Examples of what is contained in these packets are
- Emails
- Passwords
- Browser surfing
- Chat sessions
- Router configuration (internet routes)
- DNS traffic (internet configurations on a computer)

A sniffer can continuously monitor all the traffic to a computer through the network interface card by decoding the information encapsulated in the data packets.
