from scapy.layers.inet import IP, TCP, ICMP
from scapy.sendrecv import sr1
import sys



fsopen =[] 
openports = [] 


def printfile(port): 
  f = open("HalfScan.txt", "a")
  f.write("There is an open port and the port number is " + port + "\n")

def halfscan(ipaddress, bp):
    fsopen.append( sr1(IP(dst=ipaddress)/TCP(dport=bp,flags="S")))
    unans = fsopen[0]
    flag = unans.sprintf("%TCP.flags%")
    #print(fsopen)
    #print(bp)
    print(flag)
    if(flag == "SA"):
        openports.append(bp)
        printfile(bp)
        #Print to the file a port was open 
        print("Port was open")


    return fsopen



def main(ipad, begp, endp): 
    i = int(begp) 
    k = int(endp)
    count = 0 
    while(i < k):
        #Call Function


        test = halfscan(ipad,i)
        #print(test)
      #  unans = test[0]
       # for lll in test: 
        #    print(lll)
        #ans = test[1]
        #unans = test[0]
        
        #print(unans)
        
        #test.show()
        i = i + 1
   
    
    
    print("----------------------------------------------------------------------------")
    print("\n")
   # print(fsopen) 
    #print(openports)








ip = sys.argv[1]
begp = sys.argv[2]
endp = sys.argv[3]
#print(ip, begp, endp)
main(ip,begp,endp)

#main("192.168.163.1",49664,49677 )