def convert(data):
    import pandas as pd
    from datetime import datetime
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------			
    def clean_output(output):
        for k, v in output.iteritems():
            for key, val in v.iteritems():
                if isinstance(val, list):
                    for i in range(len(val)):
                        try:
                            if pd.isnull(val[i]):
                                val[i] = 0
                            else:
                                val[i] = int(round(val[i]))
                        except TypeError:
                            continue
                else:
                    try:
                        if pd.isnull(output[k][key]):
                                output[k][key] = 0
                        else:
                            output[k][key] = int(round(val))
                    except TypeError:
                        continue
        return output
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
    def pxcsv(name):
        """
        this loads csv fill and returns the data 
        """
        newdf = pd.read_csv(name, header=0)
        newdf=newdf.astype(str)
        newdf.rename( columns={'Sales':'sales',\
        'Cost recvd': 'rec_cost', \
        'Retail recvd': 'rec_retail', \
        'Cost on PO': 'coo',\
        'Retl on PO': 'roo', \
        'End retl': 'venret',\
        'Discnts off retl': 'mdown'}, inplace=True )
        return newdf    
          
    def load(df):
        """
        filters out the csv loaded, apply re-mapping rule and loads the vetor with the proper value 
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
        #output = {}
        newMap = {}
        for key, value in zMap.items():
            for string in value:
                newMap.setdefault(string, []).append(key)
        df = df.astype(str)
        for i in df.iterrows():
            index = i[1]["Categ/Subcat"] 
            if index in newMap:
                index=newMap[index][0]
            else:
                #pica mula
                #store/depto/class not configured
                continue
            depto, clas=index.split('/')
            store=stores[index]
            key=store+'_'+depto+'_'+clas
            if key not in output.keys():
                output[key] = get_data_template()  
            '''
            not calculated 
            markup (mpup)
            inventory qtd (inv)
            '''
            output[key]["sales"]      += float(str(i[1]["sales"]).replace(',',''))
            output[key]["rec_cost"]   += float(str(i[1]["rec_cost"]).replace(',',''))           
            output[key]["rec_retail"] += float(str(i[1]["rec_retail"]).replace(',',''))
            output[key]["venret"]     += float(str(i[1]["venret"]).replace(',',''))
            output[key]["coo"][0]     += float(str(i[1]["coo"]).replace(',',''))            
            output[key]["roo"][0]     += float(str(i[1]["roo"]).replace(',',''))
            #output[key]["mup"]        += float(str(i[1]["mup"]).replace(',',''))
            output[key]["mdown"]      += float(str(i[1]["mdown"]).replace(',',''))
            #output[key]["inv"]       += float(str(i[1]["inv"]).replace(',',''))
    # -----------------------------------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------
                
    output = {}
    markup_file = False
    for f in data["files"]:
        df=pxcsv(f)
        load(df)
    return clean_output(output)