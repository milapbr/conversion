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
def px1(name):
    df = pd.read_excel(name, header = 1)
    #df = df.loc[df["ID"].str.startswith("PO-")]
    #df = df.astype(str)
    #print df 
    classe={}
    x=0
    for i in df.iterrows():
        print 'i full=',i
        print '--------------------------------'
        for k in range(4):
            print i[k]
        print '--------------------------------'
        if x%2==0:
            print 'ipar=',i
            index=[i[1]]
        else:
            print 'i<impar>=',i
            classe[index]=[i[2], i[4],i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
            print 'classe[',index,']==>'
            print classe[index]
        x+=1
        if x>1:
            quit()  
def px2(name):
    df = pd.read_excel(name, header = 1)
    df = df.astype(str)
    #print df 
    classe={}
    x=0
    for i in df.iterrows():
        xx=str(i).strip()
        print 'xx=',xx
        print xx[0]
        quit()
        print '++++++++++++++++++++++++++++++++'
        print 'i full=',i
        quit()
        print '--------------------------------'
        
        for k in range(2):
            print 'k=',k,'  i[',k,']=',i[k]
        print '--------------------------------'
        #print 'i<impar>=',i
        quit()
        index=i[1]
        print i[0], i[1]
        print 'Index=', index
        classe[index]=[i[4],i[5], i[6], i[7], i[8], i[9], i[10]]
        print 'classe[',index,']==>'
        print classe[index]
        x+=1
        if x>1:
            quit()  
def px3(name):
    #df = pd.read_excel(name, header = 19, nrows=0)
    #df = pd.read_excel(name, header=19)
    #df = pd.read_excel(name, header=20)
    #erro df = pd.read_excel(name, header=21)
    #df = pd.read_excel(name, nrows=40)
    df = pd.read_excel(name, header=19)

    #df.dropna(axis = 1, inplace = True, how = "all")
    #df.drop(df.columns[[0, 1, 3, 4, 6, 9, 11, 13, 15, 17, 19, 22]], axis=1, inplace=True)  
    # df.columns is zero-based pd.Index df.drop(df.columns[[0, 1, 3, 4, 6, 9, 11, 13, 15, 17, 19, 22]], axis=1, inplace=True)  # df.columns is zero-based pd.Index 
    #df.dropna(df.columns[[0, 1, 3, 4, 6, 9, 11, 13, 15, 17, 19, 22]], axis=1, inplace=True)  
    #df = df.astype(str)
    #df.skip()
    newdf=df.drop(df.columns[[1,2,3,4,6,8,9,11,12,14,15,16,17,19,20,22,23,25,26,28,29,31,32]], axis=1, inplace=True)  
    newdf=df.fillna('*')
    newdf.rename( columns={'Unnamed: 7':'Sales'}, inplace=True )
    newdf=newdf.astype(str)
    #df2 = newdf.loc[newdf["Rank"].str.startswith("*")]
    #df2 = newdf.loc[newdf["Rank"].str.startswith("*")]
    #df2 = newdf.loc[newdf["Rank"]!= '*'] or newdf.loc[newdf["Unnamed: 7"]!='*'] 
    #df2 = newdf.loc[newdf["Rank"]!= '*'] 
    #df2 = newdf.loc[newdf["Unnamed: 7"]!='*'] 
    filter1 = newdf.loc[newdf["Rank"]!= '*']
    ##filter2 = newdf.loc[newdf["Unnamed: 7"]!='*'] 
    ###df2=df.filter1.filter2
    #df2=newdf.query(newdf["Rank"] !='*' or newdf["Unnamed: 7"] !='*')
    df2=newdf.query("Rank !='*' or Sales !='*'")
   
    #print df
    print df2
    quit()
    print newdf
    quit() 
    classe={}
    x=0
    for i in df.iterrows():
        xx=str(i).strip()
        print 'xx=',xx
        print xx[0]
        quit()
        print '++++++++++++++++++++++++++++++++'
        print 'i full=',i
        quit()
        print '--------------------------------'
        
        for k in range(2):
            print 'k=',k,'  i[',k,']=',i[k]
        print '--------------------------------'
        #print 'i<impar>=',i
        quit()
        index=i[1]
        print i[0], i[1]
        print 'Index=', index
        classe[index]=[i[4],i[5], i[6], i[7], i[8], i[9], i[10]]
        print 'classe[',index,']==>'
        print classe[index]
        x+=1
        if x>1:
            quit()  

#px2(name)
px3(even)