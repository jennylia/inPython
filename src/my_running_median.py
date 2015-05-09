# example of running median program
import sys
import os


def read_files(dir):
	for root, dirs, files in os.walk(dir):
		for name in files:
			print(os.path.join(root, name))
			f = open (os.path.join(root, name), "r")
			for line in f:
				print len(line.split())
			f.close()

	
	out = open('wc_output/med_result.txt', 'w')
	
	out.close()
	print "please check wc_result.txt now"


if __name__ == "__main__":
	print "starting the running median"
	read_files("wc_input")