easytree

拖进kali，file查看，是pe文件。

拖进peid，发现是UPX壳。

脱壳。

拖进IDA，查看字符串。
![](https://i.imgur.com/r09WTBQ.png)

确定在主函数中进行逻辑判断，并怀疑base64

在主函数中看到一串字符做比较，base64解码
aWNuZXJyc2VhZXRydmVl
得
icnerrseaetrvee

估计就是输入进行移位变换得的

用OD进行调试
![](https://i.imgur.com/CAmhlfe.jpg)
发现1234567890abcde变成了1248950a36bc7de

所以输入应该为icanreversetree

![](https://i.imgur.com/xiSRKQu.png)
md5后提交即可