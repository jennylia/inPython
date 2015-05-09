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
	print "***************Start Right Here******************"
	print "***n is: " + str(n)
	print "***curMedian is: " + str(curMedian)
	print "rightHeap length: " + str(len(rightHeap))
	print "leftHeap: " + str(len(leftHeap))
	print "rightHeap is: "
	print rightHeap
	print "leftHeap is: "
	print leftHeap

	print "Coding"
	if (len(rightHeap) > len(leftHeap)):
		print "===RIGHT LONGER==="
		print "n is: " + str(n)
		print "curMedian is: " + str(curMedian)
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
		print "===LEFT LONGER==="
		print "n is: " + str(n)
		print "curMedian is: " + str(curMedian)
		if(n <= curMedian):
			heapq.heappush(rightHeap, curMedian)
			print "$$$$$$$$$$$ Pay attention Left Heap"
			print leftHeap
			print "$$$$$$$$$$$ Pay attention Right Heap"
			print rightHeap
			#curMedian = -heapq.heappop(leftHeap)
			#what is the current Median is still smaller
			tryMedian = -leftHeap[0]
			if (tryMedian < n):
				curMedian = n
			else:
				curMedian = -heapq.heappop(leftHeap)
				heapq.heappush(leftHeap, -n)
			print "$$$$$$$$$$$ Pay attention CurMeidan"
			print curMedian
            #curMedian = left[0]
		else:
			heapq.heappush(rightHeap,n)

	else:
		print "===EQUAL || < 1 Diff LENGTH==="
		print "n is: " + str(n)
		print "curMedian is: " + str(curMedian)
		if (n > curMedian):
			heapq.heappush(rightHeap, n)
			print "$$$$$$$$$$$ Pay attention Left Heap"
			print leftHeap
			print "$$$$$$$$$$$ Pay attention Right Heap"
			print rightHeap
		else:
			heapq.heappush(leftHeap, -n)
			print "$$$$$$$$$$$ Pay attention Left Heap"
			print leftHeap
			print "$$$$$$$$$$$ Pay attention Right Heap"
			print rightHeap

	#TReturn the median:
	#This logic is more suited for added

	print "*****RETURNING MEDIAN*****"
	if (len(leftHeap) == len(rightHeap)):
		print "===EQUAL LENGTH==="
		print "Returned Median: " + str(curMedian)
		return curMedian
	elif (len(leftHeap) > len(rightHeap)):
		if(len(leftHeap)>0):
			print "@@leftHeap [0]"
			print leftHeap[0]
			print leftHeap
			heapq.heapify(leftHeap)
			print "@@leftHeap [0]"
			print leftHeap[0]
		print "===LEFT LONGER==="
		print "Returned Median: " + str(((-leftHeap[0] + curMedian)/2))
	
		return ((-leftHeap[0] + curMedian)/2)
	else:
		if(len(rightHeap)>0):
		#return (heapq.heappop(leftHeap) + curMedian)/2
			print "@@rightHeap [0]"
			print rightHeap[0]
		print "===RIGHT LONGER==="
		print "Returned Median: " + str(((rightHeap[0] + curMedian)/2))
		return ((rightHeap[0] + curMedian)/2)
		#return (heapq.heappop(rightHeap) + curMedian)/2
	# the real one be like, if eqal length return med
	#else return average of media and the longer one

def read_files(dir):
	out = open('wc_output/med_result.txt', 'w')
	inputlen = open('wc_output/med_input.txt', 'w')
	for root, dirs, files in os.walk(dir):
		for name in files:
			print(os.path.join(root, name))
			f = open (os.path.join(root, name), "r")
			for line in f:
				print len(line.split())
				lc = len(line.split())
				inputlen.write(str(lc))
				med = runningMed(float(lc))
				out.write(str(med) + '\n')
			f.close()

	
	inputlen.close()
	out.close()
	print "please check med_result.txt now"


if __name__ == "__main__":
	print "starting the running median"
	read_files("wc_input")
