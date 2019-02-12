import hashlib


rawdata = list()
dictionary = list()
svnLetters = list()


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


def encode(s):
  #print(s)
  h = hashlib.sha256(s.encode()).hexdigest()
  return h


#Reads in all of the dictionary into memory  
def getdictionary():
  #print("Hello World")
  with open("/usr/share/dict/words","r") as g:
        text = g.readlines()
        for line in text:
          dictionary.append(line.rstrip())

#Ballroom blitz?         
def dictionaryAttack():
  #print("Hello World")  
  for a in dictionary:
    if(len(a) == 7):
      svnLetters.append(a)

def ruleonedoc(s,count):
  s.capitalize()
  if count == 0:
    s + 0
  elif count == 1:
    s + 1
  elif count ==2:
    s + 2
  elif count == 3: 
    s + 3
  elif count == 4: 
    s+4 
  elif count == 5: 
    s + 5
  elif count == 6: 
    s + 6
  elif count == 7: 
    s+ 7
  elif count == 8: 
    s + 8
  else: 
    s+ 9
  return s
  
  

def cracked(unknown, known): 
  if(encode(known) == unknown):
      print("SUCCESS")


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
def firstattack():
  count = 0: 
  notcracked = True
  while(notcracked == True):
    

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
    #print(encode("Puzzles4"))
    dictionaryAttack()

    #print(svnLetters)
    #print(dictionary[0].capitalize())

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

