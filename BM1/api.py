"""
based from C:\work\rmsa-dev\f1\rmsa-fresco-rmsagit\api_samples\Passer\passer.py
Example usage---
Help: python api.py -h
Local: python api.py -s http://127.0.0.1:8000 rmsa a rmsa 0 1 3 2011 15 3 2011 /Users/emeth/Dropbox/RMSA/data/pos/CR91211.DAT
Dev: python api.py -s http://50.57.86.173 rmsa a json 0 1 3 2011 15 3 2011 /Users/emeth/rmsagit/api_samples/sample.json
PreAlpha: python api.py -s http://50.57.100.166 rmsa a json 0 1 3 2011 15 3 2011 /Users/emeth/rmsagit/api_samples/sample.json
Alpha: python api.py rmsa a json 0 1 3 2011 15 3 2011 /Users/emeth/rmsagit/api_samples/sample.json
"""

import sys, argparse

p = argparse.ArgumentParser(description="Fresco API Connector")
p.add_argument('username', help="Fresco username")
p.add_argument('password', help="Fresco password")
p.add_argument('data_format', help="Format that the data is in: e.g. 'json' or 'rmsa'")
p.add_argument('data_mapping_needed', help="Shows whether data needs mapping to RMSA keys. 1 for true, 0 for false.")
p.add_argument('data_start_day', help="The beginning day that the data is reflective of.")
p.add_argument('data_start_month', help="The beginning month that the data is reflective of.")
p.add_argument('data_start_year', help="The beginning year that the data is reflective of.")
p.add_argument('data_end_day', help="The end day that the data is reflective of.")
p.add_argument('data_end_month', help="The end month that the data is reflective of.")
p.add_argument('data_end_year', help="The end year that the data is reflective of.")
p.add_argument('data_file', help="The full path to the data file.")
p.add_argument('-s', '--server', default="http://fresco.rmsa.com", help="The http address of the Fresco server. Defaults to http://fresco.rmsa.com")
args = p.parse_args(sys.argv[1:])

import urllib
import urllib2
'''
#linux 
input_file = open('/'.join(args.data_file.replace('\\', '/')[1:-1].split('/')))

#windows
>>> 
>>> data_file
'C:\\work\\prodConv\\BM1\\bm1-05-2018.dat'
>>> '/'.join(data_file.replace('\\', '/')[0:].split('/'))
'C:/work/prodConv/BM1/bm1-05-2018.dat'
'''

print 'args='
print args
#quit()
input_file = open('/'.join(args.data_file.replace('\\', '/')[0:].split('/')))
pos_data = input_file.read()
input_file.close()

base_domain = args.server 

api_call = "pos_upload"

post_data = {
                'username' : args.username,
                'password' : args.password,
                'data_format' : args.data_format, #valid formats are "rmsa" and "json"
                'data_mapping_needed': args.data_mapping_needed, #valid values are 0 or 1
                'data_start_day' : args.data_start_day, #First of month
                'data_start_month' : args.data_start_month, #June
                'data_start_year' : args.data_start_year, 
                'data_end_day' : args.data_end_day, #mid month update
                'data_end_month' : args.data_end_month, 
                'data_end_year' : args.data_end_year, 
                'data' : pos_data
            }

#print post_data
#quit()
response = urllib2.urlopen(urllib2.Request(base_domain+'/api/'+api_call+'/', urllib.urlencode(post_data)))
result = response.read()

print result
