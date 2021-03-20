#define _CRT_SECURE_NO_WARNINGS
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include "LinkList.h"

using namespace std;

void test() {
	ListNode* header = Init_LinkList();
	Foreach_LinkList(header);

}

int main() {
	test();

	system("pause");
	return 0;
}