#define _CRT_SECURE_NO_WARNINGS
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

struct ListNode {
public:
	ListNode(int x, ListNode* next) :val(x), next(next) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode():val(0),next(nullptr){}
private:
	int val;
	ListNode* next;
};

class Solution {

};

int main() {


	system("pause");
	return 0;
}