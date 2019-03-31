#full connection in python
# Base code by Gary Lewandowski
#Additional Code to Create a Range of Ports to be scanned 
# Along with the half scan and the additional use of the 


from socket import *
from scapy.layers.inet import IP, TCP, ICMP
from scapy.sendrecv import sr 

FSOpenPorts = list()
FSClosedPorts = list()





#This is the connect port for scan THis is because of the SOcket connection
# Socket Connection is used in a full scan 
#A full scan is successful during the try Phase
#THe except statement is the socket unable to connect 

def FullScanConnectTo(host, port):
  serverName = host
  serverPort = port
  clientSocket = socket(AF_INET,SOCK_STREAM)
  clientSocket.settimeout(1)
  try:
    clientSocket.connect((serverName,serverPort))
    clientSocket.close()
    FSopenPorts.append(serverPort)
    print("Connection")
    return True
  except Exception as e:
    # didn't connect
    clientSocket.close()
    #FSClosedPorts.append(serverPort)

    return False

# Parameters ipad,begport, endport
def main(ipad, begport, endport): 
    counter = 0 
    i = begport 
    j = endport 

    while(i < j):
        #This contacts the full scan
        FullScanConnectTo(ipad,i)


        i = i + 1
        print(i)
# print(FSClosedPorts)
    print(FSOpenPorts)


    #print(FullScanConnectTo("10.253.250.9", 80))







main("10.253.250.9",8080,8240)