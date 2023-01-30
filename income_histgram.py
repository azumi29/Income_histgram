import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSV呼び出し
df_income = pd.read_csv('income_histgram.csv',encoding='ANSI', header=8, usecols=[2,3,5,7])

# '-'をNaNへ変換してその行を削除
df_income['C120110_課税対象所得【千円】'] = pd.to_numeric(df_income['C120110_課税対象所得【千円】'], errors="coerce")
df_income['C120120_納税義務者数（所得割）【人】'] = pd.to_numeric(df_income['C120120_納税義務者数（所得割）【人】'], errors="coerce")
df_income = df_income.dropna() 

# 1人当たり所得【千円】列の追加
df_income['1人当たり所得【千円】'] = df_income['C120110_課税対象所得【千円】']/df_income['C120120_納税義務者数（所得割）【人】']

# 不要な列の削除
df_income = df_income.drop("地域 コード", axis=1)
df_income = df_income.drop("地域", axis=1)
df_income = df_income.drop("C120110_課税対象所得【千円】", axis=1)
df_income = df_income.drop("C120120_納税義務者数（所得割）【人】", axis=1)

# 四捨五入
df_income = df_income.round()

print(df_income)


# histgram作成
fig, ax = plt.subplots()
ax.hist(df_income,bins=30)

# タイトル等挿入
ax.set_title('所得分布', fontname="MS Gothic")
ax.set_xlabel('1人当たり所得【千円】', fontname="MS Gothic")
ax.set_ylabel('Frequency')

# グラフを保存
plt.savefig("income_histrgam.png")

plt.show()