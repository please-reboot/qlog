# Title: qlog.py
# Date:07-09-2020
# Author: Rohde

with open('.\example.log') as log_data:
    for line in log_data:
        #print(line[19:]) #using an index
        print(line.split(':') [3])# using split and an index

    