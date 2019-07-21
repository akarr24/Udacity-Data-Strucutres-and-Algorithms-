"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

import itertools  
import collections 

L1 = [row[0] for row in calls] #list containing caller's phone number
L2 = [row[1] for row in calls] #list containing receiver's phone number
L3 = [int(row[3]) for row in calls] #list conaining call time


tuple1 = zip(L1,L3)
dict1 = {} #creating dictionary for two lists L1 and L3

for key, value in tuple1:
    if key in dict1:
        dict1[key] += value
    else:
        dict1[key] = value

tuple2 = zip(L2, L3)
dict2 = {} #creating dictionary with two lists L2 and L3

for key, value in tuple2:
    if key in dict2:
        dict2[key] += value
    else:
        dict2[key] = value
# using defaultdict 
Cdict = collections.defaultdict(int) 
  
# iterating key, val with chain() 
for key, val in itertools.chain(dict1.items(), dict2.items()): 
    Cdict[key] += val 
      
keymax = max(Cdict, key=Cdict.get)

print(str(keymax) + ' spent the longest time, ' + str(Cdict[keymax]) + ' seconds, on the phone during September 2016.')