# Ethernet Raw Socket Communication 
This python command line sample demonstrates how to communicate with a Thorlabs Ethernet capable power meter using
raw python socket communication without any additional library. 

# Details 
The powermeter uses a binary protocol to frame large request/response messages to multiple TCP packets. The given codes
uses synchronous IO to implement this binary protocol for data exchange. The example does not contain any network device
discovery. You need to know the IP and port number of the power meter to connect. Once the connection is established you
can use the methods to send and receive text and binary request and response data. 

## Limitations
Please be aware the power meter will close the connection automatically if no communication is ongoing for 30 seconds.

## Supported Meters
- PM103E
- PM5020
