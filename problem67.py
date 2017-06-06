from timeit import default_timer as timer

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

with open('p067_triangle.txt') as f:
	data = []
	for line in f:
		data.append([int(x) for x in line.split()])

best_time = 10000.0
worst_time = 0.0
time_sum = 0.0

for execution in range(10000):
	start = timer()
	
	results = list(data)
	
	for i in range(len(data)-1, 0, -1):
		results[i-1] = reduce_and_combine(results[i], results[i-1])
	
	end = timer()
	
	duration = end - start
	
	print('Execution time (seconds): ' + str(duration))
	
	if duration > worst_time: worst_time = duration
	elif duration < best_time: best_time = duration
	time_sum+=duration
	
print(results[0][0])
print('Best Execution time (seconds): ' + str(best_time))
print('Worst Execution time (seconds): ' + str(worst_time))
print('Avg Execution time (seconds): ' + str(time_sum/10000.0))
	
