numbers=raw_input('Enter the numbers\n').split()
i=0
while i<len(numbers):
	numbers[i]=int(numbers[i])
	i=i+1
p=float((2*numbers[0]*1)+(2*numbers[1]*1)+(2*numbers[2]*1)+float(2*numbers[3]*0.75)+float(2*numbers[4]*0.5))
print p
