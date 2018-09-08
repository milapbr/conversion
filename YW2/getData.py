'''
YW2   YW2 300  851  201  R05000000000000000.00
YW2   YW2 012  765  112  C0500000000000000.000
'''
import time

# your code

def printOut(arq):
    arqIn=open(arq,'r')
    arqOut=open(arq[:-4]+'_out.DAT','w')
    arqEmptyOut=open(arq[:-4]+'_empty.DAT','w')
    for line in arqIn:
        line=line.strip()
        if line.startswith('$$'):
            if not line.endswith('END'):
                line+='\n'
            arqOut.writelines(line)
            arqEmptyOut.writelines(line)
            continue
        valor=line[29:]
        #print 'valor = ', valor
        val=float(valor)
        if val>0:
           arqOut.writelines(line+'\n')
        else:
           arqEmptyOut.writelines(line+'\n')

def printOut1(arq):
    start_time = time.time()
    arqIn = open( arq,'r').readlines()[1:-1]
    elapsed_time = time.time() - start_time
    print 'inner elapsed time:', elapsed_time
    output=[]
    #print arqIn[1:-1]
    skip=0
    for i in arqIn:
        i=i.strip()
        valor=i[29:]
        val=float(valor)
        if val>0:
           output.append(i+'\n')
        '''
        if skip>10:
            break
        skip +=1
        '''
    arqOut=open(arq[:-4]+'_out2.DAT','w')
    arqOut.writelines(output)
    return
def printOut1a(arq):
    start_time = time.time()
    arqIn = open( arq,'r').readlines()[1:-1]
    elapsed_time = time.time() - start_time
    print 'inner elapsed time:', elapsed_time
    output=[]
    #print arqIn[1:-1]
    skip=0
    for i in arqIn:
        valor=i[29:]
        val=float(valor)
        if val>0:
           output.append(i)
        '''
        if skip>10:
            break
        skip +=1
        '''
    arqOut=open(arq[:-4]+'_out2.DAT','w')
    arqOut.writelines(output)
    return

def printOut2(arq):
    start_time = time.time()
    arqIn = open( arq,'r').readlines()[1:-1]
    elapsed_time = time.time() - start_time
    print 'inner elapsed time:', elapsed_time
    output=[]
    for i in arqIn:
        i=i.strip()
        valor=i[29:]
        val=float(valor)
        if val>0:
           output.append(i+'\n')
    return output

def printOut3(arq):
    arqIn = open( arq,'r').readlines()[1:-1]
    output=[]
    for i in arqIn:
        i=i.strip()
        valor=i[29:]
        val=float(valor)
        if val>0:
           output.append(i+'\n')
    return output

def printOut3a(arq):
    arqIn = open( arq,'r').readlines()[1:-1]
    print len(arqIn)
    output=[]
    for i in arqIn:
        valor=i[29:]
        val=float(valor)
        if val>0:
           output.append(i)
    del arqIn
    return output

def printOut3b(rawData):
    output=[]
    for i in rawData:
        valor=i[29:]
        val=float(valor)
        if val>0:
           output.append(i)
    return output

def printOut4(arq):
    arqIn = open( arq,'r').readlines()[1:-1]
    print len(arqIn)
    index=0
    for i in arqIn:
        valor=i[29:]
        val=float(valor)
        if val<=0.0:
           '''
           if index % 5000==0:
               print arqIn[index].strip()
           '''
           del arqIn[index]
           continue
        index+=1
    return arqIn
#printOut('YW2082018.DAT')
start_time = time.time()
#printOut1('YW2082018.DAT')
#printOut1a('YW2082018.DAT')
#x=printOut2('YW2082018.DAT')
x=printOut3a('YW2082018.DAT')
elapsed_time = time.time() - start_time
print 'elapsed time:', elapsed_time
print len(x)
#start_time = time.time()
#x=printOut4('YW2082018.DAT')
#print x
#elapsed_time = time.time() - start_time
#print 'elapsed time:', elapsed_time
#print len(x)

'''
Customer
YW2
 
Sales
5313923
 
MTD Inv
0
 
FOM Inv
0
 
EOM Inv
19132806
 
Markdown
419070
 
Markup
38691
 
Rec@ Cost
2811484
 
Rec@ Retail
6094002
 
Transfer In
276529
 
Transfer Out
257199
 
Chargeback
35826
On Order Cost
Month 1
75243
 
Month 2
3110936
 
Month 3
1617773
 
Month 4
482938
 
Month 5
601538
 
Month 6
0
 
Month 7
0
 
Month 8
0
 
Month 9
0
 
Month 10
0
 
Month 11
0
 
Month 12
0
On Order Retail
Month 1
149588
 
Month 2
6724790
 
Month 3
3547953
 
Month 4
1057229
 
Month 5
1339677
 
Month 6
0
 
Month 7
0
 
Month 8
0
 
Month 9
0
 
Month 10
0
 
Month 11
0
 
Month 12
0
Details
Valid Classes 4414  Info Invalid Classes 0  Info

'''