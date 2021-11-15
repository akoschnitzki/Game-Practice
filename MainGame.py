
import sys
import time
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)

slowprint("------------------------------")
slowprint("******************************")
slowprint("The Hollow File")
slowprint("******************************")
slowprint("------------------------------")
slowprint("A Game by Alexander Koschnitzki")
x = input("Input User Name :")
print()


