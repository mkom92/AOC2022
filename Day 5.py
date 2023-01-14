if __name__ == '__main__':

	def get_input():

		# Get your stacks of crates

		with open('Day 5.txt','r') as txt_file:

			crates = [next(txt_file).rstrip() for _ in range(10)]
			moves = [line.rstrip() for line in txt_file.readlines()]

		# Organise stacks

		stacks = []

		for _ in range(9):

			stacks.append([])

		crates.reverse()

		for row in crates[2:]:

			for n in range(9):

				val = row[n*4 + 1]


				if ord(val) > 50:

					stacks[n].append(val)

		return stacks, moves


	# Move crates to new stacks

	stacks1, moves = get_input()

	for inp_str in moves:

		inp_split = inp_str.split(' ')

		v1,v2,v3 = int(inp_split[1]),int(inp_split[3])-1,int(inp_split[5])-1

		for _ in range(v1):
			move_val = stacks1[v2].pop()
			stacks1[v3].append(move_val)

	password1 = ''

	for stack in stacks1:

		password1 += stack[-1]
		print(stack)

	print('Star 1:',password1)

	# Move crates to new stacks with new logic

	stacks2, moves = get_input()

	for inp_str in moves:

		inp_split = inp_str.split(' ')

		v1,v2,v3 = int(inp_split[1]),int(inp_split[3])-1,int(inp_split[5])-1

		move_vals = stacks2[v2][-v1:]
		stacks2[v3].extend(move_vals)
		stacks2[v2] = stacks2[v2][:-v1]


	password2 = ''

	for stack in stacks2:

		password2 += stack[-1]
		print(stack)

	print('Star 2:',password2)


