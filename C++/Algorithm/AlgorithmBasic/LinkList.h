#pragma once
#include <stdlib.h>
#include <iostream>
using namespace std;
//使C++程序可以调用C语言程序
	//定义节点数据类型
struct ListNode {
	int val;
	ListNode* next;
	ListNode(int x) :val(x), next(nullptr) {}
	ListNode() :val(0), next(nullptr) {}
	ListNode(int x, ListNode* next) :val(x), next(next) {}
};
//初始化链表
struct ListNode* Init_LinkList();
//在值为oldval的后面插入一个新的数据newval
void InsertByValue_LinkList(struct ListNode* header,int oldval,int newval);
//删除值为val的节点
void RemoveByValue_LinkList(struct ListNode* header, int delValue);
//遍历链表
void Foreach_LinkList(struct ListNode* header);
//销毁链表
void Destroy_LinkList(struct ListNode* header);
//清空链表
void Clear_LinkList(struct ListNode* header);