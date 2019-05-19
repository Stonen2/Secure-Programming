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

def printfile(port,ipad): 
    f = open("FullScan.txt", "a")
    f.write("The IP Address" + ipad + " has an open port and the port number is " + str(port) + "\n")



#From the given code we know that the try statement means that we have completed the 3 way handshake and that 
#THe port is open. Thus in the try we then pass the port number to the print file to record that the port
#that was successfully connected to is open 

def FullScanConnectTo(host, port):
  serverName = host
  #serverPort = int(port)
  serverPort = port
  clientSocket = socket(AF_INET,SOCK_STREAM)
  clientSocket.settimeout(1)
  try:
    clientSocket.connect((serverName,serverPort))
    clientSocket.close()
    #FSopenPorts.append(serverPort)
    return True
  except Exception as e:
    # didn't connect
    clientSocket.close()
    #FSClosedPorts.append(serverPort)

    return False

# Parameters ipad,begport, endport
#THis takes in arguments from the command line and casts each of these to the proper variable type 
#This then starts a loop that sets the counter to be the beginning port given and J to be the ending port
#that is specified by the user 
def main(ipad, begport, endport): 
    #counter = 0 
    i = int(begport) 
    j = int(endport) 
    #i = begport 
    #j = endport 
    #print(j)

    while(i <= j):
        #This contacts the full scan
        a = FullScanConnectTo(str(ipad),i)
        if a == True: 
          print("Port is open " + str(i) )
          printfile(i,ipad)
         
        #print("Scanning port" + str(i))
        print(a)
        i = i + 1
        #print(i)
# print(FSClosedPorts)
    #print(FSOpenPorts)


    #print(FullScanConnectTo("10.253.250.9", 80))




#ip = "10.253.250.9"
#begp = 1
#endp = 200
ip = sys.argv[1]
begp = sys.argv[2]
endp = sys.argv[3]
#print(ip, begp, endp)
main(ip,begp,endp)