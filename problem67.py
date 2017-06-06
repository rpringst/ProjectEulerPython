with open('p067_triangle.txt') as f:
	data = []
	for line in f:
		data.append([int(x) for x in line.split()])

for row in data:
	print(row)
