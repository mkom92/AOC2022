elves = []
elf = 0

with open('Day 1.txt','r') as txt_file:

	for line in txt_file.readlines():

		try:

			i = int(line)
			elf += i

		except:

			elves.append(elf)
			elf = 0


print("Star 1:",max(elves))

elves.sort()

print("Star 2:",sum(elves[-3:]))