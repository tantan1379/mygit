#include "LinkList.h"

//初始化链表
ListNode* Init_LinkList() {
	//头指针
	ListNode* header = new ListNode(0);
	//尾指针
	ListNode* pRear = header;
	int value = 0;
	while (1) {
		cout << "请输入链表的元素值" << endl;
		cin >> value;
		if (value == -1) {
			break;
		}
		//尾插法
		ListNode* newNode = new ListNode(value);
		pRear->next = newNode;
		//尾部节点更新
		pRear = pRear->next;
	}
	return header;

}
//在值为oldval的后面插入一个新的数据newval
void InsertByValue_LinkList(struct ListNode* header, int oldval, int newval) {

}
//删除值为val的节点
void RemoveByValue_LinkList(struct ListNode* header, int delValue) {

}
//遍历链表
void Foreach_LinkList(struct ListNode* header) {
	if (nullptr == header) {
		return;
	}
	ListNode* pCurrent = header->next;
	while (pCurrent != nullptr) {
		cout << pCurrent->val << endl;
		pCurrent = pCurrent->next;
	}
}
//销毁链表
void Destroy_LinkList(struct ListNode* header) {

}
//清空链表
void Clear_LinkList(struct ListNode* header) {

}