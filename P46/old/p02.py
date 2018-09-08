'''
depto 4
mapping
{(4, 39): [39], (4, 28): [28], (4, '40A'): [26, 262, 264, 268, 280, 286, 290, 292, 298], (4, 18): [18], (4, 36): [36], (13, '40B'): [2, 4], (4, 16): 16, (4, 12): [10, 12, 14], (4, 22): [22], (4, 24): [24], (4, 34): [34], (4, 20): [20], (4, 30): [30, 32], (4, 38): [38]}
'''

import sys
from datetime import datetime
import pandas as pd
name='p46-dept-04.xlsx'
even='07-2018 july even numbers.xls'

def px3(name):

    df = pd.read_excel(name, header=19)
    newdf=df.drop(df.columns[[1,2,3,4,6,8,9,11,12,14,15,16,17,19,20,22,23,25,26,28,29,31,32]], axis=1, inplace=True)  
    newdf=df.fillna('*')
    newdf.rename( columns={'Unnamed: 7':'Sales'}, inplace=True )
    newdf=newdf.astype(str)
    filter1 = newdf.loc[newdf["Rank"]!= '*']
    df2=newdf.query("Rank !='*' or Sales !='*'")
   
    #print df
    print df2
    quit()

def px4(name):

    df = pd.read_excel(name, header=19)
    df2=df.drop(df.columns[[1,2,3,4,6,8,9,11,12,14,15,16,17,19,20,22,23,25,26,28,29,31,32]], axis=1, inplace=True)  
    df2 = df2.fillna('*')
    df2.rename( columns={'Unnamed: 7':'Sales'}, inplace=True )
    df2=df2.astype(str)
    df2=df2.query("Rank !='*' or Sales !='*'")
    print df2
    quit()


px3(even)