# example of word_count program
import collections
from collections import Counter
import sys
import os
from operator import itemgetter

cnt = Counter()

def read_files(dir):
	global cnt
	for root, dirs, files in os.walk(dir):
		for name in files:
			print(os.path.join(root, name))
			f = open (os.path.join(root, name), "r")
			for line in f:
				line = (line.lower())
				line = line.replace(',','')
				line = line.replace('.','')
				for word in line.split():
					cnt[word] += 1
			f.close()

	
	out = open('wc_output/wc_result.txt', 'w')
	cnt = sorted(cnt.items(), key=itemgetter(0))
	print cnt
	for x in cnt:
		print x[0] 
		print x[1]
		out.write(x[0] +" "+ str(x[1]) + '\n')

	out.close()






if __name__ == "__main__":
	read_files("wc_input")