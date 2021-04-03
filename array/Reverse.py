import os
from os import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')


'''
Reverse an array
123
321

Ways :
1 . inbuilt funtion      O(n)  O(1)
2. two pointer method      O(n/2)    O(1)
3. list comphrehension

3  2  1
   se
Base
steps
s=0
e=n-1
swap
s+=1
e-=1
if s pos == e pos 
break

algo
n=len(a)
1. s=0 e=n-1
2. while s!=e
    swap 
    incre s
    dec e
3.break
return a

'''

def reverseArray(a):
    n=len(a) # to have length of array
    s=0 #pointer at start index 
    e=n-1 # pointer at end index
    while  s<e: # run loop till s<e when it is equal break out
        a[s],a[e]=a[e],a[s]# swapping
        s+=1 # move forward s
        e-=1 # move backward e
    return a 
input_array=list(map(int,input().split()))
print(reverseArray(input_array))
