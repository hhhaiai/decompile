vdex
android O 新增的格式包
Tool to decompile & extract Android Dex bytecode from Vdex files
https://github.com/anestisb/vdexExtractor
https://cloud.tencent.com/developer/article/1361398



dexRepair
Cmd line tool to repair Android DEX bytecode files CRC checksum

https://github.com/anestisb/dexRepair


Dex

Dex : The Data Explorer -- A data visualization tool written in Java/Groovy/JavaFX capable of powerful ETL and publishing web visualizations. https://dexvis.net

https://github.com/PatMartin/Dex


========================================================================
vdex
android O 新增的格式包，dex代码 直接转化的 可执行二进制码 文件：
1.第一次开机就会生成在/system/app/<packagename>/oat/ 下；
2.在系统运行过程中，虚拟机将其 从 “/system/app” 下 copy 到 “/data/davilk-cache/” 下
odex
    在Android N 之前，Dalvik虚拟机执行程序dex文件前，系统会对dex文件做优化，生成可执行文件odex，保存到data/dalvik-cache目录，最后把apk文件中的dex文件删除。
    优点：
        1.减少了启动时间（省去了系统第一次启动应用时从apk文件中读取dex文件，并对dex文件做优化的过程。）和对RAM的占用（apk文件中的dex如果不删除，同一个应用就会存在两个dex文件：apk中和data/dalvik-cache目录下）。
        2.防止第三方用户反编译系统的软件（odex文件是跟随系统环境变化的，改变环境会无法运行；而apk文件中又不包含dex文件，无法独立运行）。
    在Android O 之后，odex 是从vdex 这个文件中 提取了部分模块生成的一个新的 可执行二进制码 文件 ， odex 从vdex 中提取后，vdex 的大小就减少了。
        1.第一次开机就会生成在/system/app/<packagename>/oat/ 下
        2.在系统运行过程中，虚拟机将其 从 “/system/app” 下 copy 到 “/data/davilk-cache/” 下
        3.odex + vdex = apk 的全部源码 （vdex 并不是独立于odex 的文件 odex + vdex 才代表一个apk ）

art
odex 进行优化 生成的 可执行二进制码 文件，主要是apk 启动的常用函数相关地址的记录，方便寻址相关； 通常会在data/dalvik-cache/保存常用的jar包的相关地址记录。
1.第一次开机不会生成在/system/app/<packagename>/oat/ 下，以后也不会；
2.odex 文件在运行时，虚拟机会计算函数调用频率，进行函数地址的修改；
3.最后在/data/davilk-cache/ 由虚拟机生成；
4.生成art 文件后，/system/app 下的odex 和 vdex 会无效，即使你删除，apk也会正常运行
5.push 一个新的apk file 覆盖之前/system/app 下apk file ，会触发PKMS 扫描时下发force_dex flag ，强行生成新的vdex 文件 ，覆盖之前的vdex 文件，由于某种机制，这个新vdex 文件会copy到/data/dalvik-cache/下，于是art 文件也变化了。

oat
ART虚拟机使用的是oat文件，oat文件是一种Android私有ELF文件格式，它不仅包含有从DEX文件翻译而来的本地机器指令，还包含有原来的DEX文件内容。APK在安装的过程中，会通过dex2oat工具生成一个OAT文件。对于apk来说，oat文件实际上就是对odex文件的包装，即oat=odex，而对于一些framework中的一些jar包，会生成相应的oat尾缀的文件，如system@framework@boot-telephony-common.oat。


作者：richy_
链接：https://www.jianshu.com/p/f48eac038384
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。