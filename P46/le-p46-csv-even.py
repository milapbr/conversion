
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

def readCsv(arq):
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
        if line.startswith('-') or line.startswith('*'):
            continue
        print line
        arqOut.writelines(line+'\n')
        '''
        if m>5:
            quit()
        m+=1
        '''

#readCsv('C:\work\prodConv\P46\csv-07-2018 july even numbers.csv')
readCsv('C:\work\prodConv\P46\csv-07-2018 july even numbers.csv')