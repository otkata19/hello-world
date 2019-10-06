import csv
import re
import codecs
import pandas as pd
import numpy as np
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import *
from janome.charfilter import *
from sklearn.feature_extraction.text import CountVectorizer
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

#csvファイルを読み取って表にする
with codecs.open("../datasets/issa_data.csv", "r", "Shift-JIS", "ignore") as file:
    df = pd.read_table(file, delimiter=",")

t = Tokenizer()
def tokenize(text):
    token_filters = [POSKeepFilter(['名詞']),
                     ExtractAttributeFilter('surface'),]
    char_filters =  [RegexReplaceCharFilter(u'[()]', u'')]
    a = Analyzer(token_filters=token_filters,char_filters=char_filters)
    tokens = [token for token in a.analyze(text)]
    return ' '.join(tokens)

tokenized_list = [tokenize(i) for i in df.iloc[0:20, 1]]
print(tokenized_list)

"""
# 分かち書きされた文章からベクトルを得る
cv = CountVectorizer()
matrix = cv.fit_transform(removed_list)
wordlist = list(cv.vocabulary_.values())
one_hot = np.identity(len(wordlist))[wordlist]

print(matrix.shape)
print(cv.get_feature_names())
print(cv.vocabulary_)
print(wordlist)
print(one_hot)
# 得られるベクトルはscipyのsparse matrixです
# 可視化のためにdense matrixにしていますが、後続のモデルがsparse matrixでOKの場合は変換不要です
print(matrix.todense())
"""
