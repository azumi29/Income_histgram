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

df_income = df_income.round()

# df_income.cut(df_income['C120120_納税義務者数（所得割）'],bins=[-1,1999,2999,4999,9999,19999,99999])
# df_income.cut(df_income['C120120_納税義務者数（所得割）'],bins=[-1,1999,2999,4999,9999,19999,99999],labels=['young','young-adult','adult'])
df_income = df_income.reindex(columns=['1人当たり所得【千円】', 'C120120_納税義務者数（所得割）【人】'])

# df_income['年収区分']=df_income.cut(df_income['年収区分'], [-1,1999,2999,4999,9999,19999,99999])
# height_data.groupby('size').size()

print(df_income)

# df_income.hist()

# # x = df_income['C120120_納税義務者数（所得割）【人】']
# # plt.hist(df_income['1人当たり所得【千円】'])

# df_income = np.array(df_income['1人当たり所得【千円】'])

fig, ax = plt.subplots()
 
# ax.hist(df_income)
ax.hist(df_income,orientation='horizontal')
# ax.hist(df_income['1人当たり所得【千円】'], df_income['C120120_納税義務者数（所得割）【人】'])
# # ax.set_title('所得分布')pyt
# # ax.set_xlabel('1人当たり所得【千円】')
# # ax.set_ylabel('納税義務者数（所得割）【人】')
# fig.show()

# plt.savefig("income_histrgam.png")
plt.savefig("income_histrgam_horizontal.png")

plt.show()