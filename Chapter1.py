import sys
import time
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)

slowprint("Chapter 1 ")
print()
slowprint("It was a cold rainy night, the sirens of police cars filled the air")
slowprint("The young detective just arrived in his police car to the scene.")
slowprint("You decide to talk to the witnesses on scene")
while True:
	import random

	def people():
		global witnessName
		global response
		global witnessanswers

		response = ["Do you know who did it?", "Can you talk about what happened?", "Is everything ok?", "Did anyone get hurt"]
		witnessNameChoice = ["Ron", "Bobby", "Sam"]
		witnessanswers = ["That is interesting", "Hopefully you find the person"]

		random.shuffle(witnessNameChoice)
		witnessName = witnessNameChoice[0]

		print(witnessName, ":] Hello, I am ", witnessName, ", would you like to talk to me? :")
		random.shuffle(response)
		answer = input("Press y to talk to the witness :")

		random.shuffle(witnessanswers)
		witnessanswers = witnessanswers[0]
		if answer == "y":
			print(witnessName, ":] ", response[0])
			input("Y or N :")
			print(witnessanswers)

		elif answer == "n":
			print(witnessName, ":] Goodbye")

	people()
	x = input("Do you still want to ask more questions? :")
	if x == "n":
		break
slowprint("As you get done asking the witnesses on scene,")
slowprint("You decide to go inside to inspect some more ")
print()
slowprint("********************")
slowprint("End of Chapter 1")
slowprint("********************")

