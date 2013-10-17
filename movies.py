import random

m = open("/list.txt","r+")
full = m.read()

mlis = full.split("\n")
#print(mlis)
l = len(mlis)
#print(l)
i = random.randint(0,l)
#print(i)

original = mlis[i].upper()
#print(original)
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
	#print(given)
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
	#print(joint)

	n = input("Guess character: ").upper()
	gotit = False
	for x in range(l):
		if n == original[x]:
			given[x] = n
			gotit = True
	
	if n in r_entries or n in wr_entries:
		print("You already guessed that.")
		input()


	if gotit:
		r_entries.add(n)
	else:
		print("Wrong!!")
		wr_entries.add(n)
		count = len(wr_entries)
		input()
		print("\nNumber of wrong guesses :",count)
		input()


	print("\nWrong Entries : ")
	for x in wr_entries:
		print(x,end="  ")

	print("\nRight Entries : ")
	for x in r_entries:
		print(x,end="  ")
	print("\n________________________________________")

	shown = " ".join(given)
	#print(shown)
	joint = "".join(given)
	#print(joint)
	completed = joint == original
	
else:
	if completed:
		print('\n'+shown,'\n')
		print(original,'\n')
		print("Correct!")
	elif completed == False and count >= 10:
		print("\nYou failed to guess the movie within the trial limit.",'\n')
		print(original)

input()

m.close()
