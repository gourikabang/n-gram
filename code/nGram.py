import math, re, csv
import glob
import pandas as pd
import numpy as np
from itertools import zip_longest
from collections import Counter
from functools import reduce
from blum import Filter
from file import new_read, new_write
from datetime import datetime


def tokenize(file):
	for line in open(file):
		line = line.rstrip()
		token = line.split()
	return token

def chunk_list(lst, n):
    return [tuple(lst[i:i+n]) for i in range(len(lst)-n)]

def count_ngram_30per(arr, key, n):
	ngram_counts = []
	i=1
	for num, count in arr:
		if count >= key and i<=n: 
			ngram_counts.append(num)
			i+=1
	return ngram_counts

def count_ngrams(tokens, n):
    ngram_counts = []
    k = []
    n_gram = {}
    for ngram, count in Counter(chunk_list(tokens, n)).items():
    	ngram_counts.append((ngram, count))
    	k.append(count)
    	n_gram[str(ngram)]=count
    return ngram_counts, n_gram, k

def nGram(file, n):
	start_time = datetime.now()
	l=tokenize(file)
	s, d, k = count_ngrams(l, n)
	end_time = datetime.now()
	
	for tup in s:
		print(*tup)
	print('Duration: {}'.format(end_time - start_time))
	m = (len(s)*3)//10
	key = Filter(k)
	t = count_ngram_30per(s,key, m)
	return d, t
