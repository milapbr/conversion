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

def px(name):
    """
    this loadas excel fill and returns the data 
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

    return newdf

def load(df):
    """
    filters out the excel loaded, apply re-mapping rule and loads the vetor with the proper value 
    """
    #hard coded
    # stores 
    stores={'07/166A': '001', '09/191C': '002', '05/66': '001', '04/39': '001', '04/38': '001', '04/18': '001', '04/30': '001', '04/36': '001', '04/34': '001', '06/140A': '001', '04/16': '001', '07/174A': '001', '05/42': '001', '07/150': '001', '06/102': '001', '06/136': '001', '06/104': '001', '06/106': '001', '06/108': '001', '06/122': '001', '09/190C': '002', '04/12': '001', '09/40C': '002', '06/128': '001', '04/24': '001', '04/20': '001', '04/22': '001', '05/91A': '001', '04/28': '001', '04/40B': '001', '04/40A': '001', '07/160': '001', '05/78': '001', '07/126': '001', '05/90': '001', '09/140C': '002', '08/800': '001', '07/190A': '001', '05/64': '001', '09/90C': '002', '06/138': '001', '05/88': '001'}
    # this was based on the current RMSA mapping for this P46 customer
    # business rules 
    zMap={}  
    zMap={('04/12'): ['010','012','014'], \
    ('04/16'): ['016'],  \
    ('04/18'): ['018'], \
    ('04/20'): ['020'], \
    ('04/22'): ['022'], \
    ('04/24'): ['24'],  \
    ('04/28'): ['028'], \
    ('04/30'): ['030','032'], \
    ('04/34'): ['034'], ('04/36'): ['036'],  ('04/38'): ['038','288'],  \
    ('04/39'): ['289'], \
    ('04/40A'):['026','262','264','268','280','286','290','292','298'], \
    ('13/40B'):['02','04'], 
    ('05/42'): ['042','046','048','054'], \
    ('05/64'): ['064'], \
    ('05/66'): ['066','068'], \
    ('05/78'): ['078'], \
    ('05/88'): ['312','316','318','322','324'],  \
    ('05/90A'):['096','402','404'],  \
    ('05/91A'):['062','070','072','074','082','086','088','090'],  \
    ('06/102'):['102'], \
    ('06/104'):['104'], \
    ('06/106'):['106'],  \
    ('06/108'):['108'],  \
    ('06/122'):['122','124'],  \
    ('06/128'):['128'],  \
    ('06/136'):['136'],  \
    ('06/138'):['138','144','146'], \
    ('06/140A'):['110','148','150','166'], \
    ('07/126'):['126'],  \
    ('07/150'):['150'],  \
    ('07/160'):['160'],  \
    ('07/166'):['158','164'],  \
    #('07/166'):['158','164','166'],  \
    ('07/174'):['170','174','176','178'],  \
    ('07/190A'):['152','154','156','162','180']}
    
    """
    orig
    zMap={('04/39'):['039'], ('04/28'):['028'], ('04/40A'): ['026','262','264','268','280','286','290','292','298'], ('04/18'): ['018'], \
    ('04/36'):  ['36'],('13/40B'): ['02','04'], ('04/16'):  ['016'], ('04/12'): ['010','012','014'], ('04/22'):  ['022'], \
    ('04/24'):  ['24'], ('04/34'):  ['034'], ('04/20'):  ['020'], ('04/30'):  ['030','032'], ('04/38'):  ['038']}
"   

       zMap={('04/39'):['039'], ('04/28'):['028'], ('04/40A'): ['026','262','264','268','280','286','290','292','298'], ('04/18'): ['018'], \
    ('04/36'):  ['36'],('13/40B'): ['02','04'], ('04/16'):  ['016'],  ('04/22'):  ['022'], \
    ('04/24'):  ['24'], ('04/34'):  ['034'], ('04/20'):  ['020'],  ('04/38'):  ['038']}


       zMap={('04/39'):['039'], ('04/28'):['028'], ('04/40A'): ['026','262','264','268','280','286','290','292','298'], ('04/18'): ['018'], \
    ('04/36'):  ['36'],('13/40B'): ['02','04'], ('04/16'):  ['016'],  ('04/22'):  ['022'], \
    ('04/24'):  ['24'], ('04/34'):  ['034'], ('04/20'):  ['020'],  ('04/38'):  ['038']}

    ('04/288'):['38']
    """
    newMap = {}
    for key, value in zMap.items():
        for string in value:
            newMap.setdefault(string, []).append(key)
    skip = True
    print newMap
    for i in newMap:
        print i, newMap[i]
    quit()
    vetor={}
    df = df.astype(str)
    #print df
    #quit()
    for i in df.iterrows():
        if skip:
            skip = False
            continue
        #print i[1]["Categ/Subcat"]
        '''
        clas = i[1]["Categ/Subcat"].split('/')[1]
        print 'class = ', clas
        key=''
        if clas in newMap:
            store=newMap[clas][0]
            depto, clas=store.split('/')
            store=stores[store]
            #print clas, ' was found in the mapp:'
        else:
            print clas, ' WAS NOT FOUND in the mapp'
            quit()
        key=store+'_'+depto+'_'+clas
        print 'store= ', store, ' depto=', depto, '  class= ', clas
        print key
        '''

        # debug mode only
        # print 'clas=',clas  
        
        clas = i[1]["Categ/Subcat"]   
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
            #clas=clas.split('/')[1]
            index=clas
            #print i[1]["Categ/Subcat"]        
            #store = 
            #clas = i[1]["Categ/Subcat"].split('/')[1]
            #print 'class = ', clas
            key=''
            depto, clas = i[1]["Categ/Subcat"].split('/')
            store='**'
            print 'store= ', store, ' depto=', depto, '  class= ', clas   
            if clas in newMap:
                store=newMap[clas]
                store=newMap[clas][0]
                #depto, clas=store.split('/')
                #store=stores[store]
                print clas, ' was found in the mapp:'
            else:
                print 'else...'
                print 'clas=',clas
                chave=depto+'/'+str(int(clas))
                store=stores[chave]
                print clas, ' WAS NOT FOUND in the mapp'
                print (i[1]["Categ/Subcat"])
                print 'store= ', store, ' depto=', depto, '  class= ', clas   
            key=store+'_'+depto+'_'+clas
            #print 'store= ', store, ' depto=', depto, '  class= ', clas
            #print key
        

        
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
