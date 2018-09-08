        def cvgstr(name):
            name=name.lower()
            if 'str' not in name and '-' in name:
                name=name.split('-')
                name=name[0]+'- str '+name[1]
                name=name.replace('  ',' ')
            return name

for i in ['Class Summary - str 002 BDC', 'Class Summary - 002 BDC','Class Summary-002 BDC','Class Summary -  002 BDC','Class Summary-  002 BDC']:
    i2=cvgstr(i)
    print i,'\n',i2
    print 