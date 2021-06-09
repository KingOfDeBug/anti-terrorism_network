import os
import pandas as pd
import re
# 预处理
def build_frame():
    data_frame = pd.DataFrame()
    path = os.path.abspath('web information')
    for x in os.listdir(path):
        try:
            if x:
                if x.split('.')[-1] == 'xlsx':
                    name = os.path.join(path,x)
                    frame = pd.read_excel(name,engine='openpyxl')
                    frame = frame.dropna(axis = 0,how = 'all') # 删除空行
                    frame = frame.iloc[:,0:2]
                    frame.columns = [1,2]
                    data_frame = pd.concat([data_frame ,frame],ignore_index=True)
        except:
            pass
    data_frame.drop_duplicates(subset=[2],keep='first',inplace=True)
    return data_frame

# 匹配
def match(country_dict,sentence):
    lst = []
    for item in country_dict.items():
        name_tuple = item[1]
        for name in name_tuple:
            if re.search(name,sentence):
                lst.append(item[0])
                break
    return lst




def match_country(frame,country_dict):
    i = 0
    lst = []
    for title in frame.iloc[:,0]:
        if not pd.isnull(title):
            country_num = match(country_dict,title)
            if len(country_num)>=2:
                lst.append([frame.iloc[i,0],frame.iloc[i,1],country_num])
        i+=1
    return lst

def process(country_dict):
    frame = build_frame()
    lst = match_country(frame,country_dict)
    pd.DataFrame(lst).to_excel('pair_by_country.xlsx',index = False,header=None)
