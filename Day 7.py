if __name__ == '__main__':

	directories = {}
	current_dir = ''
	current_path = []

	with open('Day 7.txt','r') as txt_file:

		for line in txt_file.readlines():

			if line.rstrip() == '$ cd ..':

				current_path.pop()

			elif line[:4] == '$ cd':

				current_path.append(line.rstrip()[5:])
				current_dir = '/'.join(current_path)
				directories[current_dir] = 0

			elif line[:4] != '$ ls' and line[:3] != 'dir':

				val = int(line.rstrip().split(' ')[0])

				cur_dir = ''

				for next_dir in current_path:

					cur_dir = '/'.join([cur_dir,next_dir])
					directories[cur_dir[1:]] += val


	below_100k = 0

	space_to_free = 30000000 - (70000000 - directories['/'])
	current_smallest = 999999999

	for key, value in directories.items():
		if value <= 100000:

			below_100k += value 

		if value >= space_to_free and value < current_smallest:

			current_smallest = value

	print('Star 1:',below_100k)

	print('Star 2:',current_smallest)

