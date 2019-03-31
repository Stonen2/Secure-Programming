from scapy.layers.inet import IP, TCP, ICMP
from scapy.sendrecv import sr1
from scapy.sendrecv import sr




fsopen =[] 
openports = [] 


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


    return fsopen



def main(ipad, begp, endp): 
    i = begp 
    k = endp
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
    print(openports)






main("192.168.163.1",49664,49677 )