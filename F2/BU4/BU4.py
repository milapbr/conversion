import toDat
import total

class file:
	name = ""
	
	def __init__(self, name):
		self.name = name
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

data = {"files":[file("C:\Users\WSio\Desktop\RMSA Cilent\BU4\\10. RMSA Data 2018 Apr.xls")
		],
		"data_through": 0,
		"data_year": 2018,
		"data_month": 04
		}
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

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
#-----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
				
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
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

	def parse_data(dname,output):	
		df = pd.read_excel(dname, header = None, skiprows = 1, skip_footer=1)
		print df.tail(9)
		for i in df.iterrows():
			dept = str(int(i[1][0]))
			clas = str(int(i[1][1]))
			subc = str(int(i[1][2]))
			str_num = str(int(i[1][3]))
			
			key = str_num + "_" + dept + "_" + clas + "_" + subc
			if key not in output.keys():
				output[key] = get_data_template()
			output[key]["mdown"] += i[1][4] + i[1][5]
			output[key]["mup"] += (i[1][6])
			output[key]["sales"] += i[1][7]
			output[key]["inv"] += i[1][8]
			output[key]["rec_cost"] += i[1][9]
			output[key]["rec_retail"] += i[1][10]
			output[key]["venret"] += abs(i[1][11])
			if data.get("data_through", False):
				output[key]["coo"][0] += i[1][13]
				output[key]["roo"][0] += i[1][14]
				ind = 0
				count = 0
				for j in range(15,37):
					if not j%2 == 0:
						output[key]["coo"][ind] += i[1][j]
						count +=1
					else:
						output[key]["roo"][ind] += i[1][j]
						count +=1
					if count == 2:
						ind += 1
						count = 0
			else:
				ind = 0
				count = 0
				for j in range(13,37):
					if not j%2 == 0:
						output[key]["coo"][ind] += i[1][j]
						count +=1
					else:
						output[key]["roo"][ind] += i[1][j]
						count +=1
					if count == 2:
						ind += 1
						count = 0
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

	
	output = dict()
	
	for f in data["files"]:
		if ("data" in f.name.lower()) and ("po" not in f.name.lower()):
			parse_data(f.name, output)

	return clean_output(output)


a = convert(data)
