import hashlib


rawdata = list()
dictionary = list()

#def fun1():
 #   mylist = list()
 #   with open("crackme.txt") as f:
  #      for line in f:
 #           mylist(line)
 #   return mylist
#def test():
   # print('hello world')

 #   uncrack = list() 
  #  userhashes = list()
   # usernames = list() 




#    file = open("crackme.txt","r")

 #   print(file)
#

   # print(file.readline())


   # file.close

   # uncrack = fun1()
  #  print("   \n")

  # print(uncrack)

#Reads in all of the dictionary into memory  
def getdictionary():
  #print("Hello World")
  with open("/usr/share/dict/words","r") as g:
        text = g.readlines()
        for line in text:
          dictionary.append(line)

#Ballroom blitz?         
def dictionaryAttack():
  print("Hello World")  

#Prints the given array Nothin special 
def printarray(list):
  for i in list: 
      print(i)
#Open the Users and Passwords to CRACK 
def grabTheFile():
    with open("crackme.txt","r") as g:
        text = g.readlines()
        for line in text:
            temp = line.split(':')

            #print(line)
            rawdata.append(temp[0])
            rawdata.append(temp[1])
            rawdata.append(temp[3])
            
            #rawdata.append(line)
    

#Main Main Main
def main():
    #f = open("crackme.txt")
    #text = f.readlines()
    #print(f.readline())
    #rawdata = f.readline()
    #for l in text:
    #    rawdata = f.readline()
    
    #f.close
    grabTheFile()
    printarray(rawdata)
    getdictionary()
    #print(dictionary[1000])
    #print(rawdata)
    
   # for line4 in rawdata:
   #     print(line4)

    #m = hashlib.sha256()
    #m.update("hello world")
    #m.hexdigest()

   
    #for s in rawdata:
    #    print(s)


main()

