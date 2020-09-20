# 学习笔记 / week08

|Time|Version|Note|
|---|---|---|
|09/16|0.0.1|draft|

</br>

## 一、习题要点

**[52. N皇后 II](52_N皇后II.py)**

用整数记录每一行哪些位置已被占用，注意递归时每一层只专注于当层数据的处理。整数：cols, pie, na，用bit位表示哪些位被占用。我在做题的时候有几个地方理解了半天，分享一下：

1. `~(cols | pie | na) & ((1 << n) - 1)` 这一段有两个含义，前半部分先对 cols、pie、na **或**运算拿到当前层所有不可放置的位置（列），然后取反获得当前层所有可放置的位置，后半部分结合**与**操作就是将 32 位（or 64位）整形截断保留最低 n 位。

2. DFS drill down 时，为什么 `(pie | p) << 1`？因为每下探一层，pie占领的格子（列）就左移一位。同理，`(na | p) >> 1)`表示每下探一层，na占领的格子（列）就右移一位。画个图就清楚了。

**[338 比特位计数](338_比特位计数.py)**

- **解法 1: 位运算，O(n * k), k 表示 1 的平均个数**；

- **解法 2: 位运算+DP，时间复杂度O(n)**。因为 x & (x-1) 的意思是清零 x 最低位的 1，而 ans[i] 的意思是数字 i 二进制表示内 1 的个数，所以 ans[x] 和 ans[x&(x-1)] 的二进制数内 1 的个数相差 1。

<br/>

## 二、知识点总结

**XOR 异或**

```python
x ^ 0 = x
x ^ ~0 = ~x  # ~0 代表全 1
x ^ ~x = ~0
x ^ x = 0
```

**指定位置的位运算**

```python
# x 最右边的 n 位清零
x & (~0 << n)
# 获取 x 的第 n 位的值（0 或 1）
(x >> n) & 1
# 获取 x 的第 n 位幂值
x & (1 << n)
# 仅将第 n 位置为 1
x | (1 << n)
# 仅将第 n 位置为 0
x & (~(1 << n))
# 将 x 的最高位至（含）第 n 位清零
x & ((1 << n) - 1)
```

**实战位运算要点**

```python
# 判断奇偶
x & 1 == 1 # odd
x & 1 == 0 # oven
# 二分
mid = (left + right) >> 1 = left + (right - left) >> 1
# 清零最低位的 1（注意：这里最低位的1不是说最右边的位置，而是从右往左数遇到的第一个1的位置）
x = x & (x - 1)
# 得到最低位的 1; -x = ~x + 1
x = x & -x
# 得到最低位的 0
x = x & ~x
```

**Bloom Fiter（布隆过滤器）**
它是一个很长的二进制向量和一系列随机映射函数，可以用于检索一个元素是否在一个集合中。
- 优点：空间效率和查询时间都远远超过一般的算法；
- 缺点：有一定的误识别率和删除困难。
- 应用：比特币网络、分布式系统（Map-Reduce）Hadoop、search engine、Redis缓存、垃圾邮件过滤等。

**排序算法**

- 初级排序 O(N^2)

1. 选择排序（Selection Sort）：每次找最小值然后放到待排序数组的起始位置。

2. 插入排序（Insertion Sort）：从前向后逐步构建有序序列；对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

3. 冒泡排序（Bubble Sort）：两层嵌套循环，每次查看相邻的元素，如果逆序则交换。

- 高级排序 O(NlogN)

1. 快速排序（Quick Sort）：基于分治思想；数组取标杆pivot，将小元素放pivot左边，大元素放右侧，然后依次对右边和右边的子数组继续快排。

```python
# quick sort
def quick_sort(array, begin, end):
    if begin >= end: return
    pivot = partition(array, begin, end)
    quick_sort(array, begin, pivot-1)
    quick_sort(array, pivot+1, end)
    
def partition(array, begin, end):
    pivot, counter = end, begin
    for i in range(begin, end): # 不包含end，因为pivot已占据该点
        if array[i] < array[pivot]:
            array[counter], array[i] = array[i], array[counter]
            counter += 1
    array[counter], array[pivot] = array[pivot], array[counter]
    return counter  # 返回counter作为新的pivot

# testcase = [1,3,2,6,2,9,10,5]
# print('before:', testcase)
# quick_sort(testcase, 0, len(testcase)-1)
# print('after:', testcase)
```

2. 归并排序（Merge Sort）：同样基于分治思想；把长度为n的输入序列分成长度为n/2的子序列，然后对这两个子序列分别做归并排序，最后合并排好序的两个子序列。**需要额外的内存空间 O(N)**。

```python
# merge sort
# merge sort
def merge_sort(array, begin, end):
    if begin >= end: return
    mid = (end + begin) >> 1
    merge_sort(array, begin, mid)
    merge_sort(array, mid+1, end)
    merge(array, begin, mid, end)

def merge(array, begin, mid, end):
    res = []
    # 三段式
    left, right = begin, mid+1
    while left <= mid and right <= end:
        if array[left] < array[right]:
            res.append(array[left])
            left += 1
        else:
            res.append(array[right])
            right += 1
    while left <= mid:
        res.append(array[left])
        left += 1
    while right <= end:
        res.append(array[right])
        right += 1
    array[begin:end+1] = res
```

3. 堆排序（Heap Sort）：堆插入 O(logN)，取最大、最小值 O(1)；数组元素依次建立小顶堆，依次取堆顶元素并删除。

```python
# heap sort
import heapq
def heap_sort(array):
    temp = []
    for i in array:
        heapq.heappush(temp, i)
    i = 0
    while temp:
        array[i] = heapq.heappop(temp)
        i += 1
```