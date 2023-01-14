
rocks = set()
with open('Day 14.txt','r') as txt_file:

	for line in txt_file:

		points = [p for p in line.strip().split(' -> ')]

		for n in range(len(points)-1):

			x1,y1 = map(int,[i for i in points[n].split(',')])
			x2,y2 = map(int,[i for i in points[n+1].split(',')])

			if x1 == x2:

				min_y = min([y1,y2])
				max_y = max([y1,y2]) + 1

				x = [x1]
				y = [y_inp for y_inp in range(min_y,max_y)]

			else:

				min_x = min([x1,x2])
				max_x = max([x1,x2]) + 1

				y = [y1]
				x = [x_inp for x_inp in range(min_x,max_x)]

			for xx in x:

				for yy in y:

					rocks.add((xx,yy))


# print(sorted(rocks))

sand = set()


def falling_sand((x,y) = (500,0)):

	grain_of_sand = (x,y)
	yn = 0

	while True:

		grain_of_sand = (grain_of_sand[0], grain_of_sand[1] + yn)

		if grain_of_sand not in rocks and grain_of_sand not in sand:

			yn += 1 
			continue

		# elif grain_of_sand in sand:

		else:

			left = (grain_of_sand[0]-1,grain_of_sand[1])
			right = (grain_of_sand[0]+1,grain_of_sand[1])

			if left not in rocks and left not in sand:

				falling_sand(left)

			elif right not in rocks and right not in sand:

				falling_sand(right)

			else:

				sand.add((grain_of_sand[0],grain_of_sand[1]-1))

