import os
from os import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
import heapq

'''
Max and min --O(n)
METHOD 1 (Simple Linear Search) 
Initialize values of min and max as minimum and maximum of the first two elements respectively. Starting from 3rd, compare each element with max and min, and change max and min accordingly (i.e., if the element is smaller than min then change min, else if the element is greater than max then change max, else ignore the element

'''
def maxMin(a):
    
    # init min and max
    if len(a)>2:
        minimum=a[0]
        maximum=a[1]
        for i in range(2,len(a)):
            if a[i]<minimum:
                minimum=a[i]
            elif a[i]>maximum:
                maximum=a[i]
        return minimum,maximum
    elif len(a)==1:
        return 0
    elif len(a)<=2:
        if a[0] < a[1]:
            minimum=a[0]
            maximum=a[1]
            return minimum,maximum
        else:
            minimum=a[1]
            maximum=a[0]
            return minimum,maximum

input_array=list(map(int,input().split()))
print(maxMin(input_array))