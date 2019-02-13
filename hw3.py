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
      print("YOu have cracked a password and the password was " + known)
      return False
  else: 
    return True 

#Prints the given array Nothin special 
def printarray(list):
  for i in list: 
      print(i)
#Open the Users and Passwords to CRACK 
def grabTheFile():
    with open("password.txt","r") as g:
        text = g.readlines()
        for line in text:
            temp = line.split(':')

            #print(line)
            rawdata.append(temp[0])
            rawdata.append(temp[1])
            #rawdata.append(temp[3])
            
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
        #print(s)
        notcracked = cracked(unknown,s)
        if(notcracked == False):
          return False
          print("the password that was cracked was" + s)
          count = 100
          done = True
          break
          #a = decode(s)
          #print()
        count = count + 1 
      if(done == True):
        notcracked = False
        break
      count = 0
    break
  return True


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
      return False
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
  return True

def encodeFor2nd(f,s,t,fo,fi):
  a = ""
  b = ""
  c = ""
  d = ""
  e = ""
  g= ""
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
  fivel = 0 
  sixl = 0 
  sevenl = 0 
  eightl = 0 
  while(crackedss == False):
    if(firstl == 5):
      crackedss = True
      break
    gg = encodeforthird(firstl,secondl,thirdl,fourthl,fivel,sixl,sevenl,eightl)
    #print(gg)
    if(gg == 9999):
      crackedss = True
      break
    encode(gg)
    holding = cracked(unknown,gg)
    if(holding == False):
      return False
      print("Password Cracked "  + gg)
      break
    else:
      eightl = eightl + 1
      if(eightl == 10):
        eightl = 0 
        sevenl = sevenl + 1
        if(sevenl == 10):
          sevenl = 0 
          sixl = sixl +1 
          if(sixl == 10):
            sixl = 0
            fivel = fivel + 1
            if(fivel == 10):
              fivel = 0
              fourthl = fourthl + 1
              if(fourthl == 5):
                fourthl = 0
                thirdl = thirdl + 1
                if(thirdl == 5):
                  thirdl = 0
                  secondl = secondl + 1
                  if(secondl == 5):
                    secondl = 0
                    firstl = firstl + 1
                    if(firstl == 5 ):
                      print("FUNCTION DONE")
                      crackedss = True
                      break


    
  return True  

def encodeforthird(o,t,th,fl,fiv,six,sev,eig):
  a = ""
  b = ""
  c = ""
  d = ""
  e = ""
  f = ""
  g = ""
  h = ""
  temp = ""
  if(o == 0):
    a = "*"
  elif (o ==1):
    a = "~"
  elif (o ==2):
    a = "!"
  elif(o == 3):
    a = "#"
  elif(o == 4):
    a = ""
  if(t == 0):
    b = "*"
  elif (t ==1):
    b = "~"
  elif (t ==2):
    b = "!"
  elif(t == 3):
    b = "#"
  elif(t == 4):
    b= ""
  if(th == 0):
    c = "*"
  elif (th ==1):
    c = "~"
  elif (th ==2):
    c = "!"
  elif(th == 3):
    c = "#"
  elif(th == 4): 
    c=""
  if(fl == 0):
    d = "*"
  elif (fl ==1):
    d = "~"
  elif (fl ==2):
    d = "!"
  elif(fl == 3):
    d = "#"
  elif(fl == 4): 
    d =""





  if(fiv ==0):
    e = "0"
  elif(fiv ==1):
    e = "1"
  elif(fiv ==2):
    e = "2"
  elif(fiv ==3):
    e = "3"
  elif(fiv ==4):
    e = "4"
  elif(fiv ==5):
    e = "5"
  elif(fiv ==6):
    e = "6"
  elif(fiv ==7):
    e = "7"
  elif(fiv ==8):
    e = "8" 
  elif(fiv ==9):
    e = "9"

  if(six ==0):
    f = "0"
  elif(six ==1):
    f = "1"
  elif(six ==2):
    f = "2"
  elif(six ==3):
    f = "3"
  elif(six ==4):
    f = "4"
  elif(six ==5):
    f = "5"
  elif(six ==6):
    f = "6"
  elif(six ==7):
    f = "7"
  elif(six ==8):
    f = "8" 
  elif(six ==9):
    f = "9" 
  ###########
  if(sev ==0):
    g = "0"
  elif(sev ==1):
    g = "1"
  elif(sev ==2):
    g = "2"
  elif(sev ==3):
    g = "3"
  elif(sev ==4):
    g = "4"
  elif(sev ==5):
    g = "5"
  elif(sev ==6):
    g = "6"
  elif(sev ==7):
    g = "7"
  elif(sev ==8):
    g = "8" 
  elif(sev ==9):
    g = "9" 
  ############
  if(eig ==0):
    h = "0"
  elif(eig ==1):
    h = "1"
  elif(eig ==2):
    h = "2"
  elif(eig ==3):
    h = "3"
  elif(eig ==4):
    h = "4"
  elif(eig ==5):
    h = "5"
  elif(eig ==6):
    h = "6"
  elif(eig ==7):
    h = "7"
  elif(eig ==8):
    h = "8" 
  elif(eig ==9):
    h = "9" 







  temp = a + b + c + d + e + f + g + h  
  #print(temp)
  #if(temp == "!#~!3313"):
  #  print("YO YO YO ")
  return temp 



def fourthattack(unknown):
  correct = True
  for i in dictionary: 
    h = i
    i = i.replace('a','@')
    i = i.replace('l','1')
    
    #print(i)
    correct = cracked(unknown,i)
    if(correct == False):
      return False
      print("PAssword is cracked " + i)
      break
  return True
      

def fifthattack(unknown):
  correct = True
  number = 0
  while(number < 999999):
    j = str(number)
    #print(i)
    correct = cracked(unknown,str(number))
    
    if(correct == False):
      return False
      print("PAssword is cracked " + j)
      break
    number = number + 1
  return True

def sixthattack(unknown):
  correct = True
  for i in dictionary: 
    #print(i)
    correct = cracked(unknown,i)
    if(correct == False):
      return False
      print("PAssword is cracked " + i)
   
#Main Main Main

def runAllAttacksAtOnce(): 
  count = 1 
  userTracker = 0
  temporary = len(rawdata)
  #print(temporary) 
  while(temporary > count):
    PasswordHacked = True
    #print(rawdata[count])
    #print("\n")
    #print(rawdata[userTracker])
    #print("\n")
    #print(rawdata[count])
   # print("\n")
    #print(PasswordHacked)
    PasswordHacked = firstattack(rawdata[count])
    if(PasswordHacked == False):
      print("First level You have cracked " + rawdata[userTracker])
      print(rawdata[userTracker])
      userTracker = userTracker + 2  
      count = count + 2
      passwordHacked = False
      #print("LOOP BACK")
    else: 
      #print("First attack failed")
      PasswordHacked = secondattack(rawdata[count])
      if(PasswordHacked == False):
        print("Second Leve You have cracked " + rawdata[userTracker])
        print(rawdata[userTracker])
        userTracker = userTracker + 2  
        count = count + 2
        
      else:
        #print("Second Attack Failed")
        PasswordHacked = thirdattack(rawdata[count])
        
        if(PasswordHacked == False):
          print("\n")
          print("YO YO YO WE HAVE A MAJOR PROBLEM CAP")
          print("Level three You have cracked " + rawdata[userTracker])
          print(rawdata[userTracker])
          userTracker = userTracker + 2  
          count = count + 2
        else: 
          #print("Third Attack Failed")
          PasswordHacked = fourthattack(rawdata[count])
          if(PasswordHacked == False):
            print("Level four you have cracked " + rawdata[userTracker])
            print(rawdata[userTracker])
            userTracker = userTracker + 2  
            count = count + 2
          else: 
            #print("Fourth attack failed")
            PasswordHacked = fifthattack(rawdata[count])
            if(PasswordHacked == False):
              print("level five You have cracked " + rawdata[userTracker])
              print(rawdata[userTracker])
              userTracker = userTracker + 2  
              count = count + 2
            else: 
                #print("Ffifth attack Failed")
                PasswordHacked = sixthattack(rawdata[count])
                if(PasswordHacked == False):
                  print("You have cracked " + rawdata[userTracker])
                  print(rawdata[userTracker])
                  userTracker = userTracker + 2  
                  count = count + 2
                else: 
                  print("All Failed")
                  #print("A password was not Cracked")
                  userTracker = userTracker + 2
                  count = count + 2



    
    
def writeout(): 
  print("Just Temporary")


def main():
    #f = open("crackme.txt")
    #text = f.readlines()
    #print(f.readline())
    #rawdata = f.readline()
    #for l in text:
    #    rawdata = f.readline()
    
    #f.close
    grabTheFile()
    #printarray(rawdata)
    getdictionary()
    #print(encode("Puzzles4"))
    dictionaryAttack()
    #print(rawdata[1])
    
    runAllAttacksAtOnce()
   # firstattack(rawdata[1])
    #print(encode("~0011"))

    #print(rawdata[4])
    #secondattack(rawdata[4])
    #print(rawdata[7])
    #getdictionary()
    #print(encode("programming"))
    #sixthattack(rawdata[10])
    #print(encode("93439"))
    #print("\n")
    #print(rawdata[13])
    #print(rawdata[9])
    ##print("\n")
    #print(rawdata[8])
    #print(rawdata[7])
    #fourthattack(rawdata[7])
    #print("\n")
    #print(rawdata[5])
    #fifthattack(rawdata[13])
    #print(encode("****"))
    #print(rawdata[16])
    #thirdattack(rawdata[16])
    
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