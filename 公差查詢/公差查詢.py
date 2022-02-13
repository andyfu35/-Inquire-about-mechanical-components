import pandas as pd 
import os

PATH = "公差查詢/參數/"
date_name = os.listdir(PATH)
print(date_name)
print("請輸入類型 : ")
type_1 = input()
# if type_1 == "軸承":
type_path_2 = PATH + type_1 + "/"
type_name_2 = os.listdir(type_path_2)
type_name_3 = []
for T in range(len(type_name_2)):
    type_name_3.append(type_name_2[T].replace(".csv",""))
print("請輸入以下類型:", type_name_3)
type_3 = input()
type_path_3 = type_path_2 + type_3 + ".csv"
dataframe = pd.read_csv(type_path_3, sep=',', index_col = "參數")
print("請輸入參數:")
type_4 = input()
if type_1 == "軸承":
    text = dataframe.loc[int(type_4), :]
else:
    text = dataframe.loc[type_4, :]
print(text)
