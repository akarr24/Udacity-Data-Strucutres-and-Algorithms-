"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
L1 = [col[0] for col in texts] #list containing text senders' numbers
L2 = [col[0] for col in calls] #list containing callers' numbers 
L3 = [col[1] for col in texts] #list containing text receivers' numbers
L4 = [col[1] for col in calls] #list containing receivers' numbers

telemarketers = [] #empty list to contain telemarketers numbers

telemarketers = list(set(L2) - set(L4) - set(L1) - set(L3))

#print(telemarketers)

#removing duplicates
clean_list = []
for i in range(len(telemarketers)):
    if telemarketers[i] not in clean_list:
        clean_list.append(telemarketers[i])

#Sorting the clean list
sorted_list = sorted(clean_list)

#printing the list
print('These numbers could be telemarketers: ')
for i in sorted_list:
    print(i)