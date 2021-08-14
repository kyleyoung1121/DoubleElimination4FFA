# Heyyo, welcome to my tournament generator. Just click run and the code should prompt you on the rest.

import random, time
from datetime import datetime
print("Hey! Thanks for using this program. Please enter each player, one by one. When all players are in, type DONE")

class player:
	def __init__(self, name):
		self.name = name
		self.losses = 0
		self.first = 0
		self.second = 0

def TakeInput(upperBound):
	while True:
			try: 
				userInput = int(input())
				if userInput < 1 or userInput > upperBound:
					print("Sorry, that was an invalid input, please try again.")
				else:	
					return userInput
					break
			except:
				print("Sorry, that was an invalid input, please try again.")

def FindResults(bracket, groupNumStart = 1):
	# Find results of this round
	groupNum = groupNumStart - 1
	for group in bracket:
		# First, ask who got first
		print("Great! Who placed 1st in group " + str(groupNum+1) + "?")
		print("Was it: [enter the number]")
		# Set up some variables to track which players win and lose
		firstAndSecond = [] 
		winnerNames = []
		loserNames = []
		# Iterate through this group and print the player names
		playerNum = 1
		for player in group:
			print("\t[" + str(playerNum) + "]: " + player.name) 
			playerNum+=1
		# Ask for who got first and validify that answer 
		userInput = -99999
		userInput = TakeInput(len(group))	
		firstAndSecond.append(userInput) # Log who got first
		# Iterate through and adjust the correct player's class values
		playerNum = 1
		for player in group:
			if playerNum == userInput:
				player.first += 1 
				winnerNames.append(player.name)
			playerNum+=1
		# Next, ask who got second
		print("Okay. Who placed second?") 
		# Don't allow them to answer the 1st place player for 2nd place too.
		userInput = firstAndSecond[0]
		while int(userInput) == firstAndSecond[0]:  
			userInput = TakeInput(len(group))
			if int(userInput) == firstAndSecond[0]:
				print("You can't select that player again!")
		firstAndSecond.append(userInput)
		# Check all players. Update second place and mark the others as losers.
		playerNum = 1
		for player in group:
			if playerNum == userInput:
				player.second += 1
				winnerNames.append(player.name)
			elif playerNum != firstAndSecond[0] and playerNum != firstAndSecond[1]:
				player.losses += 1 
				loserNames.append(player.name)
				# For each player that didn't place 1st or 2nd, knock to losers bracket or remove
				# If player is already on the loser list, remove them.
				if loserList.count(player) > 0:
					loserList.remove(player)	
				else: # Otherwise, just push them into the losers bracket
					loserList.append(player)
					playerList.remove(player)
			playerNum+=1
		print("")
		time.sleep(1.5)
		groupNum +=1
		# Log the results of these findings in the log.txt file
		my_file = open("log.txt", "a")
		if bracket == loserBracket:
			# If the bracket selected is the loser bracket, reflect that in the txt
			my_file.write("LB: " + winnerNames[0] + " and " + winnerNames[1] + " defeat " + loserNames[0] + " and " + loserNames[1] + "\n")
			my_file.close()
		else:
			print("DEBUG: winnerNames:")
			print(winnerNames)
			print("DEBUG: loserNames:")
			print(loserNames)
			my_file.write("WB: " + winnerNames[0] + " and " + winnerNames[1] + " defeat " + loserNames[0])
			if len(loserNames) > 1:
				my_file.write(" and " + loserNames[1] + "\n")
			else:
				my_file.write("\n")
			my_file.close()

def GroupsFromList(list, bracket):
	# random.shuffle(list) # This line of code shuffles the players for a better shot at not running into the same player over and over
	i = 0

	if len(list) == 0:
		return

	p0 = None
	p1 = None
	p2 = None
	p3 = None
	for player in list:
		if i % 4 == 0: 
			p0 = player
		elif i % 4 == 1:
			p1 = player
		elif i % 4 == 2:
			p2 = player
		elif i % 4 == 3:
			p3 = player
			bracket.append([p0,p1,p2,p3])
			p0 = None
			p1 = None
			p2 = None
			p3 = None
		i+=1
	if p0 == None:
		return
	elif p1 == None:
		# This code runs if the last grouping only set p0.
		temp1 = bracket[len(bracket)-1][3]
		bracket[len(bracket)-1].remove(temp1)
		temp2 = bracket[len(bracket)-2][3]
		bracket[len(bracket)-2].remove(temp2)
		bracket.append([p0,temp1,temp2])
	elif p2 == None:
		# This code runs if the last grouping only set p0 and p1.
		temp = bracket[len(bracket)-1][3]
		bracket[len(bracket)-1].remove(temp)
		bracket.append([p0,p1,temp])
	elif p3 == None:
		# This code runs if the last grouping only set p0, p1, and p2.
		bracket.append([p0,p1,p2])
	
def PrintBracket(bracket, groupNumStart = 1):
	groupNum = 1
	for group in bracket:
		print("Group " + str(groupNum) +":")
		for player in group: # Print all people in each group
			print(player.name)
		groupNum+=1
		print("")
	time.sleep(1)

playerList = []
loserList = []
bracket = []
loserBracket = []
userInput = "" 

# Open the log.txt file and put intro text
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
my_file = open("log.txt", "a")
my_file.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
my_file.write("New log at " + str(current_time) + "\n")
my_file.write("This log will not whether the match up was in the winners bracket (WB) or the losers bracket (LB). The player that places first will be listed first, followed by second place.\n\n")
my_file.close()

# Take in all players and randomize that list.
while 1:
	print("Next player, please")
	userInput = input()
	if userInput.upper() == "DONE":
		break	
	buildplayer = player(userInput)
	playerList.append(buildplayer)
#random.shuffle(playerList)
if len(playerList) < 6:
	print("ERROR: Must be used on groups of 6 or more.")
	quit()

# Loop through the player list and add groups of four to the bracket list.
GroupsFromList(playerList, bracket)

# A little showmanship
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print("Alright! Here's round one:\n")
time.sleep(0.5)

# Iterate through the bracket
groupNum = 1
for group in bracket:
	print("Group " + str(groupNum) +":")
	for player in group: # Print all people in each group
		print(player.name)
	groupNum+=1
	print("")
time.sleep(2)
print("When you're ready to submit the results of this round, press enter")
input()
# Ask user for results of this round
FindResults(bracket)

while not (len(loserList) < 3 and len(playerList) < 3):
	# Wipe the brackets clean for the new round
	bracket = []
	loserBracket = []
	
	# If the losers bracket has only 5 people, we need to move one
	if len(loserList) == 5:
		# This commented out code might work, but isnt ideal
		# It chooses someone from loser bracket to send back to main bracket
		# Encounters problem when len(playerList) == 11
		'''time.sleep(1)
		luckyPlayer = random.choice(loserList)
		print("Because the loser bracket cannot have exactly 5 players, " + luckyPlayer.name + " has been selected to get a free pass back into the winners bracket.")
		luckyPlayer.losses -= 1
		playerList.append(luckyPlayer)
		loserList.remove(luckyPlayer)
		time.sleep(1)'''

		# This approach will just let the main bracket run a round
		GroupsFromList(playerList, bracket)
		print("Because of the number of players in the losers bracket, this round will just be the main bracket, to allow for a better structured next round for the losers bracket")
		print("Here are the groupings for this round:")
		PrintBracket(bracket)
		print("When you're ready to submit the results of this round, press enter")
		input()
		FindResults(bracket)
		bracket = []
		loserBracket = []

	# Build bracket from those with no losses.
	
	if len(playerList) >= 3:
		# print("DEBUG: len(playerList):" + str(len(playerList)))
		# print("DEBUG: len(loserList):" + str(len(loserList)))
		GroupsFromList(playerList, bracket)
	
	# Build losers bracket from the losers with one loss.
	if len(loserList) >= 3:
		# print("DEBUG: len(loserList):" + str(len(loserList)))
		GroupsFromList(loserList, loserBracket)
		
	# Print out both brackets
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	if len(playerList) >= 3:
		print("Here are the groupings for this round:")
		PrintBracket(bracket)

	# Note: I'm passing a custom groupNum, because I want to continue from there
	if len(loserList) >= 3:
		print("Here are the groupings for the losers bracket:")
		PrintBracket(loserBracket,len(bracket)+1)

	# Pause until they move on via space bar
	print("When you're ready to submit the results of this round, press enter")
	input()

	# Ask for results
	# Push players from bracket to losers bracket if their first loss
	if len(playerList) >= 3:
		FindResults(bracket)
	if len(loserList) >= 3:
		FindResults(loserBracket, len(bracket)+1)
	
	# Remove players from losers bracket upon second loss
	for player in playerList:
		if player.losses > 1:
			playerList.remove(player)
	for player in loserList:
		if player.losses > 1:
			loserList.remove(player)
	
	# Loop if not narrowed to the final four
time.sleep(1)
print("We're getting close to the end now!")
time.sleep(1)
print("Here is the match-up for the final round:")
for player in playerList:
	print(player.name)
for player in loserList:
	print(player.name)

# Move final two from loser bracket into finals (in winners bracket)
for player in loserList:
	playerList.append(player)

# Ask for the winner
print("When you're ready to submit the results of this round, press enter")
input()
print("Alright, who won?")
print("Was it: [enter the number]")

# Print out each player
playerNum = 1
for player in playerList:
	print("\t[" + str(playerNum) + "]: " + player.name)  
	playerNum+=1

# Ask for who got first and validify that answer 
userInput = -99999
userInput = TakeInput(len(group))
playerNum = 1
for player in playerList:
	if playerNum == userInput:
		player.first += 1 # Update the player's class value
		print("Congradulations to " + player.name + "!")
		my_file = open("log.txt", "a")
		my_file.write("WB: " + player.name + " has triumphed over all in the final match up!\n")
		my_file.close()
	playerNum+=1