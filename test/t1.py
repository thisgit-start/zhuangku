from icecream import ic

import pandas as pd

path = '/Users/wang/Downloads/1689146957625.xlsx'
pd.set_option('display.expand_frame_repr', False)
pd.set_option("display.max_row", None)
data = pd.read_excel(io=path,header = None)

# mean = data["Weight"].mean()
# median = data["Weight"].median()
# mode = data["Weight"].mode()
# df = data["College"].drop_duplicates()
# print(data[175:176]['采购计划单号'])
# print(data.iloc[175]['采购计划单号'])
# print(type(data))
# print(list(data))
# print(len(data.index))
# ic(data.columns)

ic(data.iloc[0][2])
ic(data.values[0][2])
ic(len(data))
# ic(data.columns)