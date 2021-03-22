#pragma once
#define _CRT_SECURE_NO_WARNINGS
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;
struct ListNode {
public:
	int val;
	ListNode* next;
	ListNode(int x, ListNode* next) :val(x), next(next) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode() :val(0), next(nullptr) {}
};
ListNode* AddTwoNumbers(ListNode* l1, ListNode* l2);
ListNode* Init_LinkList();
void Foreach_LinkList(ListNode* header);
void test002();