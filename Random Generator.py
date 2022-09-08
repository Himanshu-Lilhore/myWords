noun = open("BestNouns.txt", "r")
adjective = open("BestAdjectives.txt", "r")
verb = open("BestVerbs.txt", "r")

noun = noun.readlines()
nl = len(noun) - 1
while nl >= 0:
    noun[nl] = noun[nl][:-1]
    nl -= 1

adjective = adjective.readlines()
ad = len(adjective) - 1
while ad >= 0:
    adjective[ad] = adjective[ad][:-1]
    ad -= 1

verb = verb.readlines()
vb = len(verb) - 1
while vb >= 0:
    verb[vb] = verb[vb][:-1]
    vb -= 1

howMany = 3
nl = len(noun) - 1
ad = len(adjective) - 1
vb = len(verb) - 1
import random
for i in range(howMany):
    whichNoun = random.randint(0, nl)
    whichAdjective = random.randint(0, ad)
    whichVerb = random.randint(0, vb)
    print(adjective[whichAdjective].upper(), verb[whichVerb] +
          "ing", noun[whichNoun].upper(), sep="")
