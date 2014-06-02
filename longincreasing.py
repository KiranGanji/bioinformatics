f=open('rosalind_lgis.txt')
raw_data=f.readlines()
f.close()
for line in range(1, len(raw_data)):
	num_init=raw_data[line]
num=[]
num=num_init.split()
i=0
while i<len(num):
	num[i]=int(num[i])
	i=i+1

#Increasing subsequence algorithm
def incr_substr(d):
	l = []
    	for i in range(len(d)):
        	l.append(max([l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], key=len) 
                  + [d[i]])
    	return max(l, key=len)
#Decreasing subsequence algorithm
def dec_substr(d):
	l = []
    	for i in range(len(d)):
        	l.append(max([l[j] for j in range(i) if l[j][-1] > d[i]] or [[]], key=len) 
                  + [d[i]])
    	return max(l, key=len)
a=incr_substr(num)
print ' '.join(str(x) for x in a)
b= dec_substr(num)
print ' '.join(str(x) for x in b)
	
