if __name__ == '__main__':

	class Monkey:

		def __init__(self,inp_list):

			self.num = int([i for i in inp_list[0].split(' ')][1][:1])
			self.current_items = [j for j in map(int,[i for i in inp_list[1].split('Starting items: ')][1].split(', '))]
			self.test = int([i for i in inp_list[3].split(' ')][3])
			self.if_true = int([i for i in inp_list[4].split(' ')][5])
			self.if_false = int([i for i in inp_list[5].split(' ')][5])
			self.operation = [i for i in inp_list[2].split('= old ')][1]
			self.passed_items = 0

		def decoded_operation(self,item):

			math_operation, value = self.operation.split(' ')

			if value == 'old':

				return item*item

			elif math_operation == '*':

				return item * int(value)

			else:

				return item + int(value)


		def move(self,monkeys,mod = 1):

			for item in self.current_items:

				worry = self.decoded_operation(item)
				
				if mod == 1:

					worry //= 3

				else:

					worry %= mod

				if worry % self.test == 0:
					monkeys[self.if_true].current_items.append(worry)

				else:
					monkeys[self.if_false].current_items.append(worry)

				self.passed_items += 1


			self.current_items = []


	def generate_monkeys():

		with open('Day 11.txt','r') as txt_file:

			monkeys = []
			inp_list = []

			for line in txt_file.readlines():

				if line.strip() == '':
					continue

				else: 

					inp_list.append(line.strip())


				if len(inp_list) == 6:

					monkeys.append(Monkey(inp_list))
					inp_list = []

		return monkeys

	# Star 1

	star_1_monkeys = generate_monkeys()

	reg_round = 0

	while reg_round < 20:

		for monkey in star_1_monkeys:

			monkey.move(star_1_monkeys)


		reg_round += 1


	passes = []
	for monkey in star_1_monkeys:

		passes.append(monkey.passed_items)

	passes.sort(reverse=True)

	print('Star 1:', passes[0]*passes[1])



	# Star 2

	star_2_monkeys = generate_monkeys()

	mod = 1

	for monkey in star_2_monkeys:

		mod *= monkey.test
		
	mod_round = 0

	while mod_round < 10000:

		for monkey in star_2_monkeys:

			monkey.move(star_2_monkeys,mod)

		mod_round += 1


	new_passes = []
	for monkey in star_2_monkeys:

		new_passes.append(monkey.passed_items)

	new_passes.sort(reverse=True)

	print('Star 2:', new_passes[0]*new_passes[1])
