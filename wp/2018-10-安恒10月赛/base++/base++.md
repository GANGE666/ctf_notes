给了idb文件
![](https://i.imgur.com/56g0wA0.jpg)

最后与
‘TRLT5amLBoLT5Z6Fa5LqN6mkTomqR66Da4LqX5mgBwkkP5wmTZ6D====’
对比，相等即可

----------

打开先看transform_1()
![](https://i.imgur.com/R1sennw.png)

----------

transform_1()大概过程为：
遍历this字符串，大小写字母分别处理，
做一次移位变换，移13个字符。
abcdefghijklmnopqrstuvwxyz
变成
nopqrstuvwxyzabcdefghijklm

ABCDEFGHIJKLMNOPQRSTUVWXYZ
变成
NOPQRSTUVWXYZABCDEFGHIJKLM

----------

再看transform_2():
先对 **byte_40507C** 'BCDEFGHIJKLMNOPQRSTUVWXYZ'做transform1变换
再加几个数字
![](https://i.imgur.com/IPI6ncu.png)
得 **byte_40507C** 为 
NoPqRsTuVwXyZaBcDeFgHiJkLm765432



----------

接下来看transform_3():
![](https://i.imgur.com/dWUtDxn.png)
关键在于base_tran_5()这个函数

----------
跟进base_tran_5():
![](https://i.imgur.com/pRkwRJV.png)
关键在于两个while，不过根据末尾=号的数量可以推断出len%5=2
看了一下两个while的内容。
实现了一个类似base64的转换。
写出逆向脚本如下。
![](https://i.imgur.com/h69vtcM.png)

再将最后几位'TZ6D===='手动转换为'37'，拼接上去。

得input = ‘10a78cca3eb00b70e2bcbc5f3ebdd937’

检查：![](https://i.imgur.com/VUgZkkw.jpg)

getflag