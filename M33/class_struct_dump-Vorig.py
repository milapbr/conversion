import json
import csv
import urllib
import urllib2

'''

username = raw_input("Username: ")
password = raw_input("Password: ")
customer = raw_input("Customer: ")

'''
username= 'importteam'
password= 'Hq{2q%Bv^5A,_h6t'
customer= 'M33'
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
print 'native = ', native

f = open('{0}_class_structure.csv'.format(customer), 'wb')

writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

for n in native:
    print n
    writer.writerow([n['_customer'], n['_store'], n['_department'], n['_class']])

f.close()

