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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

records = []
L1 = [col[0] for col in texts] #list containing  text senders numbers
L2 = [col[1] for col in texts] #list containing text receivers numbers
L3 = [col[0] for col in calls] #list containing callers' numbers
L4 = [col[1] for col in calls] #list conataining receivers' numbers

for i in range(len(L1)):
    if L1[i] not in records:
        records.append(L1)

for i in range(len(L2)):
    if L2[i] not in records:
        records.append(L2[i])

for i in range(len(L3)):
    if L3[i] not in records:
        records.append(L3[i])

for i in range(len(L4)):
    if L4[i] not in records:
        records.append(L4[i])


print('There are ' + str(len(records)) + ' different telephone numbers in the records.')        
