import os
from os import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
import heapq
'''
Max and min --O(n)
add all elements to minheap top element is min
multiply heap with -1
and return min again x-1 which is max
'''

def maxMin(a):
    heap=[]
    for i in a:
        heapq.heappush(heap,i)
    min_val=heap[0]
    max_val=heap[-1]
    return min_val,max_val
    
input_array=list(map(int,input().split()))
print(maxMin(input_array))