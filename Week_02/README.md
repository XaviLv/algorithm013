# 学习笔记 / Week02

|Time|Version|Note|
|---|---|---|
|08/05|0.0.1|draft|


> 既然**刷题**是成长为顶尖职业选手的必经之路，那就认认真真地彻底用好这几个月吧！
> 除了五毒神掌之外，我觉得应该适当拓展，把每周课程范围内的高频题尽量多做一些，特别是要多做几遍！！！这样，每周都能聚焦在一个小知识圈内，刻意练习。通过不同的题目，发现自己学习中的疏漏和偏差，及时纠正并不断强化！>                                                  ———— week2 小理解


## Hash Table



## HashMap Source Code
```python
public V get(Object key)
{
    int idx = hash(key);
    HashEntry<K, V> e = buckets[idx];
    while (e != null)
    {
        if (equals(key, e.key))
        return e.value;
        e = e.next;
    }
    return null;
}
```



## 堆

二叉堆：只是其中的一种实现，而且是堆里效率比较低的，取最大（小）值的时间复杂度是 O(1)，添加删除节点需要堆化，时间复杂度是 O(logN)。也因为实现简单，通常会在 **面试** 中出现。

Fibonacci堆：效率最高的一种堆，仅了解。

Priority Qeueu：是各种语言（库）的堆实现.。