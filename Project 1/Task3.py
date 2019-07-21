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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

#Part A

call_list = []

for i in range(len(calls)):
        if calls[i][0][0:5] == "(080)":
            if calls[i][1][0] == '(':
                if calls[i][1][0] == '(' and calls[i][1][4] == ')':
                    call_list.append(calls[i][1][1:4])
                elif calls[i][1][0] == '(' and calls[i][1][5] == ')':
                    call_list.append(calls[i][1][1:5])
                else:
                    call_list.append(calls[i][1][1:6])
            elif calls[i][1][0] in ('7', '8', '9'):
                call_list.append(calls[i][1][0:4])
            

#removing duplicates
clean_list = []
for i in range(len(call_list)):
    if call_list[i] not in clean_list:
        clean_list.append(call_list[i])

#sorting the list
sorted_list = sorted(clean_list)

#printing elements in lexicographic order
for i in sorted_list:
    print(i)


#Part B

from_bangalore = [] #list containing all calls originating from bangalore
for i in range(len(calls)):
    if calls[i][0][0:5] == '(080)':
        from_bangalore.append(calls[i][0])

to_bangalore = [] #list containing all calls from bangalore to bangalore
for i in range(len(calls)):
        if calls[i][0][0:5] == '(080)' and calls[i][1][0:5] == '(080)':
            to_bangalore.append(calls[i][1])

per_calls = (len(to_bangalore) / len(from_bangalore)) * 100

print('%.2f  percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.' % per_calls)
