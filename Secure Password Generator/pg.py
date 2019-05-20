import random


rules = list()
dictionary = list()
words = list()
#Generate a 20 Character Password
#Randomly Pick from the 3 Rules such that rules cannot be guessed
#First Rule pick a 8,9,10 Character Dictionary Password
#Mutate the dictionary Word --> Change random Characters to special characters
#Second Rule Generate Random 10 Numbers
#Third Rule Salt The Dictionary pass and Mutate Numbers

global word 




def ruleone():
    a = ''
    for x in range(10):
        c = random.randint(0,9)
        a = a + str(c)
        #print(c)
    return a


def getdictionary():
  with open("/usr/share/dict/words","r") as g:
        text = g.readlines()
        for line in text:
            dictionary.append(line.rstrip())


def dictionaryAttack():
  for a in dictionary:
    if(len(a) == 8 or len(a) == 9 or len(a) == 10):
        words.append(a)

def pickword():
    b = random.randint(0,len(words))
    c = words[b]

    return c



def salt(l, t):
    n = ''
    he = ''
    if l == 1:

        for i in range(7):
            g = random.randint(0,9)
            n = n + str(g)
            t =  t + n
    else:
        for i in range(6):
            g = random.randint(0,9)
            n = str(g) + n
            t = n + t
    return t



def mutatepass(word):
    c = random.randint(0,5)
    if c == 1:

         word = word.replace('a','@')

    elif c == 2:
        word = word.replace('o','#')

    elif c == 3:
        word = word.replace('l','1')


    elif c == 4:
        word = word.replace('s','$')



    else:
        word = word.replace('a','@')
    return word





def ranrule():
    testing = ''
    x = 1
    rr = False 
    bb = False 
    cc = False 
    while(bb == False or cc == False or rr == False):
        
        #print(x)
        a = random.randint(1,3)
        #print(a)
        if a == 1 and 1 in rules:
            print("Rule 1")
            rules.remove(1)
            g = ruleone()
            testing = testing + g
            rr = True 

        elif a == 2 and 2 in rules:
            print("RUle 2")
            d = pickword()
            testing = testing + d
            rules.remove(2)
            bb = True 

        elif a == 3 and 3 in rules:
            print("Rule 3")
            ll = random.randint(1,2)
            j = salt(ll, testing)
            testing = j
            rules.remove(3)
            cc = True 
            
    return testing


def writeout(w):
  f = open("SecurePass.txt", "a")
  f.write("The Secure Password Generated is " + w + "\n")


def main():
    word = ''
    rules.append(1)
    rules.append(2)
    rules.append(3)
    getdictionary()
    dictionaryAttack()

    word = ranrule()
    word = mutatepass(word)
    writeout(word)
    #loaddic()
    #mutatepass()
    #genpass()
    #b = ruleone()


    #print(b)

    #print("Hello Universe")





main()