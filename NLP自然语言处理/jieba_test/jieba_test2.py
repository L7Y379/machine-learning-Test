'''并行分词
原理：将目标文本按行分隔后，把各行文本分配到多个 Python 进程并行分词，然后归并结果，从而获得分词速度的可观提升 基于 python 自带的 multiprocessing 模块，目前暂不支持 Windows

用法：

jieba.enable_parallel(4) # 开启并行分词模式，参数为并行进程数
jieba.disable_parallel() # 关闭并行分词模式

注意：并行分词仅支持默认分词器 jieba.dt 和 jieba.posseg.dt。
'''
import sys
import time
import jieba
'''
jieba.enable_parallel()
content = open(u'西游记.txt',"r").read()
t1 = time.time()
words = "/ ".join(jieba.cut(content))
t2 = time.time()
tm_cost = t2-t1
print('并行分词速度为 %s bytes/second' % (len(content)/tm_cost))
'''
jieba.disable_parallel()
content = open('西游记.txt',"rb").read()
t1 = time.time()
words = "/ ".join(jieba.cut(content))
t2 = time.time()
tm_cost = t2-t1
print('非并行分词速度为 %s bytes/second' % (len(content)/tm_cost))

'''
Tokenize：返回词语在原文的起止位置
注意，输入参数只接受 unicode
'''
print("这是默认模式的tokenize")
result = jieba.tokenize(u'自然语言处理非常有用')
for tk in result:
    print("%s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))

print("\n-----------我是神奇的分割线------------\n")

print("这是搜索模式的tokenize")
result = jieba.tokenize(u'自然语言处理非常有用', mode='search')
for tk in result:
    print("%s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))