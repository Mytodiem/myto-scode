from random import randint

print("nhap dam, la, keo:")
Player = input()
computer = randint(0,2)
if computer == 0:
	computer = "dam"
if computer == 1:
	computer = "La"
if computer ==2:
	computer = "keo"

print("---")
print("you choose: " +Player)
print("computer choose:" +computer)
print("---")

if Player == computer:
	print("draw")
else:
	if Player == "keo":
		if computer=="la":
			print("win")
		else:
			print("Lose")
	elif Player == "dam":
		if computer == "keo":
			print("Win")
		else:
			print("Lose")
	elif Player =="la":
		if computer =="keo":
			print("Lose")
		else:
			print("Win")
	else:
		print("nhap sai")