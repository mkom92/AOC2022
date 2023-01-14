if __name__ == '__main__':

	# Util

	def round_position(x,y):

		if x > y:
			val = -(-(x+y)//2)

		else:
			val = (x+y)//2

		return val

	# Part 1

	head = [0,0]
	tail = [0,0]

	move_dict = {'R': [0,1], 'L': [0,-1], 'U': [1,1], 'D': [1,-1]}

	tail_positions = set()

	with open('Day 9.txt','r') as txt_file:

		for line in txt_file.readlines():

			direction, steps = line.rstrip().split(' ')

			move = move_dict[direction]

			for _ in range(int(steps)):

				head[move[0]] += move[1]

				if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:

					tail = [round_position(head[0],tail[0]), round_position(head[1],tail[1])]

				tail_positions.add(f'{tail[0]},{tail[1]}')

	print('Star 1:',len(list(tail_positions)))

	# Part 2

	n = 10
	knots = []

	for _ in range(n):

		knots.append([0,0])


	last_knot_positions = set()

	with open('Day 9.txt','r') as txt_file:

		for line in txt_file.readlines():

			direction, steps = line.rstrip().split(' ')

			move = move_dict[direction]

			for _ in range(int(steps)):

				knots[0][move[0]] += move[1]

				for k, _ in enumerate(knots[1:]):

					if abs(knots[k][0] - knots[k+1][0]) > 1 or abs(knots[k][1] - knots[k+1][1]) > 1:

						knots[k+1] = [round_position(knots[k][0],knots[k+1][0]), round_position(knots[k][1],knots[k+1][1])]

				last_knot_positions.add(f'{knots[n-1][0]},{knots[n-1][1]}')

	print('Star 2:',len(list(last_knot_positions)))
	