if __name__ == '__main__':

	from json import loads 
	pairs = []
	all_packets = [[[2]],[[6]]]

	with open('Day 13.txt','r') as txt_file:

		pair = []

		for line in txt_file.readlines():

			if line == '\n':

				pass

			else:

				inp_packet = loads(line.strip())

				all_packets.append(inp_packet)
				pair.append(inp_packet)

				if len(pair) == 2:

					pairs.append(pair)
					pair = []

	def compare_ints(x,y):


		if x > y:
			result = 0

		elif x < y:
			result = 1

		else:
			result = 99

		return result


	def compare_arrays(pair):

		ar1, ar2 = pair

		n = 0
		result = 99
		while True:

			try:
				x, y = ar1[n], ar2[n]

			except:

				try:

					x = ar1[n]
					return 0

				except:

					try:

						y = ar2[n]
						return 1

					except:
						break

			if type(x) == type(y):

				if type(x) == list:

					result = compare_arrays([x,y])

				else:

					result = compare_ints(x,y)

			else:

				if type(x) == list:

					result = compare_arrays([x,[y]])

				else:

					result = compare_arrays([[x],y])

			if result < 99:

				return result
			
			else:
				n += 1

		return result

	correct_pairs = 0

	for num, p in enumerate(pairs):

		test = compare_arrays(p)

		if test == 1:

			correct_pairs += num+1


	print('Star 1:',correct_pairs)


	test_packets = [[[2]],[[6]]]
	positions = []

	for packet in test_packets:

		position = 1

		for other_packet in all_packets:

			if packet == other_packet:
				pass 
			else:
				position += compare_arrays([other_packet,packet])

		positions.append(position)

	print('Star 2:',positions[0]*positions[1])