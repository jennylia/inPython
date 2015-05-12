#!/usr/bin/env bash

# Modified version of the sample framework 

# I'll make sure that all my programs (written in Python in this example) have the proper permissions
chmod a+x ./src/my_word_count.py
chmod a+x ./src/my_running_median.py
chmod +wxr ./wc_output/wc_result.txt
chmod +wxr ./wc_output/med_result.txt

# finally I'll execute my programs, with the input directory wc_input and output the files in the directory wc_output
python ./src/my_word_count.py 
python ./src/my_running_median.py 



