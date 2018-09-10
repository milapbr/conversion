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
even='08-2018 August even report.xls'
def px1(name):
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

def px(name):
    """
    this loadas excel fill and returns the data 
    """
    df = pd.read_excel(name, header=19)
    newdf=df.drop(df.columns[[1,2,3,4,6,8,9,11,12,14,15,16,17,19,20,22,23,25,26,28,29,31,32]], axis=1, inplace=True)  
    newdf=df.fillna('*')
    newdf.rename( columns={'Unnamed: 7':'sales',\
    'Unnamed: 10': 'rec_retail', \
    'Unnamed: 13': 'rec_cost',\
    'Unnamed: 18': 'venret',\
    'Unnamed: 21': 'coo',\
    'Unnamed: 24': 'roo', \
    'Unnamed: 27': 'inv',\
    'Unnamed: 30': 'mup',\
    'Unnamed: 33': 'mdown'}, inplace=True )
    newdf=newdf.astype(str)
    newdf=newdf.query("Rank !='*' or sales !='*'")
    ##print newdf
    ##quit()
    return newdf
def get_data_template():
		return {"sales":0,
				"inv":0,
				"mdown":0,
				"mup":0,
				"rec_cost":0,
				"rec_retail":0,
				"roo":[0,0,0,0,0,0,0,0,0,0,0,0],
				"coo":[0,0,0,0,0,0,0,0,0,0,0,0],
				"venret":0,
				"tfrin":0,
				"tfrout":0
				}
def load(df):
    """
    filters out the excel loaded, apply re-mapping rule and loads the vetor with the proper value 
    """
    #hard coded
    # stores 
    stores={'07/166A': '001', '09/191C': '002', '05/66': '001', '04/39': '001', '04/38': '001', '04/18': '001', \
    '04/30' : '001', '04/36'  : '001', '04/34'  : '001', '06/140A': '001',  '04/16' : '001', '07/174A': '001', \
    '05/42' : '001', '07/150' : '001', '06/102' : '001', '06/136' : '001',  '06/104': '001', '06/106' : '001', \
    '06/108': '001', '06/122' : '001', '09/190C': '002', '04/12'  : '001',  '09/40C': '002', '06/128' : '001', \
    '04/24' : '001', '04/20'  : '001', '04/22'  : '001', '05/91A' : '001',  '04/28' : '001', '04/40B' : '001', \
    '04/40A': '001', '07/160' : '001', '05/78'  : '001', '07/126' : '001',  '05/90' : '001', '09/140C': '002', \
    '08/800': '001', '07/190A': '001', '05/64'  : '001', '09/90C' : '002',  '06/138': '001', '05/88'  : '001'}
    # this was based on the current RMSA mapping for this P46 customer
    # business rules 
    zMap={}  
    zMap={('04/12'): ['04/010','04/012','04/014'], \
    ('04/16'): ['04/016'], \
    ('04/18'): ['04/018'], \
    ('04/20'): ['04/020'], \
    ('04/22'): ['04/022'], \
    ('04/24'): ['04/024'], \
    ('04/28'): ['04/028'], \
    ('04/30'): ['04/030','04/032'], \
    ('04/34'): ['04/034'], \
    ('04/36'): ['04/036'], \
    ('04/38'): ['04/038','04/288'], \
    ('04/39'): ['04/289','04/296'], \
    ('04/40A'):['04/026','04/262','04/264','04/268','04/176', '04/280','04/286','04/290','04/292','04/294', '04/298', '04/9900'], \
    ('04/40B'):['04/02','04/04','13/2','13/4'], 
    ('05/42'): ['05/042','05/046','05/048','05/054'], \
    ('05/64'): ['05/064'], \
    ('05/66'): ['05/066','05/068'], \
    ('05/78'): ['05/078'], \
    ('05/88'): ['05/312','05/316','05/318','05/322','05/324'],  \
    ('05/90'): ['05/096','12/402','12/404'],  \
    #('05/90'):['05/096','05/402','05/404'],  \
    ('05/91A'):['05/062','05/070','05/072','05/074','05/082','05/086','05/088','05/090','05/9900'],  \
    ('06/102'):['06/102'], \
    ('06/104'):['06/104'], \
    ('06/106'):['06/106'], \
    ('06/108'):['06/108'], \
    ('06/122'):['06/122','06/124'], \
    ('06/128'):['06/128'], \
    ('06/136'):['06/136'], \
    ('06/138'):['06/138','06/144','06/146'], \
    ('06/140A'):['06/110','06/148','06/150','06/166','06/9900'], \
    ('07/126'):['07/126','06/126'], \
    ('07/150'):['07/150'], \
    ('07/160'):['07/160'], \
    ('07/166A'):['07/158','07/164','07/166'],  \
    #('07/166'):['158','164','166'],  \
    ('07/174A'):['07/170','07/174','07/176','07/178'],  \
    ('07/190A'):['07/152','07/154','07/156','07/162','07/180','07/9900'], \
    ('08/800') :['08/004','08/010','08/014','08/032','08/034','08/036','08/104','08/122','08/126','08/148','08/160','08/166','08/9900'], \
    ('09/190C'):['09/9900'], \
    ('09/191C'):['10/240','10/246','10/248','10/250','10/298','10/9900','11/008', '11/9900']}
    output = {}
    newMap = {}
    for key, value in zMap.items():
        for string in value:
            newMap.setdefault(string, []).append(key)
    skip = True
    ##print newMap
    '''
    for i in newMap:
        print i, newMap[i]
    ##quit()
    '''
    vetor={}
    df = df.astype(str)
    #print df
    #quit()
    for i in df.iterrows():
        if skip:
            skip = False
            continue
        # debug mode only
        # print 'clas=',clas 
        index = i[1]["Categ/Subcat"]   
        if index =='*':
            vetor[index]=[i[1]["sales"], \
            i[1]["rec_cost"], \
            i[1]["rec_retail"], \
            i[1]["venret"], \
            i[1]["coo"], \
            i[1]["roo"], \
            i[1]["inv"], \
            i[1]["mup"], \
            i[1]["mdown"]]
            print [i[1]["sales"]]
        else:
            #print 'index=', index
            if index in newMap:
                index=newMap[index][0]
                #print 'new index=', index
            depto, clas=index.split('/')
            depto=str(int(depto))
            store=stores[index]
            #print 'store=', store, ' depto=', depto, '  class=', clas   
            key=store+'_'+depto+'_'+clas
            if key not in output.keys():
               output[key] = get_data_template()
            
            #output[key]["sales"]    += float([i[1]["sales"])
            #print i[1]["sales"]
            #output[key]["sales"]  =+ float("".join(i[1]["sales"].split(",")))
            #'''
            '''
            print [i[1]["rec_cost"]]
            print vetor
            quit()
            '''
            #output[key]["rec_cost"] += float("".join(i[1]["rec_cost"].split(",")))
            '''
            output[key]["venret"]   += float([i[1]["venret"])
            output[key]["coo"]      += float([i[1]["coo"])
            
            output[key]["roo"]      += float([i[1]["roo"])
            output[key]["mup"]      += float([i[1]["mup"])
            output[key]["mdown"]    += float([i[1]["mdown"])
            '''

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
