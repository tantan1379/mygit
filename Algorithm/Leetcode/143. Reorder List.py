'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.
'''

from utils import ListNode, InitLinkList, ForeachLinkList


def reorderList(head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    if(not head or not head.next):
        return head
    newlist = []
    cur = head
    while(cur):
        newlist.append(cur)
        cur = cur.next
    i = 0
    j = len(newlist)-1
    while i < j:
        newlist[i].next = newlist[j]
        i += 1
        if i == j:
            break
        newlist[j].next = newlist[i]
        j -= 1
    newlist[i].next = None
    return head


# fast and slow pointer
def reorderList_(head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    if(not head or not head.next):
        return head
    # step1: find the midpoint
    fast,slow = head,head
    while(fast.next and fast.next.next):
        fast = fast.next.next
        slow = slow.next
    mid = slow
    # step2: split the linklist
    l1 = head
    l2 = mid.next
    slow.next = None
    # step3: inverse the second linklist
    cur = l2
    prev = None
    while(cur):
        pnext = cur.next
        cur.next = prev
        prev = cur
        cur = pnext
    l2 = prev
    # # step4: merge the two linklist
    res = l1
    while(l1 and l2):
        temp1 = l1.next
        temp2 = l2.next
        l1.next = l2
        l1 = temp1
        l2.next = l1
        l2 = temp2
    return head

if __name__ == "__main__":
    myarr = [1, 2, 3, 4, 5,6]
    head = InitLinkList(myarr)
    ForeachLinkList(head)
    # newhead1,newhead2 = reorderList_(head)
    # ForeachLinkList(newhead1)
    # ForeachLinkList(newhead2)
    res = reorderList_(head)
    ForeachLinkList(res)