import pandas as pd
def process_country():
    country_frame = pd.read_excel('country_name.xlsx',engine='openpyxl',header=None)
    country_frame = country_frame.dropna(axis = 0,how = 'all') # 删除空行
    country_dict = {}
    i = 1
    for x in country_frame.itertuples():
        lst = []
        for y in x[1:]:
            if not pd.isnull(y):
                lst.append(y)
        country_dict[i] = tuple(lst)
        i += 1
    return country_dict

