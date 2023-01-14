if __name__ == '__main__':

	with open('Day 6.txt','r') as txt_file:

		inp_string = txt_file.read()

	def detect_packet(n):

		m = n

		while True:

			test = inp_string[n-m:n]

			if len(list(set(test))) == len(test):

				break

			n+=1

		return n, test


	star1 = detect_packet(4)
	star2 = detect_packet(14)

	print('Star 1:',star1)
	print('Star 2:',star2)
