'''
depto 4
mapping
z={}
z={(4, 39): [39], (4, 28): [28], (4, '40A'): [26, 262, 264, 268, 280, 286, 290, 292, 298], (4, 18): [18], (4, 36): [36], (13, '40B'): [2, 4], (4, 16): 16, (4, 12): [10, 12, 14], (4, 22): [22], (4, 24): [24], (4, 34): [34], (4, 20): [20], (4, 30): [30, 32], (4, 38): [38]}

{('04/39'): [39], (4, 28): [28], (4, '40A'): [26, 262, 264, 268, 280, 286, 290, 292, 298], (4, 18): [18], (4, 36): [36], (13, '40B'): [2, 4], (4, 16): 16, (4, 12): [10, 12, 14], (4, 22): [22], (4, 24): [24], (4, 34): [34], (4, 20): [20], (4, 30): [30, 32], (4, 38): [38]}

'''

import sys
from datetime import datetime
import pandas as pd
even='07-2018 july even numbers.xls'

def px4(name):
    """
    this loads excel file and extract the
    """
    df = pd.read_excel(name, header=19)
    newdf=df.drop(df.columns[[1,2,3,4,6,8,9,11,12,14,15,16,17,19,20,22,23,25,26,28,29,31,32]], axis=1, inplace=True)  
    newdf=df.fillna('*')
    newdf.rename( columns={'Unnamed: 7':'Sales',\
    'Unnamed: 10': 'Cost of sales', \
    'Unnamed: 13':'Cost recvd',\
    'Unnamed: 18':'Retail recvd',\
    'Unnamed: 21': 'Cost on PO',\
    'Unnamed: 24': 'Retl on PO', \
    'Unnamed: 27': 'Cost on hand',\
    'Unnamed: 30': 'End retl',\
    'Unnamed: 33': 'Discnts off retl'}, inplace=True )
    newdf=newdf.astype(str)
    newdf=newdf.query("Rank !='*' or Sales !='*'")
    print newdf
    quit()

def px(name):

    df = pd.read_excel(name, header=19)
    newdf=df.drop(df.columns[[1,2,3,4,6,8,9,11,12,14,15,16,17,19,20,22,23,25,26,28,29,31,32]], axis=1, inplace=True)  
    newdf=df.fillna('*')
    newdf.rename( columns={'Unnamed: 7':'Sales',\
    'Unnamed: 10': 'Cost of sales', \
    'Unnamed: 13':'Cost recvd',\
    'Unnamed: 18':'Retail recvd',\
    'Unnamed: 21': 'Cost on PO',\
    'Unnamed: 24': 'Retl on PO', \
    'Unnamed: 27': 'Cost on hand',\
    'Unnamed: 30': 'End retl',\
    'Unnamed: 33': 'Discnts off retl'}, inplace=True )
    newdf=newdf.astype(str)
    newdf=newdf.query("Rank !='*' or Sales !='*'")
    #df.dropna(axis = 1, inplace = True, how = "all")
    ## not working newdf.dropna(colum ='Rank', axis = 1, inplace = True, how = "all")
    ##print newdf.columns
    ###S    newdf.drop(newdf.columns[0], axis=1, inplace=True)  
    ##print newdf.columns
    #quit()
    ##print newdf
    ##quit()
    return newdf

def load(df):
    skip = True
    vetor={}
    df = df.astype(str)
    z=0
    for i in df.iterrows():
        #print i
        z+=1
        if z>5000:
            print 'vetor='
            print vetor
            quit()
        if skip:
            skip = False
            continue
        clas = i[1]["Categ/Subcat"]
        print 'clas=',clas
        #quit()
        
        if clas =='*':
            vetor[index]=[i[1]["Sales"], \
            i[1]["Cost of sales"], \
            i[1]["Cost recvd"],    \
            i[1]["Retail recvd"],  \
            i[1]["Cost on PO"],    \
            i[1]["Retl on PO"],    \
            i[1]["Cost on hand"],  \
            i[1]["End retl"],      \
            i[1]["Discnts off retl"]]
        else:
            index=clas
        
        key = "001__" + clas
        '''
        if key not in output.keys():
            output[key] = get_data_template()
        output[key]["sales"] += float("".join(i[1]["Total Sell"].split(",")))
        output[key]["mdown"] += float("".join(i[1]["Total Discount"].split(",")))
        '''

    print vetor
    
#df=px4(even)
df=px(even)
load(df)
