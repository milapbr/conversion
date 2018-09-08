class file:
	name = ""
	
	def __init__(self, name):
		self.name = name

data = {"files":[file("/home/william/shareWin/Project/MBS/sub/Feb 18 full POs.xlsx"),
		file("/home/william/shareWin/Project/MBS/sub/Feb 18 full purch and sales.xlsx")
		#file("/home/william/shareWin/Project/MBS/RMSA PO Info 1217.xlsx"),
		#file("/home/william/shareWin/Project/MBS/RMSA Sales Inventory 1217.xlsx")
		#file("/home/william/shareWin/Project/MBS/PO report - UCM 12.01.17.xlsx"),
		#file("/home/william/shareWin/Project/MBS/sales & inventory  - UCM12.01.17.xlsx")
		],
		"data_through" :0,
		"data_year" :2018,
		"data_month" :2
		}


def total(dic):
	sales = 0
	md = 0
	mp = 0
	inv = 0
	invfo= 0
	recr = 0
	recc = 0
	coo = [0,0,0,0,0,0,0,0,0,0,0,0]
	roo = [0,0,0,0,0,0,0,0,0,0,0,0]
	trin = 0
	tout = 0
	vent = 0

	for k, v in dic.iteritems():
		for key, val in v.iteritems():
			if key == "sales":
				sales += val
			elif key == "mdown":
				md += val
			elif key == "mup":
				mp += val
			elif key == "inv":
				inv += val
			elif key == "inv_fom":
				invfo += val
			elif key == "rec_retail":
				recr += val
			elif key == "rec_cost":
				recc += val
			elif key == "tfrin":
				trin += val
			elif key == "tfrout":
				tout += val
			elif key == "venret":
				vent += val
			elif key == "roo":
				for j in range(12):
					roo[j] += val[j]
			elif key == "coo":
				for j in range(12):
					coo[j] += val[j]


	return {"sales":sales, 
			"mdown":md, 
			"mup":mp, 
			"inv":inv, 
			"inv_fom":invfo, 
			"rec_retail":recr, 
			"rec_cost":recc, 
			"tfrin":trin, 
			"tfrout":tout,
			"venret":vent, 
			"roo":roo, 
			"coo": coo
			}
	
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------		
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

	def parse_data(df,output):
		#check which name in inv_name is used in the data as the header for inventory
		inv_name = ["ENDING INV", "END INVT RETAIL"]
		inv = set(inv_name).intersection(set(df.columns))
		inv = list(inv)[0]
		
		tf_flag = False
		if "TRANSFERS PTD" in df.columns:
			tf_flag = True
			
		for i in df.iterrows():
			try:
				store_num = "00" + str(int(i[1]["STORE NUMBER"]))
			except (KeyError, ValueError):
				store_num = "001"
			if store_num == "00":
				store_num = "001"
			key = str(store_num) + "__" + str(int(i[1]["CLASS NUMBER"])) + "_" + str(int(i[1]["SUBCLASS"]))
			if key not in output.keys():
				output[key] = get_data_template()
			

			output[key]["sales"] += i[1]["SALES PTD"]
			output[key]["mdown"] += i[1]["MARKDOWNS"]
			output[key]["inv"] += i[1][inv]
			output[key]["mup"] += i[1]["MARKUPS"]
			output[key]["rec_cost"] += i[1]["PURCHASES COST"]
			output[key]["rec_cost"] += i[1]["OTHER PURCHASE COST"]
			output[key]["rec_retail"] += i[1]["PURCHASES RETAIL"]
			output[key]["rec_retail"] += i[1]["OTHER PURCHASE RETAIL"]
			output[key]["venret"] += abs(i[1]["RETURN PURCHASE RETAIL"])
			
			if tf_flag:
				if i[1]["TRANSFERS PTD"] >= 0:
					output[key]["tfrin"] += i[1]["TRANSFERS PTD"]
				elif i[1]["TRANSFERS PTD"] < 0:
					output[key]["tfrout"] += abs(i[1]["TRANSFERS PTD"])
					
#-----------------------------------------------------------------------------------------------					#-----------------------------------------------------------------------------------------------

	def parse_oo(df,output):
		fullm = True
		if data.get("data_throught",0) != 0:
			fullm = False
		d_y = data["data_year"]
		d_m = data["data_month"]
		if fullm:
			if d_m + 1 > 12:
				d_m = 1
				d_y = d_y + 1
			else: 
				d_m = d_m + 1
		
		#check which name in ed_name is used in the data as the header for expected date
		ed_name = ["Expected Date", "Expected TrueDate"]
		e_d = set(ed_name).intersection(set(df.columns))
		e_d = list(e_d)[0]		
		
		for i in df.iterrows():
			try:
				store_num = "00" + str(int(i[1]["STORE NUMBER"]))
			except (KeyError, ValueError):
				store_num = "001"
			if store_num == "00":
				store_num = "001"
			key = str(store_num) + "__" + str(int(i[1]["CLASS NUMBER"])) + "_" + str(int(i[1]["SUBCLASS"]))
			if key not in output.keys():
				output[key] = get_data_template()
			datetime_object = datetime.strptime(i[1][e_d], "%m/%d/%y")
			c_y = datetime_object.year
			c_m = datetime_object.month
			
			if c_y < d_y:
				index = 0
			elif c_y == d_y:
				if c_m < d_m:
					index = 0
				elif c_m == d_m:
					index = 0
				elif c_m > d_m:
					index = c_m - d_m
			elif c_y > d_y:
				index = c_m - d_m + 12
				if index > 11:
					index = 11
			output[key]["roo"][index] += i[1]["RETAIL OPEN"]
			output[key]["coo"][index] += i[1]["COST OPEN"]
			
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
			
	output = {}
	for f in data["files"]:
		x = pd.read_excel(f.name)
		x.dropna(axis = 0, how = "any", subset = ["CLASS NUMBER"],inplace = True)
		x["STORE NUMBER"] = x["STORE NUMBER"].fillna(value='')
		x.dropna(axis = 1, how = "all",inplace = True)
		x.fillna(value = "0", inplace = True)
		
		#This for loop is to convert "xxx-" data to "-xxx" 
		for index, row in x.iterrows():
			for col in row.index:
				if ((col != "CLASS NUMBER") and (col != "STORE NUMBER") and ("Date" not in col)) :
					if isinstance(x.loc[index, col], object):
						try:
							x.loc[index, col] = float(x.loc[index, col])
						except ValueError:
							temp = '-' + (x.loc[index, col]).replace(',','')
							x.loc[index, col] = float(temp[:-1])
							
		sale_name = ["sale", "inventory"]
		oo_name = ["oo", "po","on order"]	
			
		if any(name in f.name.lower() for name in sale_name):
			parse_data(x,output)
		elif any(name in f.name.lower() for name in oo_name):
			parse_oo(x,output)
	
	return clean_output(output)

#convert(data)
print total(convert(data))

