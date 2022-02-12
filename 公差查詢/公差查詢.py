import pandas as pd 
import os
import csv
import numpy as np
from tqdm import tqdm, trange


PATH = "公差查詢/參數/"
date_name = os.listdir(PATH)
print(date_name)
print("請輸入類型 : ")
type_1 = input()
if type_1 == "軸承":
    type_path_2 = PATH + type_1 + "/"
    type_name_2 = os.listdir(type_path_2)
    type_name_3 = []
    for T in range(len(type_name_2)):
        type_name_3.append(type_name_2[T].replace(".csv",""))
    print("請輸入以下類型:", type_name_3)
    type_3 = input()
    type_path_3 = type_path_2 + type_3 + ".csv"
    dataframe = pd.read_csv(type_path_3, sep=',', index_col = "編號")
    print("請輸入參數:")
    type_4 = input()
    a = dataframe.loc[int(type_4), :]
    print(a)
    # print(dataframe)
else:
    type_path_1 = PATH + type_1 + "/"
    type_name_1 = os.listdir(type_path_1)
    print("請輸入以下類型:", type_name_1)
    type_2 = input()
    if type_2 == "平行鍵":
        type_path_3 = "公差查詢\參數\鍵\平行鍵\平行鍵.csv"

    else:
        type_path_2 = type_path_1 + type_2 + "/"
        type_name_2 = os.listdir(type_path_2)
        type_name_3 = []
        for T in range(len(type_name_2)):
            type_name_3.append(type_name_2[T].replace(".csv",""))
        print("請輸入以下類型:", type_name_3)
        type_3 = input()
        type_path_3 = type_path_2 + type_3 + ".csv"
        dataframe = pd.read_csv(type_path_3, sep=',', index_col = "系列")
        print("請輸入參數:")
        type_4 = input()
        a = dataframe.loc[type_4, :]
        print(a)