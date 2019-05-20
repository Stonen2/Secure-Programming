import random





#Generate a 20 Character Password
#Randomly Pick from the 3 Rules such that rules cannot be guessed
#First Rule pick a 8,9,10 Character Dictionary Password
#Mutate the dictionary Word --> Change random Characters to special characters
#Second Rule Generate Random 10 Numbers
#Third Rule Salt The Dictionary pass and Mutate Numbers



def loaddic():
    print("Hello World")


def ruleone():
    a = ''
    for x in range(10):
        c = random.randint(0,9)
        a = a + str(c)
        print(c)

    print("Working")
    return a


def getdictWords():
    print("Hello World")



def mutatepass():
    print("Working")

def genpass():
    print("Working")

def ranrule():
    print("Hello World")


def main():

    loaddic()
    mutatepass()
    genpass()
    b = ruleone()
    print(b)

    print("Hello Universe")





main()
