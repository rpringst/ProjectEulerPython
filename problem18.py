def reduce_and_combine(lower, upper):
	if len(lower) <= len(upper):
		print('Error!')
		return
	else:
		new = []
		for i in range(len(lower)-1):
			if lower[i] >= lower[i+1]:
				new.append(lower[i])
			else:
				new.append(lower[i+1])
	return [sum(x) for x in zip(upper, new)]
		

with open('p018_triangle.txt') as f:
	data = []
	for line in f:
		data.append([int(x) for x in line.split()])

results = list(data)

for i in range(len(data)-1, 0, -1):
	print(i)
	results[i-1] = reduce_and_combine(results[i], results[i-1])
	
for row in data:
	print(row)
	
for row in results:
	print(row)
