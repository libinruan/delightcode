"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

heapq: https://docs.python.org/3/library/heapq.html
Leetcode no.23 <> Jiuzhang no.104

"""
from typing import List
import heapq
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # load input data :: val, list index, first node of a list
        h = [(head.val, idx, head) for idx, head in enumerate(lists) if head is not None]
        heapq.heapify(h)
        # list node boilerplate 
        dummy = ListNode()
        p = dummy
        # primary logic: comparison and update pointers
        while h:
            val, idx, node = heapq.heappop(h)  # 1. pop the minimum value node
            p.next, p = node, node  # 2. save local answer or p.next = node; p = p.next
            if p.next is not None:
                heapq.heappush(h, (p.next.val, idx, p.next))
        return dummy.next