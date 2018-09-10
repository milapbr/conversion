
def readCsv1(arq):
    arqIn=open(arq,'r')
    arqOut=open(arq[:-4]+'_out.csv','w')
    m=0
    skip = True
    for line in arqIn: 
        line=line.strip()
        if skip:
            if not line.startswith('Rank,'):
               continue
            else:
               skip = False
        while line.count(',,')>1:
            line=line.replace(',,',',')
        line=line.strip(',')
        if len(line)==0:
            continue
        #print 'lineA=', line
        #if len(line)
        #print 'lineB=', line
        
        lineD=[line]
       
        print 'lineD1=', lineD
        lineE=[]
        print 'line=', line
        if line[0:1]=='"':
            max=3
            lineD=lineD[0].split(',')
            print 'lineD2=', lineD
            for i in lineD:
                lineE.append(i)

        else:
            max=9
            lineD=[line]
            for i in range(max):
                lineE.append(lineD[0][i])
        #print 'lineB=', line
        print 'lineE=', lineE
        if m>5:
            quit()
        m+=1

def stripChar(string, char):
    while string.count(char * 2)>1:
          string=string.replace(char * 2,char)
    return string.strip(char)  
def readCsv(arq):
    arqIn=open(arq,'r')
    arqOut=open(arq[:-4]+'_out.csv','w')
    m=0
    skip = True
    i=0
    for line in arqIn: 
        line=line.strip()
        if skip:
            if not line.startswith('Rank,'):
               continue
            else:
               #print line
               line=stripChar(line,',')
               #print line
               #exit()
               skip = False
               arqOut.writelines(line+',')
               continue
        line=stripChar(line,',')
        '''
        while line.count(',,')>1:
            line=line.replace(',,',',')
        
        line=line.strip(',')
        '''
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
        '''
        if m>5:
            quit()
        m+=1
        '''

#readCsv('C:\work\conversion\P46\csv-07-2018 july even numbers.csv')
#readCsv('C:\work\conversion\P46\csv-07-2018 july even numbers.csv')
#readCsv('work-csf-08-2018 August even report.csv')
readCsv('C:\work\conversion\P46\work-csv-08-2018 August odd report.csv')