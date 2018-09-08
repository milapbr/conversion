import sys
from datetime import datetime
import pandas as pd
##parse classList
'''
Customer,Store,Department,Class,Description
P46,001,04,12,SOLID MULTI CL TOWEL
P46,001,04,16,EMBROIDERED TOWELS
P46,001,04,18,GUEST TIP TOWELS
P46,001,04,20,TUB MATS
P46,001,04,22,OUTDOOR TOWELS
P46,001,04,24,BATH SHEETS
P46,001,04,28,ROBES/WRAPS
'''

def classpx(name):

    df = pd.read_csv(name, header=0, dtype=str)
    df = df.astype(str)
    df.drop(df.columns[[0,4]], axis=1, inplace=True)  
    v={}
    for i in df.iterrows():
        v[i[1][1]+'/'+i[1][2]]=i[1][0]
    print v
        
classpx('p46-classlist.csv')
