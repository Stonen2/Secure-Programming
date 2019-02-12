import hashlib


rawdata = list()

def fun1():
    mylist = list()
    with open("crackme.txt") as f:
        for line in f:
            mylist(line)
    return mylist
def test():
    print('hello world')

    uncrack = list() 
    userhashes = list()
    usernames = list() 




    file = open("crackme.txt","r")

    print(file)


    print(file.readline())


    file.close

    uncrack = fun1()
    print("   \n")

    print(uncrack)


def main():
    #f = open("crackme.txt")
    #text = f.readlines()
    #print(f.readline())
    #rawdata = f.readline()
    #for l in text:
    #    rawdata = f.readline()
    
    #f.close


    with open("crackme.txt","r") as g:
        text = g.readlines()
        for line in text:
            print(line)
    
    print(rawdata)

   
    #for s in rawdata:
    #    print(s)


main()

