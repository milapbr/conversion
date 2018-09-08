import toDat
import total
import read_map

class file:
	name = ""
	
	def __init__(self, name):
		self.name = name
#-----------------------------------------------------------------------------------------------					#-----------------------------------------------------------------------------------------------

data = {"files":[file("/home/william/shareWin/Project/RS0/2018-05-01 - RSO_Inventory.csv"),
		file("/home/william/shareWin/Project/RS0/2018-05-01 - RSO_Sales.csv"),
		file("/home/william/shareWin/Project/RS0/2018-05-01 - RSO_OnOrder.csv"),
		file("/home/william/shareWin/Project/RS0/2018-05-01 - RSO_Receiving.csv")
		],
		"data_through" :0,
		"data_year" :2018,
		"data_month" :04
		}
table = read_map.map_table("/home/william/Desktop/project/RS0/mapping table.txt").table
#-----------------------------------------------------------------------------------------------					#-----------------------------------------------------------------------------------------------

def convert(data):
	import pandas as pd
	from datetime import datetime
    
	def get_data_template():
		return {"sales":0,
				"inv":0,
				"mdown":0,
				"mup":0,
				"rec_cost":0,
				"rec_retail":0,
				"roo":[0,0,0,0,0,0,0,0,0,0,0,0],
				"coo":[0,0,0,0,0,0,0,0,0,0,0,0],
				"venret":0,
				"tfrin":0,
				"tfrout":0
				}
#-----------------------------------------------------------------------------------------------					#-----------------------------------------------------------------------------------------------
				
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
#-----------------------------------------------------------------------------------------------					#-----------------------------------------------------------------------------------------------

	def parse_sales(dname,output):
		df = pd.read_csv(dname, header = 3)
		df.dropna(axis = 0, how = "all", inplace =True)
		for i in df.iterrows():
			clas = "".join(i[1]["RMSA Category"].split())
			dept = ""
			c_list = clas.split('-')
			
			if c_list[0] == "99":
				clas = "99"
				dept = c_list[1][0:1]
			elif c_list[0] == "304H":
				clas = "304"
			else:
				clas = c_list[0]
			for k,v in table.iteritems():
				if clas == "99":
					continue
				if clas in v:
					dept = k
					break
			key = "001_" + dept + "_" + clas
			if key not in output.keys():
				output[key] = get_data_template()
			output[key]["sales"] = i[1]["Total Sell"]
			output[key]["mdown"] = i[1]["Total Discount"]
		
#-----------------------------------------------------------------------------------------------					#-----------------------------------------------------------------------------------------------

	def parse_oo(dname,output):
		df = pd.read_csv(dname, header = 3)
		df.dropna(axis = 0, how = "all",inplace = True)
		for i in df.iterrows():
			clas = "".join(i[1]["RMSA Class"].split())
			dept = ""
			c_list = clas.split('-')
			
			if c_list[0] == "99":
				clas = "99"
				dept = c_list[1][0:1]
			elif c_list[0] == "304H":
				clas = "304"
			else:
				clas = c_list[0]
			for k,v in table.iteritems():
				if clas == "99":
					continue
				if clas in v:
					dept = k
					break
			key = "001_" + dept + "_" + clas
			if key not in output.keys():
				output[key] = get_data_template()
			output[key]["coo"][0] = i[1][" Total Cost"]
			output[key]["roo"][0] = i[1][" Total Sell"]
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

	def parse_rec(dname,output):
		df = pd.read_csv(dname, header = 3)
		df.dropna(axis = 0, how = "all", inplace =True)
		for i in df.iterrows():
			clas = "".join(i[1]["Row Labels"].split())
			dept = ""
			c_list = clas.split('-')
			
			if c_list[0] == "99":
				clas = "99"
				dept = c_list[1][0:1]
			elif c_list[0] == "304H":
				clas = "304"
			else:
				clas = c_list[0]
			for k,v in table.iteritems():
				if clas == "99":
					continue
				if clas in v:
					dept = k
					break
			key = "001_" + dept + "_" + clas
			if key not in output.keys():
				output[key] = get_data_template()
			output[key]["rec_retail"] = i[1]["Sum of Total Sell"]
			output[key]["rec_cost"] = i[1]["Total Cost"]

		
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

	def parse_inv(dname, output):
		df = pd.read_csv(dname, header = 3)
		df.dropna(axis = 0, how = "all",inplace = True)
		for i in df.iterrows():
			clas = "".join(i[1]["RMSA Class"].split())
			dept = ""
			c_list = clas.split('-')
			
			if c_list[0] == "99":
				clas = "99"
				dept = c_list[1][0:1]
			elif c_list[0] == "304H":
				clas = "304"
			else:
				clas = c_list[0]
			for k,v in table.iteritems():
				if clas == "99":
					continue
				if clas in v:
					dept = k
					break
			key = "001_" + dept + "_" + clas
			if key not in output.keys():
				output[key] = get_data_template()
			output[key]["inv"] = i[1][" Total Sell"]
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
			
	output = {}
	
	for f in data["files"]:
		if "inventory" in f.name.lower():
			parse_inv(f.name, output)
		elif "sales" in f.name.lower():
			parse_sales(f.name, output)
		elif "onorder" in f.name.lower():
			parse_oo(f.name, output)
		elif "receiving" in f.name.lower():
			parse_rec(f.name, output)
	
	
	return clean_output(output)
a = convert(data)
#print a
print total.sum(a)

