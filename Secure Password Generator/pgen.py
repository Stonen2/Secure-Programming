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

word = ''



def ruleone():
    a = ''
    for x in range(10):
        c = random.randint(0,9)
        a = a + str(c)
        print(c)
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



def salt(l):
    n = ''
    if l == 1:

        for i in range(7):
            g = random.randint(0,9)
            n = n + str(g)
            word = word + n
    else:
        for i in range(6):
            g = random.randint(0,9)
            n = str(g) + n
            word = n + word
    return n


def mutatepass():
    print("Working")



def ranrule():

    for x in range(3):
        a = random.randint(1,len(rules))
        if a == 1:
            print("Rule 1")
            rules.remove(1)
            word = word + ruleone()

        elif a == 2:
            print("RUle 2")
            word = word + pickword()
            rules.remove(2)

        else:
            print("Rule 3")
            ll = random.randint(1,2)
            salt(ll)
            ru+les.remove(3)


def writeout():
  f = open("SecurePass.txt", "a")
  f.write("The Secure Password Generated is " + word + "\n")


def main():
    rules.append(1)
    rules.append(2)
    rules.append(3)
    getdictionary()
    dictionaryAttack()

    ranrule()
    mutatepass()
    writeout()
    #loaddic()
    #mutatepass()
    #genpass()
    #b = ruleone()


    #print(b)

    #print("Hello Universe")





main()
