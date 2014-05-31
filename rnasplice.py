map = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
       "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
       "TAT":"Y", "TAC":"Y", "TAA":"STOP", "TAG":"STOP",
       "TGT":"C", "TGC":"C", "TGA":"STOP", "TGG":"W",
       "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
       "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
       "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",
       "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
       "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
       "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",
       "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
       "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
       "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
       "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

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
#Unfortunately the above function is not listing the first sequence
#as the first in the list. So swap with the sequence of max length with first index
sequences=parse_fasta('rosalind_splc.txt')
index_max= sequences.index(max(sequences,key=len))
sequences[index_max], sequences[0] = sequences[0], sequences[index_max]

#eradicate all the sequences from the firat sequence from the list

for j in range(1,len(sequences)):
    	k=sequences[0].find(sequences[j])
    	sequences[0]=sequences[0].replace(sequences[j],"")
s=sequences[0]

#Translate the sequence to Protein
start=s.find("ATG")
s2=[]
if start!=-1:
    while start+2<len(s):
        codon=s[start:start+3]
        if codon not in ("TGA","TAA","TAG"):
            s2.append(map[codon])
        else:
            break
        start=start+3
protein=''.join(s2)
print protein


