##if string in 'suit','wool'SUIT/WOOL  Suits/100% WOOL SUIT

import pandas as pd
from datetime import datetime

def parse_classlist(name):
    df = pd.read_table(name, header = 0)
    print df
    #df.dropna(axis = 1, inplace = True, how = "all")
    df.dropna(axis = 1, inplace = False, how = "all")
    
    print df
    #df.dropna(subset = ["Class.1"], inplace = True)
    for i in df.iterrows():
        #print type(i)
        print i[1]
file='averaged_out_margins.xlsx'
file='MB2-ClassList.csv'
#salesname='Custom - Sales Report - RMSA - April.txt'
#onhand='Custom - Monthly Inventory On Hand - April.txt'
#inventoryname='Custom - Inventory History - RMSA - April.txt'
#print 'type1'+'\t'+'transaction'+'\t'+'value'+'\t'
#x = pd.read_excel(file)
#print x
#parse_classlist(file)

#XXX df = pd.read_csv(file, index_col='Description', names=['Customer','Store','Department','Class'])
#ok df = pd.read_csv(file)
## ok df = pd.read_csv(file, header=None)
df = pd.read_csv(file, index_col='Description', names=['Customer','Store','Department','Class','Description'])
print df
print ('.........................')
struct={}
for i in df.iterrows():
    #print i
    print i[0], i[1][0], i[1][1], i[1][2], i[1][3]
    struct[i[0]]
