if __name__ == '__main__':

	# Variables

	X = 1
	cycle = 1
	
	lookup_cycles = {}

	row = ''
	render = []

	# Utils

	def new_cycle(cycle,X,lookup_cycles,row,render):

		if (cycle+20) % 40 == 0:
			lookup_cycles[cycle] = X

		elif ((cycle-1) % 40 == 0) and cycle != 1:
			render.append(row)
			row = ''

		if X <= cycle % 40 <= X+2:
			row += '█'

		else:
			row += '.'

		return row


	# Loop

	with open('Day 10.txt','r') as txt_file:

		for line in txt_file.readlines():

			row = new_cycle(cycle,X,lookup_cycles,row,render)

			if line.rstrip() == 'noop':

				cycle += 1

			else:

				cycle += 1

				row = new_cycle(cycle,X,lookup_cycles,row,render)

				cycle += 1
				X += int([i for i in line.rstrip().split(' ')][1])


		render.append(row)

	# Results

	signal_strength = 0

	for key, value in lookup_cycles.items():

		signal_strength += key*value

	print('Star 1:', signal_strength)

	print('Star 2 render:\n')
	for r in render:

		print(r)