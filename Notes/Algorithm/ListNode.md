## 链表基础

### 一、对比链表和数组：
**数组：**
数组的优点：
各个元素的内存空间的地址连续，因此可以通过位置快速访问、定位某个元素。
数组的缺点：
（1）修改数组（删除、插入）将导致元素大量移动，效率极低；（2）静态数组的内存空间可能存在空间不足或空间浪费问题。

**链表：**
链表的优点；
链表在指定位置进行插入和删除操作时，只需要修改被删节点上一节点的链接地址，不需要移动元素。
链表的缺点：
（1）相对于数组，多了指针域的内存开销；（2）查找效率较低。

### 二、链表概念：

链表是由一系列节点LinkNode组成，每个节点包含两个域：数据域（用于保存数据）和指针域（用于保存下一个节点的地址），ListNode在内存中是不可连续的。它包含一个指向**相同类型**数据结构的指针，因此可以说是一个包含对自身引用的类型。像这样的类型称为自引用数据类型或自引用数据结构。

可以分为：静态链表和动态链表
也可以分为：单向链表、双向链表、循环链表、单向循环链表、双向循环链表

### 三、链表结构：

![image-20210318102820213](C:\Users\TRT\AppData\Roaming\Typora\typora-user-images\image-20210318102820213.png)

#### 1、头节点：

非空链表的第一个结点称为链表的头节点。要访问链表中的结点，需要有一个指向链表头的指针。从链表头开始，可以按照存储在每个结点中的后继指针访问链表中的其余结点。头节点的下一个节点我们通常称为第一个有效节点。

**Notes:**

1、获取到链表的第一个节点，就相当于获取整个链表。
2、头节点不包含任何有效数据。

#### 2、尾部节点：

每次链表增长或减短需要更新尾部节点的位置

##### Notes:

1、最后一个结点中的后继指针通常被设置为 nullptr 以指示链表的结束。
2、尾部节点通常被初始化为头节点

### 四、单向链表的C++表示：

单向链表：只能通过前一个节点知道后一个元素的地址

#### 1、结构体定义：

```c++
    struct ListNode
    {
        float val;
        ListNode *next;
        //构造函数
        ListNode():val(0),next(nullptr){}
        ListNode(float x):val(x),next(nullptr){}
        ListNode(float x,ListNode* next):val(x),next(next){}
    };
```

#### 2、链表初始化（创建插入更新）：

```C++
ListNode* InitLinkList(){
	//创建头节点指针
    ListNode* header = new ListNode(0);
    //创建尾节点指针
    ListNode* pRear = header;
    float val=-1;
    while(1){
        cout<<"please input the element in LinkList:"<<" ";
        cin>>val;
        if(val==-1) {break;}
        //插入元素（尾插法）
        pRear->next = new ListNode(val);
        //更新尾部节点
        pRear = pRear->next;//pRear = newNode
    }
    return header;
}
```

#### 3、链表遍历（打印链表）：

```C++
void Foreach_LinkList(ListNode* header) {
	if (nullptr == header) {
		cout << "This is an empty LinkList" << endl;
		return;
	}
	ListNode* pCurrent = header->next;
	while (pCurrent) {
		cout << pCurrent->val << " ";
		pCurrent = pCurrent->next;
	}
}
```

#### 4、在指定值的位置插入新节点：

```C++
void InsertByValue_LinkList(ListNode* header, float oldval, float newval) {
	if (nullptr == header) {
		cout << "This is an empty LinkList" << endl;
		return;
	}
	//创建两个辅助指针变量
	ListNode* pPrev = header;
	ListNode* pCurrent = header->next;
	while (pCurrent) {
		if (pCurrent->val == oldval) {
			break;
		}
		pPrev = pPrev->next;
		pCurrent = pCurrent->next;
	}
	//如果pCurrent为NULL则说明链表中不存在值为oldval的节点，插入到链表的尾部
	pPrev->next = new ListNode(newval, pCurrent);//pPrev->next = newNode; newNode->next = pCurrent;
}
```



### 五、LeetCode:

#### [2. 两数相加](https://leetcode-cn.com/problems/add-two-numbers/)

给你两个 **非空** 的链表，表示两个非负的整数。它们每位数字都是按照 **逆序** 的方式存储的，并且每个节点只能存储 **一位** 数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

```
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
```

解：

```C++
class Solution{
public:
    ListNode* addTwoNumbers(ListNode* l1,ListNode* l2){
        ListNode* dummy = new ListNode(0);//创建哑节点（位于头节点前的节点，避免头节点的特殊判断）
        ListNode* pCurrent = dummy;//创建可供“移动”的当前节点
        int carry = 0;//进位
        while(l1||l2||carry){
            int target = (l1?l1->val:0)+(l2?l2->val:0)+carry;
            carry = target/10;//注：python用//
            ListNode* newNode = new ListNode(target%10);//创建新节点
            pCurrent->next = newNode;//连接到尾部节点的下一个节点
            pCurrent = newNode;//更新当前节点
            if(l1) l1 = l1->next;//更新两个相加链表
            if(l2) l2 = l2->next;
        }
        return dummy->next;//相当于return header
    }
};
```







