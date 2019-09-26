# ライブラリのインポート
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

df = pd.read_csv("datasets/test3_2.csv", encoding="shift-jis")
print(df.iloc[12,2])
