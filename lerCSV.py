import sys
import itertools


arquivo = sys.argv[1]
counter=itertools.count()
with open (arquivo) as f:
	for line in f:
		#categoria = line.strip().split('\t')[0]
		idTweet = line.strip().split('\t')[0]
		texto = line.strip().split('\t')[1]		
#		dataDeCriacao = line.strip().split('\t')[2]
#		print "%s\t%s\t%s\t%s" %(categoria, idTweet, texto, dataDeCriacao)
		print "%s\t%s\t%s\t%s" %(next(counter),idTweet, texto, dataDeCriacao)
		
