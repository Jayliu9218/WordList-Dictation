# 基于Python操作单词db数据库与Edge大声朗读的英语听写方案



***声明：本教程仅作学习交流与丰富单词书作用，支持正版，从你我做起！***



***写在前面：本教程由[Biem](https://www.cnblogs.com/biem/)大力支持，欢迎关注！***



## 1 获取单词书的单词数据库

[红宝书词汇APK下载-20230727仍可用](https://sj.qq.com/appdetail/com.hongbaoshuapp)

红宝书词汇APP的单词数据库就在APK安装文件中，解压后即可发现，并且最近几年的都有。我没有安装SQL相关软件，就直接上网查了其他人的解决方案，发现可以db文件并没有加密（微信的聊天文件Msg.db是加密的），用Python结合sqlite库可以直接读取其内容，再利用Python读写文件的操作，可以很轻松的得到单词数据。

<img src=".\assets\image-20230727224139010.png" alt="image-20230727224139010" style="zoom: 80%;" />

<center>
图1 获取红宝书词汇apk与单词的db数据库    
</center>
<img src=".\assets\image-20230727224325253.png" alt="image-20230727224325253" style="zoom: 80%;" />

<center>
图2 单词的db数据库文件 
</center>



## 2 尽可能不造轮子得到自己想要的数据

首先分享一位大神的博客：[红宝书词汇导出到成欧路词典单词库和生词本](https://www.cnblogs.com/biem/p/16101097.html)。前人栽树后人乘凉，感谢大神的分享！我试了一下居然直接就能跑，不过前提是安装好了sqlite的相关库文件，这点我也是提前照着网上的教程安装的：[SQLite安装](https://www.runoob.com/sqlite/sqlite-installation.html)。之后呢就是对Python代码的一些修改，使之生成自己需要的单词文件。

至于具体的代码部分，下图应该是博客作者在查看数据库后进行的划分，我们取自己所需，听写的话其实只需要中文意义即可，不太需要其他东西，所以我把其他的都没有加入`onceItemOrder`列表，同时考虑到单词复习是章节化的，需要对不同章节的单词有所区分，故仅保留了`unit`一个属性。

<img src=".\assets\image-20230727230551864.png" alt="image-20230727230551864" style="zoom: 80%;" />

<center>
图3 单词的属性列表    
</center>
<img src=".\assets\image-20230727230822332.png" alt="image-20230727230822332" style="zoom: 80%;" />

<center>
图4 调整后的`onceItemOrder`    
</center>

除此之外，还对导出做了一些调整。

<img src=".\assets\image-20230727231208577.png" alt="image-20230727231208577" style="zoom:80%;" />

<center>
图5 获取写入内容与一些调整 
</center>

总而言之，经过合理的调整，得到了所需要的单词文件，接下来还需要进一步处理：

1. 单词章节化：考虑到几乎每天都会使用，这一步我就没有再编程了。具体步骤为查找`UNIT X`之后选中对应的单元，再复制粘贴到新文件`X.txt`，在`X.txt`中查找`UNIT X`并替换为空，整个操作并不会耗费很长的时间；

2. 行随机化：用一下Python的读写文件功能：首先读入新文件`X.txt`，再读取每一行的内容生成内容列表`NewContent`，同时获得总行数`LineOfFile`，根据总行数获得范围内的随机数列表`OrderList`。之后进行写入文件操作：逐行写入内容为：`str(i)+NewContent[OrderList[i]]`，即获得章节化的随机分布的单词中文列表。

<img src=".\assets\image-20230727231441126.png" alt="image-20230727231441126" style="zoom:80%;" />

<center>
图6 调整后的原始单词本文件
</center>
<img src=".\assets\image-20230727232446888.png" alt="image-20230727232446888" style="zoom:80%;" />

<center>
图7 最终用于听写的单词本文件
</center>



## 3 使用Edge的”大声朗读“功能进行听写

最后一步，用`Edge`打开最终的单词本文件，在”更多功能“中选择”大声朗读“（快捷键`ctrl+shift+u`），在语音选项中可以调节语速和音种（体验后发现`Microsoft Xiaoxiao Online (Natual) - Chineses (Mainland)`还不错）。

<center>
    戴上耳机，重温高中美好时光~~~
</center>
<img src=".\assets\image-20230727232954952.png" alt="image-20230727232954952" style="zoom:80%;" />

<center>
图8 听写示例
</center>
<img src=".\assets\IMG_4006.jpg" alt="IMG_4006" style="zoom:80%;" />

<center>
图9 听写示例
</center>


***再次声明：本教程仅作学习交流与丰富单词书作用，支持正版，从你我做起！***

