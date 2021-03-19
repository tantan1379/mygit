#pragma once
//使C++程序可以调用C语言程序
#ifdef __cplusplus
extern "C" {
#endif
	struct ListNode {
		int data;
		struct ListNode* next;
	};



#ifdef __cplusplus
}
#endif