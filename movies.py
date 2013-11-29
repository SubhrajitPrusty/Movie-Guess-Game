import os
import random

def game():
	os.system("cls")
	m = open("list.txt","r+")
	full = m.read()

	mlis = full.split("\n")
	l = len(mlis)
	i = random.randint(0,l)

	original = mlis[i].upper()
	l = len(original)
	k = int(l/3)
	given = list()
	for p in original:
		if p!="/":
			x="_"
		else:
			x=p
		given.append(x)

	for x in range(k):
		n = random.randint(0,l-1)
		given[n] = original[n]

	joint = "".join(given)
	completed = False
	wr_entries = set()
	r_entries = set()
	count = len(wr_entries)

	while not completed and count < 10:

		shown = " ".join(given)
		print("\n \n"+shown,'\n')
		joint = "".join(given)

		n = input("Guess character: ").upper()
		if len(n) != 1 or n.isspace():
			print("You didnot enter a character. TRY AGAIN")
			continue
		os.system("cls")
		gotit = False
		for x in range(l):
			if n == original[x]:
				given[x] = n
				gotit = True

		if n in r_entries or n in wr_entries:
			print("You already guessed that.")
			input("Press enter to continue...")
			os.system("cls")

		if gotit:
			r_entries.add(n)
		else:
			print("\n! ! ! W R O N G ! ! ! \n")
			wr_entries.add(n)
			count = len(wr_entries)
			input("Press enter to continue...")
			os.system("cls")


		print("\nWrong Entries : ")
		for x in wr_entries:
			print(x,end="  ")
		print("\n\nNumber of wrong guesses :",count)

		print("\nRight Entries : ")
		for x in r_entries:
			print(x,end="  ")
		print("\n________________________________________")

		shown = " ".join(given)
		joint = "".join(given)
		completed = joint == original

		if completed:
			print('\n'+shown,'\n')
			print("! ! ! C O R R E C T ! ! !")
			break
		elif completed == False and count >= 10:
			print("\nYou failed to guess the movie within the trial limit.",'\n')
			print(original)
			break
	m.close()

again = "y"
while again == "y":
	game()
	again = input("Do you want to play again?? y or n : ").lower()
else:
	print("\nThank you for playing :)\nPress enter to exit.")
	input()
