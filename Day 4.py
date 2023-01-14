
covered_ranges = 0
overlapping_ranges = 0

with open('Day 4.txt','r') as txt_file:

	for line in txt_file.readlines():

		ranges = line.rstrip().split(',')
		x1,y1 = map(int,ranges[0].split('-'))
		x2,y2 = map(int,ranges[1].split('-'))

		if (x1 >= x2 and y1 <= y2) or (x1 <= x2 and y1 >= y2):

			covered_ranges += 1


		if (x1 <= x2 <= y1) or (x1 <= y2 <= y1) or (x2 <= x1 <= y2) or (x2 <= y1 <= y2):  

			overlapping_ranges += 1

print('Star 1:',covered_ranges)
print('Star 2:',overlapping_ranges)

