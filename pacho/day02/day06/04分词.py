import jieba

str1 = '你可真skr弟弟，笑skr人！！！'

# 按搜索引擎搜索，带符号
mycut = jieba.cut_for_search(str1)

cutStr = jieba.cut(str1, cut_all=True)
print(mycut)

print('/'.join(mycut))
print('*'.join(cutStr))