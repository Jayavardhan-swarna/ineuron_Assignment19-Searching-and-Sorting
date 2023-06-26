import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i))

    dummy = ListNode()
    curr = dummy

    while heap:
        _, i = heapq.heappop(heap)
        curr.next = lists[i]
        curr = curr.next
        lists[i] = lists[i].next
        if lists[i]:
            heapq.heappush(heap, (lists[i].val, i))

    return dummy.next


# Example 1
lists = [ListNode(1, ListNode(4, ListNode(5))),
         ListNode(1, ListNode(3, ListNode(4))),
         ListNode(2, ListNode(6))]
merged_list = mergeKLists(lists)
while merged_list:
    print(merged_list.val, end=' ')
    merged_list = merged_list.next
# Output: 1 1 2 3 4 4 5 6

# Example 2
lists = []
merged_list = mergeKLists(lists)
while merged_list:
    print(merged_list.val, end=' ')
    merged_list = merged_list.next
# Output: 

# Example 3
lists = [[]]
merged_list = mergeKLists(lists)
while merged_list:
    print(merged_list.val, end=' ')
    merged_list = merged_list.next
# Output: 
