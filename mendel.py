k1,m1,n1=raw_input('Enter the number of homozyous dominant, hetero and recessive\n').split()
k=int(k1)
m=int(m1)
n=int(n1)
t=k+m+n
p=1-(float((m*m)+(4*(n*n))+(4*m*n)-(4*n)-m)/float(4*t*(t-1)))
print p
