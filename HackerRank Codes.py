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

