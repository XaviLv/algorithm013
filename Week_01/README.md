# 学习笔记

> 最需要总结的笔记：
> 1. 老师布置的软作业，比如读源码，脑图
> 2. 有不懂或者疑惑的问题，在这里提出来
> 3. 针对一周的学习情况，总结自己哪里做的好，哪里做的不足，下周有针对性地改进
> 4. 相同类型的题目，或者相同类型的解题思路，在这里总结
> 5. 重点题目，在这里记录详细思路和解法，不要求贴代码
> 6. 其他


**10周 300题 ： 相当于 1天 至少 4题**
___



## 师夷长技以制

* 刷题秘籍：**五毒神掌**


* 如何科学搜索源码


* 分析 Queue 和 Priority Queue 源码


* 用 add first 或 add last 这套新的 API 改写 Deque 的代码


* 复杂度分析（时间/空间）


* 编码技巧 & Code Style


## 加餐

* 数据结构与算法总揽（脑图）

## 工欲善其事，必先利其器
* 五毒神掌App：年轮（艾宾浩斯遗忘曲线）


* 磨刀霍霍向算法：玩转IDE


* 一起「作弊」吧：cheatsheet小合集


## 算法解题思路
 (只记录最重要的一些思路！！！相同类型的解题思路总结一下，最好有图！！不要罗列，单个题目的思路应该在py代码中注解，十分重要的，比如接雨水，可以在这里详细说明，或者直接在leetcode的题解中写清楚，这里链接一下。)
### 简单
* [爬楼梯（阿里巴巴、腾讯、字节跳动在半年内面试常考）](https://leetcode-cn.com/problems/climbing-stairs/)


* [206. 反转链表（字节跳动、亚马逊在半年内面试常考）](https://leetcode.com/problems/reverse-linked-list/)


* [141. 环形链表（阿里巴巴、字节跳动、腾讯在半年内面试常考）](https://leetcode.com/problems/linked-list-cycle/)


* [26. 删除排序数组中的重复项（Facebook、字节跳动、微软在半年内面试中考过）](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/)


* [189. 旋转数组（微软、亚马逊、PayPal 在半年内面试中考过）](https://leetcode-cn.com/problems/rotate-array/)


* [21. 合并两个有序链表（亚马逊、字节跳动在半年内面试常考）](https://leetcode-cn.com/problems/merge-two-sorted-lists/) 


* [88. 合并两个有序数组（Facebook 在半年内面试常考）](https://leetcode-cn.com/problems/merge-sorted-array/)


* [1. 两数之和（亚马逊、字节跳动、谷歌、Facebook、苹果、微软在半年内面试中高频常考）](https://leetcode-cn.com/problems/two-sum/)


* [283. 移动零（Facebook、亚马逊、苹果在半年内面试中考过）](https://leetcode-cn.com/problems/move-zeroes/)


* [66. 加一（谷歌、字节跳动、Facebook 在半年内面试中考过）](https://leetcode-cn.com/problems/plus-one/) 


* [20. 有效的括号（亚马逊、JPMorgan 在半年内面试常考）](https://leetcode-cn.com/problems/valid-parentheses/)


* [155. 最小栈（亚马逊在半年内面试常考）](https://leetcode-cn.com/problems/min-stack/)


### 中等：
* [641. 设计循环双端队列（Facebook 在 1 年内面试中考过）](https://leetcode.com/problems/design-circular-deque/)


* [15. 三数之和（国内、国际大厂历年面试高频老题）](https://leetcode-cn.com/problems/3sum/)


* [11. 盛水最多容器（腾讯、百度、字节跳动在近半年内面试常考）](https://leetcode-cn.com/problems/container-with-most-water/)


* [24. 两两交换链表中的节点（阿里巴巴、字节跳动在半年内面试常考）](https://leetcode.com/problems/swap-nodes-in-pairs/)


* [142. 环形链表 II](https://leetcode.com/problems/linked-list-cycle-ii/)





### 困难：
* [42. 接雨水（亚马逊、字节跳动、高盛集团、Facebook 在半年内面试常考）](https://leetcode.com/problems/trapping-rain-water/)


* [84. 柱状图中最大的矩形（亚马逊、微软、字节跳动在半年内面试中考过）](https://leetcode-cn.com/problems/largest-rectangle-in-histogram/) 


* [239. 滑动窗口最大值（亚马逊在半年内面试常考）](https://leetcode-cn.com/problems/sliding-window-maximum/)


* [25. K 个一组翻转链表（字节跳动、猿辅导在半年内面试常考](https://leetcode.com/problems/reverse-nodes-in-k-group/)



## 参考链接
1. [Java 的 PriorityQueue 文档](https://docs.oracle.com/javase/10/docs/api/java/util/PriorityQueue.html)
2. [Java 的 Stack 源码](http://developer.classpath.org/doc/java/util/Stack-source.html)
3. [Java 的 Queue 源码](http://fuseyism.com/classpath/doc/java/util/Queue-source.html)
4. [Python 的 heapq](https://docs.python.org/2/library/heapq.html); 
5. [高性能的 container 库](https://docs.python.org/2/library/collections.html); 
6. [Java 源码分析（ArrayList）](http://developer.classpath.org/doc/java/util/ArrayList-source.html)
7. [Linked List 的标准实现代码](https://www.geeksforgeeks.org/implementing-a-linked-list-in-java-using-class/)
8. [Linked List 示例代码](http://www.cs.cmu.edu/~adamchik/15-121/lectures/Linked%20Lists/code/LinkedList.java)
9. [Java 源码分析（LinkedList）](http://developer.classpath.org/doc/java/util/LinkedList-source.html)
10. [LRU Cache - Linked list： LRU 缓存机制](http://leetcode-cn.com/problems/lru-cache)
11. [Redis - Skip List：跳跃表、为啥 Redis 使用跳表（Skip List）而不是使用 Red-Black？](http://www.zhihu.com/question/20202931)

——————————

*兴奋 -> 彷徨 -> 坚持 -> offer！*
