# -----------------------stack -------------------------------------------
import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#----------------------------------------------------------------------------
'''
next largest to the right 
'''




class Solution:
    def __init__(self):
        self.stack=[]
    def function1(self):
        return self.empty()
    def helperfunction(self):
        return
    def top(self):
        return self.stack[-1]
    def empty(self):
        if self.stack=[]:
            return True
        else:
            return False

instance=Solution()
print(instance.function1())

'''
# input section
n=int(input())
for _ in range(n):
    list_input=list(map(int,input().split()))
'''



