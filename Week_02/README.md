# 学习笔记 / Week02

|Time|Version|Note|
|---|---|---|
|08/05|0.0.1|draft|


> 既然**刷题**是成长为顶尖职业选手的必经之路，那就认认真真地彻底用好这几个月吧！
> 除了五毒神掌之外，我觉得应该适当拓展，把每周课程范围内的高频题尽量多做一些，特别是要多做几遍！！！这样，每周都能聚焦在一个小知识圈内，刻意练习。通过不同的题目，发现自己学习中的疏漏和偏差，及时纠正并不断强化！>                                                  ———— week2 小理解


## HashMap 源码分析 之 Get / Put
* Get
Get 方法比较直接，根据传入的 key，计算 hash 值（索引），并依据该索引直接获取数组 buckets 中保存的 HashEntry。然后从该 HashEntry 链表头节点开始遍历，直到找到相同的 key，或者到链表尾部位置。详细分析如下：
```python
public V get(Object key)
{
    # 计算 key 对应的 hash 值作为 buckets 数组的索引
    int idx = hash(key);
    # buckets 实际是一个数组，保存了类型为 HashEntry<K, V> 的元素，即每个元素包含了键值对
    # 注意这些元素是 hash 表每个位置的开头
    HashEntry<K, V> e = buckets[idx];
    # HashMap 采用链表法解决hash collisions，这个while循环就是为了在idx指示的链表中，找到对应的key
    # 如果找到相同的key，则返回相应的值；可见最坏查询效率从 O(1) 下降到了 O(N)
    while (e != null)
    {
        if (equals(key, e.key))
        return e.value;
        e = e.next;
    }
    # 如果找不到相同的key，则返回空（即没有找到）
    return null;
}
```
问题：
1. HashEntry 的实现是 LinkedHashMap 吗？

* Put
Put 方法涉及到 hash碰撞 、hash表扩展等，稍微有点复杂，详细如下：
```python
public V put(K key, V value)
{
    # 计算 idx，hash 函数就是用 key.hashcode 对 buckets 长度取模。那么，随之而来有两个点值得思考：
    # 1. idx 位置已经被其他值到了，即存在hash collision，怎么办？2. 如果存储的值过多，hash 冲突发生的概率大，平均检索效率明显下滑到 O(n) 如何优化？
    # 慢慢往下看
    int idx = hash(key);
    # buckets 存储的是 idx 位置的键值对链表
    HashEntry<K, V> e = buckets[idx];
    # 如果 e 为空，则表示该位置还未被占用，可直接在后面创建 HashEntry 以存放 key-value；
    # 如果 e 非空，则检索链表 e，查看是否有相同的 key 存在。如果存在相同的 key，则覆盖其原本的 value。
    while (e != null)
    {
        if (equals(key, e.key))
        {
            e.access(); // Must call this for bookkeeping in LinkedHashMap.
            V r = e.value;
            e.value = value;
            return r;
        }
        else
            e = e.next;
    }

    // At this point, we know we need to add a new entry.
    # modCount 看注释是为了线程安全，细节我不太清楚，暂时跳过。
    modCount++;
    # size 记录了 hash表 中存放的所有 key-value 个数，如果大于 threshold，说明该表 hash collisions 发生的概率较高，
    # 性能将明显退化至 O(n)，因此需要扩容。
    if (++size > threshold)
    {
        # 扩容，一般是令 hash table 尺寸翻倍，rehash 过程中将重新计算所有 HashEntry 的索引值。
        rehash();
        // Need a new hash value to suit the bigger table.
        # 当然，扩容后也要重新计算输入 key 的索引值，该 idx 仍有较小概率会 hash 冲突，但扩容后整个 hash 表的平均时间复杂度回到 O(1)
        idx = hash(key);
    }

    // LinkedHashMap cannot override put(), hence this call.
    # 在 buckets 的 idx 位置添加键值对。注意：buckets[idx] 保存的是该位置链表的头节点
    addEntry(key, value, idx, true);
    return null;
}

void addEntry(K key, V value, int idx, boolean callRemove)
{
    # 新建节点 HashEntry
    HashEntry<K, V> e = new HashEntry<K, V>(key, value);
    # 在链表头部插入节点 e。
    # 常规链表操作：先把 e.next 指向当前链表的头节点（即buckets[idx]保存的节点），然后把 e 作为头节点保存到 buckets[idx] 中（覆盖原来的值）
    e.next = buckets[idx];
    buckets[idx] = e;
}
```
问题：
1. 什么是 bookkeeping？在 LinkedHashMap 中又是如何使用的？


## Heap 堆

|名称|描述|
|---|---|
|二叉堆|只是其中的一种实现，而且是堆里效率比较低的，取最大（小）值的时间复杂度是 O(1)，添加删除节点需要堆化，时间复杂度是 O(logN)。也因为实现简单，通常会在 *面试* 中出现。|
|Fibonacci堆|效率最高的一种堆，仅了解。|
|Priority Queue|是各种语言（库）的堆实现|
|Heapq|python中堆的实现|

### 什么是 Binary Heap（二叉堆）？

Binary Heap（二叉堆）是特殊的一个完全二叉树，其根节点大于或小于其所有的子孙节点。如果是大于，则为 max heap（大顶堆）；如果是小于，则为 min heap（小顶堆）。可以用树或者数组表示。

### 为什么要用数组表示 Binary Heap？
因为 Binary Heap 是一个完全二叉树，用数组存放既可以节省空间，又能通过下标快速访问父节点或孩子节点。比如对于节点 i，其父节点是 (i-1)//2，其左儿子是 2*i+1，右儿子是 2*i+2（假设index从0开始）。

### Heap sort（堆排序）
Heap sort 类似插入排序，后者每次选取最大值放在最后，不断重复以完成排序。堆排序相比选择排序，在取得最大值的方法上有所不同。具体步骤如下：
1. 使用输入数据创建一个 max heap（大顶堆）；
2. 弹出 top 元素，并记录至 ans（answer）数组，然后 heapify（堆化）；
3. 重复上述步骤，直到堆为空。
上述步骤中可以通过创建 min heap，或者使用 deque 等操作，实现升序排列。

----
坚持！第二周！

加油！第三周～