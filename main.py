# Heyyo, welcome to my tournament generator. Just click run and the code should prompt you on the rest.

import random, time

print("Hey! Thanks for using this program. Please enter each player, one by one. When all players are in, type DONE")

class Person:
	def __init__(self, name):
		self.name = name
		self.losses = 0
		self.first = 0
		self.second = 0
		self.third = 0
		self.fourth = 0

playerList = []
bracket = []
loserBracket = []
userInput = ""

# Take in all players and randomize that list.
while 1:
	print("Next player, please")
	userInput = input()
	if userInput.upper() == "DONE":
		break	
	buildPerson = Person(userInput)
	playerList.append(buildPerson)
random.shuffle(playerList)
if len(playerList) < 6:
	print("WARNING: Using this software with less than 6 players will lead to errors.")

# Organize this list into groupings of four
p0 = None
p1 = None
p2 = None
p3 = None

for i in range(0,len(playerList)):
	if i % 4 == 0:
		p0 = playerList[i]
	elif i % 4 == 1:
		p1 = playerList[i]
	elif i % 4 == 2:
		p2 = playerList[i]
	elif i % 4 == 3:
		p3 = playerList[i]
		bracket.append([p0,p1,p2,p3])

# If players cant be evenly split, deal with it here (min size = 3)
if len(playerList) % 4 == 1 and len(playerList) >= 6:
	temp1 = r1List[len(r1List)-1][3]
	r1List[len(r1List)-1].remove(temp1)
	temp2 = r1List[len(r1List)-2][3]
	r1List[len(r1List)-2].remove(temp2)
	r1List.append([p0,temp1,temp2])
elif len(playerList) % 4 == 2  and len(playerList) >= 6:
	temp = r1List[len(r1List)-1][3]
	r1List[len(r1List)-1].remove(temp)
	r1List.append([p0,p1,temp])
elif len(playerList) % 4 == 3  and len(playerList) >= 6:
	r1List.append([p0,p1,p2])

print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print("Alright! Here's round one:\n")
time.sleep(0.5)
i = 1
for group in r1List:
	print("Group " + str(i) +":")
	for person in group:
		print(person.name)
	i+=1
	print("")
time.sleep(2)
print("When you complete round 1, press enter")
input()
i = 0
for group in r1List:
	print("Great! Who won round 1 in group " + str(i+1) + "?")
	print("Was it: [enter the number]")
	p = 1
	for person in group:
		print("\t[" + str(p) + "]: " + person.name)
		p+=1
	userInput = int(input())
	while userInput < 0 or userInput > len(group):  userInput = input()