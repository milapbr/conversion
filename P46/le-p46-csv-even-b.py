'''
based on le-046-csv-even-b.py
'''
def stripChar(string, char):
    while string.count(char * 2)>1:
          string=string.replace(char * 2,char)
    return string.strip(char)  
def readCsv(arq):
    arqIn=open(arq,'r')
    arqOut=open(arq[:-4]+'_out.csv','w')
    skip = True
    i=0
    for line in arqIn: 
        line=line.strip()
        if skip:
            if not line.startswith('Rank,'):
               continue
            else:
               line=stripChar(line,',')
               skip = False
               arqOut.writelines(line+',')
               continue
        line=stripChar(line,',')

        if len(line)==0:
            continue
        if line.startswith('-') or line.startswith('*'):
            continue
        line=line.replace(',*,',',')
        print line
        if i%2==0:
           arqOut.writelines(line+'\n')
        else:
           arqOut.writelines(line+',')
        i+=1
def readCsvToMem(arq):
    arqIn=open(arq,'r')
    arqOut=[]
    skip = True
    i=0
    for line in arqIn: 
        line=line.strip()
        if skip:
            if not line.startswith('Rank,'):
               continue
            else:
               line=stripChar(line,',')
               skip = False
               arqOut.append(line+',')
               continue
        line=stripChar(line,',')

        if len(line)==0:
            continue
        if line.startswith('-') or line.startswith('*'):
            continue
        line=line.replace(',*,',',')
        #print line
        if i%2==0:
           arqOut.append(line+'\n')
        else:
           arqOut.append(line+',')
        i+=1
    print 'arqOut='
    print arqOut

#readCsv('C:\work\conversion\P46\csv-07-2018 july even numbers.csv')
#readCsv('C:\work\conversion\P46\csv-07-2018 july even numbers.csv')
readCsvToMem('C:\work\conversion\P46\csv-07-2018 july even numbers.csv')
