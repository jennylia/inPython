# example of running median program
"""
The important libraries to import
"""

import os
import numpy
import functools
import heapq
from heapq import heapify, heappush, heappop, _heapify_max,_siftup_max
import sys

#Set up
curMedian = 0
leftHeap = []
rightHeap = []
heapq.heapify(rightHeap)
heapq.heapify(leftHeap)

def runningMed(n):
	#importing the global variables
	global curMedian 
	global leftHeap
	global rightHeap
	#The first time
	if (curMedian == 0):
		curMedian = n
		return curMedian

	#the second +... time
	if (len(rightHeap) > len(leftHeap)):
		if(n >= curMedian):
			heapq.heappush(leftHeap, -curMedian)

			tryMedian = rightHeap[0]
			if (tryMedian > n):
				curMedian = n
			else:
				curMedian = heapq.heappop(rightHeap)
				heapq.heappush(rightHeap, n) 

		else:
			heapq.heappush(leftHeap,-n)
	elif (len(leftHeap) > len(rightHeap)):
		if(n <= curMedian):
			heapq.heappush(rightHeap, curMedian)

			tryMedian = -leftHeap[0]
			if (tryMedian < n):
				curMedian = n
			else:
				curMedian = -heapq.heappop(leftHeap)
				heapq.heappush(leftHeap, -n)
		else:
			heapq.heappush(rightHeap,n)

	else:
		if (n > curMedian):
			heapq.heappush(rightHeap, n)

		else:
			heapq.heappush(leftHeap, -n)


	if (len(leftHeap) == len(rightHeap)):
		return curMedian
	elif (len(leftHeap) > len(rightHeap)):
		if(len(leftHeap)>0):
			return ((-leftHeap[0] + curMedian)/2)
	else:
		if(len(rightHeap)>0):
			return ((rightHeap[0] + curMedian)/2)


def read_files(dir):
	out = open('wc_output/med_result.txt', 'w')
	for root, dirs, files in os.walk(dir):
		for name in files:
			print(os.path.join(root, name))
			f = open (os.path.join(root, name), "r")
			for line in f:
				print line
				lc = len(line.split())
				med = runningMed(float(lc))
				out.write(str(med) + '\n')
			f.close()

	
	out.close()
	print "please check med_result.txt now"


if __name__ == "__main__":
	print "starting the running median"
	read_files("wc_input")
