number = 2 ** 1000
stringnumber = str(number)

total = 0
for digit in stringnumber:
    total+=int(digit)

print(total)
