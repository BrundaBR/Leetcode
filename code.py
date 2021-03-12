#----------imports-------------------------------------------------------
import sys
from heapq import heappush, heappop,heapify
from collections import defaultdict
import math
import itertools 
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')
#----------------------------------------------------------------------------

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_node(self,data):
        new_node=Node(data)
        hd=self.head
        if self.head is None:
            self.head=new_node
            return
      
        while hd.next:
            hd=hd.next
        hd.next=new_node

        

    def insert_at_position(self,data,pos):
        new_node=Node(data)#new node to insert 5
        idx=0
        cur=self.head
        while idx!=pos:
            cur=cur.next
            idx=idx+1
        new_node.next=cur.next
        cur.next=new_node

    def print_node(self):
        cur=self.head
        while cur:
            print(cur.data,end=" ")
            cur=cur.next


    def node_at_begin(self,data):
        new_node=Node(data)
        cur=self.head
        new_node.next=cur
        self.head=new_node



instance=LinkedList()
instance.insert_node(9)
instance.insert_node(10)
instance.print_node()
instance.insert_at_position(5,0)
instance.print_node()

instance.node_at_begin(1)
instance.print_node()




































































# class Solution:
#     def __init__(self):
#         self.stack=[]
#         self.minHeap=[]
    







'''
# input section

n=int(input())
for _ in range(n):
    list_input=list(map(int,input().split()))
'''















