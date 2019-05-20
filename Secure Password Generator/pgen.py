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
    if l == 1:
        print("Hello World")
    else:
        print("Hello World")

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



            rules.remove(3)


        print(a)


def main():
    rules.append(1)
    rules.append(2)
    rules.append(3)
    ranrule()
    #loaddic()
    #mutatepass()
    #genpass()
    b = ruleone()
    getdictionary()
    dictionaryAttack()
    print(words)

    #print(b)

    #print("Hello Universe")





main()
