'''
和拉丁语系不同，亚洲语言是不用空格分开每个有意义的词的。而当我们进行自然语言处理的时候，大部分情况下，词汇是我们对句子和文章理解的基础，因此需要一个工具去把完整的文本中分解成粒度更细的词。

jieba就是这样一个非常好用的中文工具，是以分词起家的，但是功能比分词要强大很多。

1.基本分词函数与用法
jieba.cut 以及 jieba.cut_for_search 返回的结构都是一个可迭代的 generator，可以使用 for 循环来获得分词后得到的每一个词语(unicode)

jieba.cut 方法接受三个输入参数:

需要分词的字符串
cut_all 参数用来控制是否采用全模式
HMM 参数用来控制是否使用 HMM 模型
jieba.cut_for_search 方法接受两个参数

需要分词的字符串
是否使用 HMM 模型。
该方法适合用于搜索引擎构建倒排索引的分词，粒度比较细
'''
import jieba

seg_list = jieba.cut("我在学习自然语言处理", cut_all=True)
print(seg_list)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我在学习自然语言处理", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他毕业于上海交通大学，在百度深度学习研究院进行研究")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在哈佛大学深造")  # 搜索引擎模式
print(", ".join(seg_list))

#jieba.lcut以及jieba.lcut_for_search直接返回 list
result_lcut = jieba.lcut("小明硕士毕业于中国科学院计算所，后在哈佛大学深造")
print(result_lcut)
print(" ".join(result_lcut))
print(" ".join(jieba.lcut_for_search("小明硕士毕业于中国科学院计算所，后在哈佛大学深造")))

"""添加用户自定义词典
很多时候我们需要针对自己的场景进行分词，会有一些领域内的专有词汇。

1.可以用jieba.load_userdict(file_name)加载用户字典
2.少量的词汇可以自己用下面方法手动添加：
用 add_word(word, freq=None, tag=None) 和 del_word(word) 在程序中动态修改词典
用 suggest_freq(segment, tune=True) 可调节单个词语的词频，使其能（或不能）被分出来
"""

print('/'.join(jieba.cut('如果放到旧字典中将出错。', HMM=False)))
jieba.suggest_freq(('中', '将'), True)
print('/'.join(jieba.cut('如果放到旧字典中将出错。', HMM=False)))

"""
关键词提取
基于 TF-IDF 算法的关键词抽取
import jieba.analyse

jieba.analyse.extract_tags(sentence, topK=20, withWeight=False, allowPOS=())
sentence 为待提取的文本
topK 为返回几个 TF/IDF 权重最大的关键词，默认值为 20
withWeight 为是否一并返回关键词权重值，默认值为 False
allowPOS 仅包括指定词性的词，默认值为空，即不筛选
"""

import jieba.analyse as analyse
lines = open('NBA.txt','rb').read()
print("  ".join(analyse.extract_tags(lines, topK=20, withWeight=False, allowPOS=())))
lines = open('西游记.txt','rb').read()
print("  ".join(analyse.extract_tags(lines, topK=20, withWeight=False, allowPOS=())))


'''基于 TextRank 算法的关键词抽取
jieba.analyse.textrank(sentence, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v')) 直接使用，接口相同，注意默认过滤词性。
jieba.analyse.TextRank() 新建自定义 TextRank 实例
算法论文： TextRank: Bringing Order into Texts

基本思想:

将待抽取关键词的文本进行分词
以固定窗口大小(默认为5，通过span属性调整)，词之间的共现关系，构建图
计算图中节点的PageRank，注意是无向带权图
'''
lines = open('NBA.txt','rb').read()
print("  ".join(analyse.textrank(lines, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))))
print("---------------------我是分割线----------------")
print("  ".join(analyse.textrank(lines, topK=20, withWeight=False, allowPOS=('ns', 'n'))))

lines = open('西游记.txt','rb').read()
print("  ".join(analyse.textrank(lines, topK=20, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))))

'''词性标注
jieba.posseg.POSTokenizer(tokenizer=None) 新建自定义分词器，tokenizer 参数可指定内部使用的 jieba.Tokenizer 分词器。jieba.posseg.dt 为默认词性标注分词器。
标注句子分词后每个词的词性，采用和 ictclas 兼容的标记法。
'''

import jieba.posseg as pseg
words = pseg.cut("我爱自然语言处理")
for word, flag in words:
    print('%s %s' % (word, flag))