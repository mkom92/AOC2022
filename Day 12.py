if __name__ == '__main__':

	import numpy as np 
	import heapq

	grid_lists = []

	def decode_symbol(x):

		if x == 'S':
			return 0
		elif x == 'E':
			return 27
		else:
			return ord(x) - 96

	with open('Day 12.txt','r') as txt_file:

		for line in txt_file.readlines():

			grid_lists.append([decode_symbol(i) for i in line.strip()])

	grid = np.array(grid_lists)

	s_n, s_m = np.where(grid == 0)
	e_n, e_m = np.where(grid == 27)

	start = (s_n[0],s_m[0])
	end = (e_n[0],e_m[0])


	def neighbours(point,grid,dire):

		n,m = grid.shape
		xn,ym = point
		directions = [(1,0),(-1,0),(0,1),(0,-1)]
		adjacent = []

		for d in directions:

			x,y = point[0]+d[0], point[1]+d[1]


			if 0 <= x < n and 0 <= y < m:

				if dire == 'up' and grid[x][y] - grid[xn][ym] < 2:

					adjacent.append((x,y))

				elif dire == 'down' and grid[xn][ym] - grid[x][y] < 2:

					adjacent.append((x,y))

		return adjacent


	def djikstra(start,grid,dire,end = (99,99), end_val = 99):

		visited = set()
		pq = [(0,start,())]
		last_1 = 0

		while pq:

			steps, point, path = heapq.heappop(pq)

			if point not in visited:

				visited.add(point)
				path = (point,path)

				if end_val == 99:
					if point == end: 
						print(steps)
						break

				else:
					n,m = point
					if grid[n][m] == end_val:
						print(steps)
						break

				for point2 in neighbours(point,grid,dire):

					if point2 not in visited: 
						
						heapq.heappush(pq, (steps+1, point2, path))



	print('Star 1:') 
	djikstra(start,grid,'up',end)

	print('Star 2:')
	djikstra(end,grid,'down',end_val = 1)

