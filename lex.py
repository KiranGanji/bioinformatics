from itertools import product
array=[]
array=raw_input('Enter the different symbols\n').split()
num=int(raw_input('Enter the number which you can use the string for\n'))
array2= ''.join(array)
def lex(array,num):
	permlist= ([x for x in product(array, repeat=num)])
	fo=open('output.txt','w')
	for i in permlist:
		fo.write(''.join(i))
		fo.write('\n')
	fo.close()
lex(array2,num)
	
