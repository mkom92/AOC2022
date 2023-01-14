if __name__ == '__main__':

	# create a set of rocks coordinates from the input

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

	# get the bottom limit - if a grain of sand falls below this point, stop

	ys = set()

	for rock in rocks:

		ys.add(rock[1])


	def falling_sand(max_y,star,x=500,y=0):

		yn = 0

		run = True
		while run:

			grain_of_sand = (x, y + yn)

			if grain_of_sand not in rocks and grain_of_sand not in sand:

				yn += 1 

			else:

				left = (grain_of_sand[0]-1,grain_of_sand[1])
				right = (grain_of_sand[0]+1,grain_of_sand[1])

				if grain_of_sand == (x,y):
					run = False
					return run

				elif left not in rocks and left not in sand:

					run = falling_sand(max_y,star,left[0],left[1])

				elif right not in rocks and right not in sand:

					run = falling_sand(max_y,star,right[0],right[1])

				else:

					sand.add((grain_of_sand[0],grain_of_sand[1]-1))
					return True

			if star == 2 and grain_of_sand[1] == max_y:

				sand.add((grain_of_sand[0],grain_of_sand[1]-1))
				return True

			if grain_of_sand[1] > max_y or grain_of_sand[1] < y:
				run = False
				return run


	max_y = max(ys)
	sand = set()


	run = True
	while run:
		run = falling_sand(max_y = max_y,star=1)

	print('Star 1:',len(sand))



	max_y = max(ys) + 2
	sand = set()


	run = True
	while run:
		run = falling_sand(max_y = max_y,star=2)

	print('Star 2:',len(sand))