#include "ll.h"
#include <iostream>

using namespace std;

//初始化链表
struct ListNode* Init_LinkList() {
	ListNode* header = new ListNode(0);
	ListNode* pRear = header;
	int val = -1;
	while (1) {
		cout << "请输入链表的元素：" << endl;
		cin >> val;
		if (val == -1) {
			break;
		}
		pRear->next = new ListNode(val);
		pRear = pRear->next;
	}
	return header;
}

//遍历链表
void Foreach_LinkList(struct ListNode* header) {
	if (nullptr == header) {
		return;
	}
	ListNode* pCurrent = header->next;
	while (pCurrent) {
		cout << pCurrent->val << " ";
		cout << endl;
		pCurrent = pCurrent->next;
	}
}