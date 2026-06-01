## Problem Statement 01

"""Count Elements Greater Than Previous Average
Given an array of positive integers, return the number of elements that are strictly greater 
than the average of all previous elements. Skip the first element.
Example :
Input:
responseTimes = [100, 200, 150,300]
Output: 2
"""

## Solution

#!/bin/python3

import math
import os
import random
import re
import sys
def countResponseTimeRegressions(responseTimes):
    if not responseTimes or len(responseTimes) < 2:
        return 0
    count =0
    avg=0
    prevnum=responseTimes[0]
    for i in range(1,len(responseTimes)):
        avg= prevnum/i
        
        if avg< responseTimes[i]:
            count+=1
        prevnum+=responseTimes[i]
    return count     
        

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
  go


"""
Find the Smallest Missing Positive Integer
Given an unsorted array of integers, find the smallest positive integer not present in the array in O(n) time and O(1) extra space.
Example
Input:
orderNumbers = [3, 4, -1, 1]
Output: 2
"""


## Solution

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findSmallestMissingPositive' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY orderNumbers as parameter.
#

def findSmallestMissingPositive(orderNumbers):
    listlength =len(orderNumbers)
    for i in range(listlength):
        while 1 <= int(orderNumbers[i]) <= listlength and orderNumbers[int(orderNumbers[i]) - 1] != orderNumbers[i]:
            correct_idx = int(orderNumbers[i]) - 1
            orderNumbers[i], orderNumbers[correct_idx] = orderNumbers[correct_idx], orderNumbers[i]
    
            
    # Write your code here
    for i in range(len(orderNumbers)):
        if int(orderNumbers[i]) != i + 1:
            return i + 1
    return len(orderNumbers)+1

if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)
go

