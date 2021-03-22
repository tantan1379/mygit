#include "ll.h"

//将两个链表按位相加
ListNode* AddTwoNumbers(ListNode* l1, ListNode* l2) {
	ListNode* dummy = new ListNode(0);
	ListNode* pCurrent = dummy;
	ListNode* newPoint = new ListNode(0);
	int carry = 0;
	while (l1 || l2 || carry) {
		int target = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + carry;
		carry = target / 10;
		newPoint->val = target % 10;
		pCurrent->next = newPoint;
		pCurrent = newPoint;
		if (l1) l1 = l1->next;
		if (l2) l2 = l2->next;

	}
	ListNode* ans = dummy->next;
	delete dummy;
	delete newPoint;
	return ans;
}

void test002() {
	ListNode* l1 = Init_LinkList();
	ListNode* l2 = Init_LinkList();
	ListNode* target = AddTwoNumbers(l1, l2);
	Foreach_LinkList(target);
}