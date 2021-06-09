import pandas as pd
from graph import my_graph

def change(lst):
    result_lst = []
    for x in lst:
        num = len(x)
        for i in range(0,num-1):
            for j in range(i+1,num):
                result_lst.append((x[i],x[j]))
    return result_lst

def count(lst):
    result_lst = []
    tem_set = set(lst)
    for x in tem_set:
        result_lst.append((x[0],x[1],lst.count(x)))
    return result_lst

def read_xlsx():
    data_frame = pd.read_excel('pair_by_country.xlsx',engine='openpyxl',header = None)
    tem_lst = [x.strip('[').strip(']').split(', ') for x in list(data_frame.iloc[:,2])]
    tem_lst = [x for x in tem_lst if len(x)>=2]
    tem_lst = change(tem_lst)
    lst = count(tem_lst)
    return lst

def build_graph():
    G = my_graph()
    lst = read_xlsx()
    G.add_weighted_edges_from(lst)
    return G
