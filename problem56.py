def a_tothe_b(a, b):
	return a ** b

def sum_of_digits(x):
	string_representation = str(x)
	sum = 0
	for digit in string_representation:
		sum+=int(digit)
	return sum

def main(args):
	maxsum = 0
	for a in range(100):
		for b in range(100):
			print(str(a) + ' to the ' + str(b))
			ab = a_tothe_b(a,b)
			sumofdigits = sum_of_digits(ab)
			if sumofdigits > maxsum:
				maxsum = sumofdigits
	print(maxsum)
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
