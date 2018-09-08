import json
import csv
import urllib
import urllib2

'''

username = raw_input("Username: ")
password = raw_input("Password: ")
customer = raw_input("Customer: ")

'''

def classlist(username, password, customer, save=False):

    url = 'http://fresco.rmsa.com/secretz/class_struct_dump/'
    pdata = {
        'username' : username,
        'password' : password,
        'customer' : customer,
    }
    post_data = urllib.urlencode(pdata)

    req = urllib2.Request(url, post_data)
    response = urllib2.urlopen(req)
    result = response.read()

    native = json.loads(result)
    if save:
        f = open('{0}_class_structure.csv'.format(customer), 'wb')
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    classlistArray={}
    for n in native:
        if save:
            writer.writerow([n['_customer'], n['_store'], n['_department'], n['_class']])
        else:
            #classlistArray=[]
            #classlistArray.append([n['_customer'], n['_store'], n['_department'], n['_class']])
            classlistArray[n['_customer'], n['_store'], n['_department'],n['_class']]= n['_class']
    if save:
       f.close()
    
    print classlistArray
    return classlistArray

username= 'importteam'
password= 'Hq{2q%Bv^5A,_h6t'
customer= 'M33'
classlist(username, password, customer, False)