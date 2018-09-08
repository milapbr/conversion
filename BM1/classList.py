"""

##########################################
#   this solution has been deprecated.   #
##########################################

###############################################
#   please use class_struct_dump.py instead   #
###############################################

based from C:\work\rmsa-dev\f1\rmsa-fresco-rmsagit\customers\views\api_views.py
Example usage---
Help: python classList.py -h
Local: python classList.py -s http://127.0.0.1:8000 <username> <password> <customer id> 
reg:   python classList.py -s https://reg.rmsa.com/ <username> <password> <customer id> 
qa:    python classList.py -s https://qa.rmsa.com/ <username> <password> <customer id> 
Dev:   python classList.py -s https://dev.rmsa.com/ <username> <password> <customer id> 
ua:    python classList.py -s https://ia.rmsa.com/ <username> <password> <customer id> 
prod:  python classList.py -s https://fresco.rmsa.com/ <username> <password> <customer id> 

Customer ID M33
python classList.py -s https://reg.rmsa.com/ importteam importteam1 M33

https://reg.rmsa.com/export_plan/quick_class_list/
"""

import sys, argparse

p = argparse.ArgumentParser(description="Fresco API Connector")
p.add_argument('username', help="Fresco username")
p.add_argument('password', help="Fresco password")
p.add_argument('customer', help="Fresco customer id")
p.add_argument('-s', '--server', default="http://fresco.rmsa.com", help="The http address of the Fresco server. Defaults to http://fresco.rmsa.com")
args = p.parse_args(sys.argv[1:])

print 'args=', args
#quit()
import urllib
import urllib2

base_domain = args.server 

#api_call = "class_struct_dump"
#https://reg.rmsa.com/export_plan/quick_class_list/
#api="/export_plan/"
#api_call="quick_class_list/"

#api="/print_class_structure/"

post_data = {
                'username' : args.username,
                'password' : args.password,
                'customer' : args.customer
            }

#response = urllib2.urlopen(urllib2.Request(base_domain+api+api_call+'/', urllib.urlencode(post_data)))
#response = urllib2.urlopen(urllib2.Request(base_domain+api+'/', urllib.urlencode(post_data)))

#api = "/class_struct_dump/"
#https://reg.rmsa.com/export_plan/class_struct_dump/  not found
#https://reg.rmsa.com/export_plan/quick_class_list/
#api = "/export_plan/quick_class_list/"  return html elements not data
#api = "/print_class_structure/" ** 404 not found **
#api_call = "/export_tool/print_class_structure/" 
api_call = "/print_class_structure/" 
api_call = "/class_struct_dump/"
#https://reg.rmsa.com//export_tool/print_class_structure/
#https://reg.rmsa.com/export_plan/quick_class_list/

#response = urllib2.urlopen(urllib2.Request(base_domain+api+'/', urllib.urlencode(post_data)))
#response = urllib2.urlopen(urllib2.Request(base_domain+'/api/'+api_call+'/', urllib.urlencode(post_data)))
print 'url = ', base_domain+api_call+'/'
response = urllib2.urlopen(urllib2.Request(base_domain+api_call+'/', urllib.urlencode(post_data)))

result = response.read()

print result
