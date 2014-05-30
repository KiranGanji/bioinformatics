import itertools
n=int(raw_input('Enter the number'))
array=[]

for i in range(-(int(n)),int(n)+1):
	array.append(i)
#have to remove the 0 element from the array of numbers
array.pop(n)
#list the permutations which have duplications like (-2,2)
permu=list(itertools.permutations(array,n))
permu2=[]
#delete the duplications
for element in permu:
	k=0
	for j in element:
		if((j in element)&((j*-1)in element)):
			k=1
			break
	if k==0:
		permu2.append(element)
#write to the file
i=0
fo=open('output.txt','a')
fo.write(str(len(permu2)))
fo.write('\n')
while i<len(permu2):
	fo.write(str(permu2[i]).replace('(','').replace(',','').replace(')',''))
	fo.write('\n')
	i=i+1
fo.close()
