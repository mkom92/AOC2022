from numpy import array, ndenumerate, prod, transpose

if __name__ == '__main__':


	rows = []

	with open('Day 8.txt','r') as txt_file:

		for line in txt_file.readlines():

			rows.append([tree for tree in line.rstrip()])

	grid = array(rows)

	visible_trees = 0

	for index, value in ndenumerate(grid):

		m,n = index
		m_max, n_max = grid.shape

		if m == 0 or n == 0 or m == (m_max-1) or n == (n_max-1):

			visible_trees += 1

		elif value > max(grid[m][:n]) or value > max(grid[m][n+1:]):

			visible_trees += 1

		elif value > max(transpose(grid)[n][:m]) or value > max(transpose(grid)[n][m+1:]):

			visible_trees += 1

	print('Star 1:', visible_trees)


	top_scenic_score = 0


	for index, value in ndenumerate(grid):

		m,n = index

		visibility_list = [0,0,0,0]

		for tree in grid[m][:n][::-1]:

			visibility_list[0] += 1

			if tree >= value:

				break

		for tree in grid[m][n+1:]:

			visibility_list[1] += 1

			if tree >= value:

				break

		for tree in transpose(grid)[n][:m][::-1]:

			visibility_list[2] += 1

			if tree >= value:

				break

		for tree in transpose(grid)[n][m+1:]:

			visibility_list[3] += 1

			if tree >= value:

				break

		score = prod(visibility_list)

		if score > top_scenic_score:

			top_scenic_score = score
			best_vis_list = visibility_list
			best_mn = [m,n]

	print('Star 2:', top_scenic_score)