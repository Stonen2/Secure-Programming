#full connection in python
# Base code by Gary Lewandowski
#Additional Code to Create a Range of Ports to be scanned 
# Along with the half scan and the additional use of the 
from socket import *
import sys 


FSOpenPorts = list()
FSClosedPorts = list()





#This is the connect port for scan THis is because of the SOcket connection
# Socket Connection is used in a full scan 
#A full scan is successful during the try Phase
#THe except statement is the socket unable to connect 

def printfile(port): 
  f = open("FullScan.txt", "a")
  f.write("There is an open port and the port number is " + port + "\n")

def FullScanConnectTo(host, port):
  serverName = host
  serverPort = str(port)
  clientSocket = socket(AF_INET,SOCK_STREAM)
  clientSocket.settimeout(1)
  try:
    clientSocket.connect((serverName,serverPort))
    clientSocket.close()
    #FSopenPorts.append(serverPort)
    printfile(serverPort)
    print("Port is open")
    return True
  except Exception as e:
    # didn't connect
    clientSocket.close()
    #FSClosedPorts.append(serverPort)

    return False

# Parameters ipad,begport, endport
def main(ipad, begport, endport): 
    counter = 0 
    i = int(begport) 
    j = int(endport) 
    #print(j)

    while(i < j):
        #This contacts the full scan
        FullScanConnectTo(ipad,i)
        #print("Scanning port" + str(i))

        i = i + 1
        #print(i)
# print(FSClosedPorts)
    #print(FSOpenPorts)


    #print(FullScanConnectTo("10.253.250.9", 80))





ip = sys.argv[1]
begp = sys.argv[2]
endp = sys.argv[3]
#print(ip, begp, endp)
main(ip,begp,endp)