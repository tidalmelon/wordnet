#### wordnet语义相似度


1. 内容概览
  * lowesr\_common\_hypernyms(): 获取最低共同上位词
  * min\_depth(): 词集深度
  * path\_similarity(): **词集**相似度

2. lowesr\_common\_hypernyms()

```
功能：两个词集的最小公倍数
```

```

baleen whale 须鲸
vertebrate 脊椎动物


>>> right=wn.synset('right_whale.n.01')    # right_whale 露脊鲸、脊美鲸
>>> orca=wn.synset('orca.n.01')            # orca 逆戟鲸
>>> minke=wn.synset('minke_whale.n.01')    # minke whale 小须鲸
>>> tortoise = wn.synset('tortoise.n.01')  # tortoise 海龟
>>> novel =wn.synset('novel.n.01')

>>> right.lowest_common_hypernyms(minke)   # 说明right whale与minke whale都属于baleen whale（须鲸）
[Synset('baleen_whale.n.01')]
>>> right.lowest_common_hypernyms(tortoise)# 说明right whale 与 tortoise 都属于脊椎动物vertebrate
[Synset('vertebrate.n.01')]
>>> right.lowest_common_hypernyms(novel)   # ight whale与novel没有什么必然的联系，只能都属于entity: 根上位词
[Synset('entity.n.01')]


```

3. 如何衡量词集的远近，距离

```

>>> wn.synset('right_whale.n.01').min_depth()
15
>>> wn.synset('minke_whale.n.01').min_depth()
16
>>> wn.synset('right_whale.n.01').lowest_common_hypernyms(wn.synset('minke_whale.n.01'))
[Synset('baleen_whale.n.01')]
>>> wn.synset('baleen_whale.n.01').min_depth()
14

# 能衡量一定的关系，但是不深

>>> wn.synset('entity.n.01').min_depth()
0



```


4. **词集**相似度


  + 相似度取值范围为0~1以及-1
  + 两个词集之间没有路径返回 -1
  + 同义词集与自身比较返回1
  + 基于上位词层次结构概念中相互关联的最短路径下，进行计算的
  + 还未提到返回0的情况

```
>>> orca.path_similarity(tortoise)
0.07142857142857142


# 计算方法:

>>> dis1=wn.synset('tortoise.n.01').min_depth()
>>> dis2=wn.synset('orca.n.01').min_depth()
>>> dis1,dis2
(13, 16)
>>> wn.synset('tortoise.n.01').lowest_common_hypernyms(wn.synset('orca.n.01'))
[Synset('vertebrate.n.01')]

# 两个词集的最小公倍数
>>> wn.synset('tortoise.n.01').lowest_common_hypernyms(wn.synset('orca.n.01'))[0].min_depth()
8


# 公式：
# dis1 = 词集1深度-最小公倍数深度
# dis2 = 词集2深度-最小公倍数深度
# sim = 1.0/(dis1+dis2+1)
>>> 1.0/(13-8+16-8+1)
0.07142857142857142

# 验证成立

```












