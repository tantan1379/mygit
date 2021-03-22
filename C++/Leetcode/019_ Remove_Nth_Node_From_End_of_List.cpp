#include "ll.h"

//删除链表的倒数第N个节点
ListNode* Remove_Nth_Node_From_End_of_List(ListNode* header, int n) {
	ListNode* dummy = new ListNode(0, header);
	ListNode* fast = dummy;
	ListNode* slow = dummy->next;
	for (int i = 0; i < n; i++) {
		fast = fast->next;
	}
	while (fast) {
		slow = slow->next;
		fast = fast->next;
	}
	slow->next = slow->next->next;
	ListNode* ans = dummy->next;
	return ans;
}