def parse_fasta(filename):
    f = open(filename)
    sequences = {}
    for line in f:
        if line.startswith('>'):
            name = line[1:].rstrip('\n')
            sequences[name] = ''
        else:
            sequences[name] = sequences[name] + line.rstrip('\n')
    return sequences.values()
seq=parse_fasta('rosalind_tran.txt')
i=0
transi=0
transv=0
while i<len(seq[0]):
	if (seq[0][i]== 'A' and seq[1][i]=='G') or (seq[0][i]== 'C' and seq[1][i]=='T'):
		transi+=1
	elif (seq[0][i]== 'A' and seq[1][i]=='T') or (seq[0][i]== 'A' and seq[1][i]=='C') or (seq[0][i]== 'G' and seq[1][i]=='T') or (seq[0][i]== 'G' and seq[1][i]=='C'):
		transv+=1
	elif (seq[0][i]== 'G' and seq[1][i]=='A') or (seq[0][i]== 'T' and seq[1][i]=='C'):
		transi+=1
	elif (seq[0][i]== 'C' and seq[1][i]=='A') or (seq[0][i]== 'C' and seq[1][i]=='G') or (seq[0][i]== 'T' and seq[1][i]=='A') or (seq[0][i]== 'T' and seq[1][i]=='G'):
		transv+=1
	i=i+1

print float(transi)/float(transv)

#This happens to be the worst algorithm I have have ever coded. So have to recode this in
#future.And so I am wrting the commit as to be coded again.	
