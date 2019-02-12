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
def runallAttacks():
  print("Swag on Full Attack")

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
  s = s.capitalize()

  if count == 0:
   s = s + '0'
  elif count == 1:
   s= s + '1'
  elif count ==2:
    s= s + '2'
  elif count == 3: 
    s=s + '3'
  elif count == 4: 
    s=s+'4' 
  elif count == 5: 
    s=s + '5'
  elif count == 6: 
    s=s + '6'
  elif count == 7: 
    s=s+ '7'
  elif count == 8: 
    s=s + '8'
  elif count == 9: 
    s=s+ '9'
  #print(s)
  return s
  
  

def cracked(unknown, known): 
  if(encode(known) == unknown):
      print("YOu have cracked a password")
      return False
  else: 
    return True 

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
def decode(s):
  m = hashlib.sha256()
  s.decode()
  return s
def firstattack(unknown):
  count = 0
  notcracked = True
  done = False
  while(notcracked == True):
    
    for i in svnLetters:
      while(count < 10):
        s = ruleonedoc(i,count)
        notcracked = cracked(unknown,s)
        if(notcracked == False):
          print("the password that was cracked was" + s)
          count = 100
          done = True
          break
          #a = decode(s)
          #print()
        count = count + 1 
      if(done == True):
        break
      count = 0


def secondattack(unknown):
  firstlayer = 0
  secondlayer = 0
  thirdlayer = 0 
  fourthlayer = 0
  fifthlayer = 0 
  crackedss = False
  holding = True
  #gg = encodeFor2nd(0,0,0,0,0)
  #print(gg)
  while(crackedss == False):
    if(firstlayer == 5):
      crackedss = True
      break
    gg = encodeFor2nd(firstlayer,secondlayer,thirdlayer,fourthlayer,fifthlayer)
    #print(gg)
    encode(gg)
    holding = cracked(unknown,gg)
    if(holding == False):
      print("Password Cracked "  + gg)
      break
    fifthlayer = fifthlayer + 1
    if(fifthlayer == 10):
      fourthlayer = fourthlayer + 1
      fifthlayer = 0
      if(fourthlayer == 10):
        thirdlayer = thirdlayer + 1
        fourthlayer = 0
        if(thirdlayer == 10):
          secondlayer = secondlayer + 1
          thirdlayer = 0
          if(secondlayer == 10):
            firstlayer = firstlayer + 1
            secondlayer = 0
            if(firstlayer == 5):
              break
              #notfound = true

    #crackedss = True
  

def encodeFor2nd(f,s,t,fo,fi):
  if(f == 0):
    a = "*"
  elif (f ==1):
    a = "~"
  elif (f ==2):
    a = "!"
  elif(f == 3):
    a = "#"
  if(s ==0):
    b = "0"
  elif(s ==1):
    b = "1"
  elif(s ==2):
    b = "2"
  elif(s ==3):
    b = "3"
  elif(s ==4):
    b = "4"
  elif(s ==5):
    b = "5"
  elif(s ==6):
    b = "6"
  elif(s ==7):
    b = "7"
  elif(s ==8):
    b = "8" 
  elif(s ==9):
    b = "9" 
  if(t ==0):
    c = "0"
  elif(t ==1):
    c = "1"
  elif(t ==2):
    c = "2"
  elif(t ==3):
    c = "3"
  elif(t ==4):
    c = "4"
  elif(t ==5):
    c = "5"
  elif(t ==6):
    c = "6"
  elif(t ==7):
    c = "7"
  elif(t ==8):
    c = "8" 
  elif(t ==9):
    c = "9" 
  ###########
  if(fo ==0):
    d = "0"
  elif(fo ==1):
    d = "1"
  elif(fo ==2):
    d = "2"
  elif(fo ==3):
    d = "3"
  elif(fo ==4):
    d = "4"
  elif(fo ==5):
    d = "5"
  elif(fo ==6):
    d = "6"
  elif(fo ==7):
    d = "7"
  elif(fo ==8):
    d = "8" 
  elif(fo ==9):
    d = "9" 
  ############
  if(fi ==0):
    e = "0"
  elif(fi ==1):
    e = "1"
  elif(fi ==2):
    e = "2"
  elif(fi ==3):
    e = "3"
  elif(fi ==4):
    e = "4"
  elif(fi ==5):
    e = "5"
  elif(fi ==6):
    e = "6"
  elif(fi ==7):
    e = "7"
  elif(fi ==8):
    e = "8" 
  elif(fi ==9):
    e = "9" 
  g = a + b + c + d + e
  #print(g)
  return g

def thirdattack(unknown):
  crackedss = False
  holding = True
  firstl = 0
  secondl = 0
  thirdl = 0 
  fourthl = 0
  while(crackedss == False):
    if(firstl == 5):
      crackedss = True
      break
    gg = encodeforthird(firstl,secondl,thirdl,fourthl)
    #print(gg)
    encode(gg)
    holding = cracked(unknown,gg)
    if(holding == False):
      print("Password Cracked "  + gg)
      break
    if(fourthl == 5):
      break
    

def encodeforthird(o,t,th,f):
  if(o == 0):
    a = "*"
  elif (o ==1):
    a = "~"
  elif (o ==2):
    a = "!"
  elif(o == 3):
    a = "#"
  
  if(t == 0):
    b = "*"
  elif (t ==1):
    b = "~"
  elif (t ==2):
    b = "!"
  elif(t == 3):
    b = "#"
  else:
    b= ""
  if(th == 0):
    c = "*"
  elif (th ==1):
    c = "~"
  elif (th ==2):
    c = "!"
  elif(th == 3):
    c = "#"
  else: 
    c=""
  if(f == 0):
    d = "*"
  elif (f ==1):
    d = "~"
  elif (f ==2):
    d = "!"
  elif(f == 3):
    d = "#"
  else: 
    d =""
  temp = a + b + c + d 
  print(temp)
  return a + b + c + d



def fourthattack(unknown):
  correct = True
  for i in dictionary: 
    h = i
    i = i.replace('a','@')
    i = i.replace('l','1')
    
    #print(i)
    correct = cracked(unknown,i)
    if(correct == False):
      print("PAssword is cracked " + i)
      break
      

def fifthattack(unknown):
  correct = True
  number = 0
  while(number < 999999):
    j = str(number)
    #print(i)
    correct = cracked(unknown,str(number))
    
    if(correct == False):
      print("PAssword is cracked " + j)
      break
    number = number + 1

def sixthattack(unknown):
  correct = True
  for i in dictionary: 
    #print(i)
    correct = cracked(unknown,i)
    if(correct == False):
      print("PAssword is cracked " + i)
   
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
    #print(rawdata[1])
    

    firstattack(rawdata[1])
    #print(encode("~0011"))

    #print(rawdata[4])
    secondattack(rawdata[4])
    #print(rawdata[7])
    #getdictionary()
    #print(encode("programming"))
    sixthattack(rawdata[10])
    #print(encode("93439"))
    #print("\n")
    #print(rawdata[13])
    #print(rawdata[9])
    ##print("\n")
    #print(rawdata[8])
    print(rawdata[7])
    fourthattack(rawdata[7])
    #print("\n")
    #print(rawdata[5])
    fifthattack(rawdata[13])
    #print(encode("****"))
    #print(rawdata[16])
    thirdattack(rawdata[16])
    
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
