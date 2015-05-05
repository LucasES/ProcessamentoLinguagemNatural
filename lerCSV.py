import sys

arquivo = sys.argv[1]

with open (arquivo) as f:
	for line in f:
		categoria = line.strip().split('\t')[0]
		idTweet = line.strip().split('\t')[1]
		texto = line.strip().split('\t')[2]		
		dataDeCriacao = line.strip().split('\t')[3]
		print "%s\t%s\t%s\t%s" %(categoria, idTweet, texto, dataDeCriacao)
		
