import sys

arquivo = sys.argv[1]
s = set()

with open (arquivo) as f:
	for line in f:
#		if line not in s:
		categoria = line.strip().split('\t')[0]
		corpo = line.strip().split('\t')[1]	
		print categoria, corpo
#			novoArquivo.write(categoria+"\t"+corpo+"\n")				
#			s.add(line)						
