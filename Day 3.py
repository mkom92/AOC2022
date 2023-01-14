
score = 0

with open('Day 3.txt','r') as txt_file:
	
	for line in txt_file.readlines():

		x = line.rstrip()
		l = x[:(len(x)//2)]
		r = x[(len(x)//2):]

		same = ''

		for i in l:

			if i in r:

				same = i
				break

		if same == same.upper():

			score += ord(same) - ord('A') + 27

		else:

			score += ord(same) - ord('a') + 1


print("Star 1:",score)


score3 = 0

with open('Day 3.txt','r') as txt_file:


	list3 = []

	for line in txt_file.readlines():

		list3.append(line.rstrip())

		if len(list3) == 3:

			same3 = ''

			for elem1 in list3[0]:

				if elem1 in list3[1] and elem1 in list3[2]:

					same3 = elem1

			if same3 == same3.upper():

				score3 += ord(same3) - ord('A') + 27

			else:

				score3 += ord(same3) - ord('a') + 1

			list3 = []


print("Star 2:",score3)
