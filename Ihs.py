from scapy.layers.inet import IP, TCP, ICMP
from scapy.sendrecv import sr1
import random 
import sys


fsopen =[] 
openports = [] 
allports = [] 

def printfile(port): 
  f = open("HalfScan.txt", "a")
  f.write("There is an open port and the port number is " + port + "\n")


def halfscan(ipaddress, bp):
    fsopen.append( sr1(IP(dst=ipaddress)/TCP(dport=bp,flags="S")))
    unans = fsopen[0]
    flag = unans.sprintf("%TCP.flags%")
    print(fsopen)
    print(bp)
    print(flag)
    if(flag == "SA"):
        openports.append(bp)
        print("Port was open")
        printfile(str(bp))


    return fsopen

def randport(bp, ep):
    a = random.randint(int(bp),int(ep))
    flag = False
    while(flag == False):
        if a not in allports: 
            a = random.randint(int(bp),int(ep))
            flag = False
        else: 
            allports.remove(a)
            return a

def grabTheFile():
    with open("/usr/share/nmap/nmap-services","r") as g:
        text = g.readlines()
        for line in text:
            print(line)

#def printReport():


def main(ipad, begp, endp): 
    i = int(begp) 
    count = int(begp)
    k = int(endp)
    while(count < k):
        allports.append(count)
        count = count + 1

    #while(len(allports) > 1):
    #    randport(begp, endp)
    ##    print(allports)
     #   print("\n")


    #print("ALl Ports is Empty --------------------")
    #print(allports)
    while(len(allports) > 1 ):
        #Call Function
        port = randport(begp, endp)

        test = halfscan(ipad,port)
        print("\n")
        print(allports)
        #print(test)
      #  unans = test[0]
       # for lll in test: 
        #    print(lll)
        #ans = test[1]
        #unans = test[0]
        
        #print(unans)
        
        #test.show()
        #i = i + 1
   
    
    
    print("----------------------------------------------------------------------------")
    print("\n")
    print("SCAN FINISHED")
    
   # print(fsopen) 
    print(openports)
    print("\n")
    grabTheFile()
    print("\n")
    print(openports)





ip = sys.argv[1]
begp = sys.argv[2]
endp = sys.argv[3]
#print(ip, begp, endp)
main(ip,begp,endp)


#main("192.168.163.1",49664,49670 )
