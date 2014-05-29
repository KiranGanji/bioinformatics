import itertools
n=raw_input('Enter the number')
array=[]
for i in range(1,int(n)+1):
	array.append(i)
permu=list(itertools.permutations(array))
i=0
fo=open('output.txt','a')
fo.write(str(len(permu)))
fo.write('\n')
while i<len(permu):
	fo.write(str(permu[i]).replace('(','').replace(',','').replace(')',''))
	fo.write('\n')
	i=i+1
fo.close()
