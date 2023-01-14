
# Star 1

round_result_points = {
	'A': {'X': 3, 'Y': 6, 'Z': 0}
	, 'B': {'X': 0, 'Y': 3, 'Z': 6}
	, 'C': {'X': 6, 'Y': 0, 'Z': 3}
}

shape_points ={
	'X': 1
	, 'Y': 2
	, 'Z': 3
}

# Star 2

points = {
	'A': {'X': 0+3, 'Y': 3+1, 'Z': 6+2}
	, 'B': {'X': 0+1, 'Y': 3+2, 'Z': 6+3}
	, 'C': {'X': 0+2, 'Y': 3+3, 'Z': 6+1}
}

total_score = 0
total_score_2 = 0

with open('Day 2.txt','r') as txt_file:

	for line in txt_file.readlines():

		n = line.rstrip().split()
		total_score += round_result_points[n[0]][n[1]] + shape_points[n[1]]

		total_score_2 += points[n[0]][n[1]]

print("Star 1:",total_score)
print("Star 2:",total_score_2)