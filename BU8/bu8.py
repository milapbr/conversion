
def convert(data):
	import pandas as pd
	from datetime import datetime

#-----------------------------------------------------------------------------------------------					
#-----------------------------------------------------------------------------------------------
				
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

	def parse_sale(output,dname):
		df = pd.read_excel(dname, header = 5, skip_footer = 1, convert_float = False)
		df.dropna(axis = 1, how = "all", inplace = True)
		df.dropna(axis = 0, how = "all", inplace = True)
                dname=cvgstr(dname)
		dex = dname.lower().find("str") + 4
		str_num = dname.lower()[dex:dex + 3]
		df.columns = ["Styles", "Units", "Cost", "Sales", "Margin", "Margin%", "Retail", "Discount"]
		for i in df.iterrows():
			if "JACKETS" in i[1]["Styles"]:
				clas = "40A"
			elif "PANTS" in i[1]["Styles"]:
				clas = "50A"
			elif "HANDBAG" in i[1]["Styles"]:
				clas = "805"
			elif "JEWELLERY" in i[1]["Styles"]:
				clas = "903"	
			else:			
				clas = ((i[1]["Styles"].split(" "))[0])[:2]
				try:
					check = int(clas)
				except ValueError:
					continue
			key  =  str_num + "__" + clas
			if key not in output.keys():
				output[key] = get_data_template()
			output[key]["sales"] += i[1]["Sales"]
			output[key]["mdown"] += i[1]["Discount"]
#-----------------------------------------------------------------------------------------------					
#-----------------------------------------------------------------------------------------------

	def parse_oo(output, dname):
		df = pd.read_excel(dname, convert_float = False, header = 3, parse_cols = "C,E:X")
		#df.dropna(axis = 1, how = "all", inplace = True)
		df = df.reset_index()
		col = list(df.columns)
		col[0] = "Styles"
		col[1] = "Store"
		df.columns = col
		df.dropna(subset = ["Store"], inplace = True)
		df.dropna(axis = 1, how = "all", inplace = True)
		for col in df.columns:
			if df[col].dtype is pd.np.dtype(float):
				df[col].fillna(value = 0, inplace = True)
		for i in df.iterrows():
			if not pd.isnull(i[1]["Styles"]):
				clas = i[1]["Styles"]
				if "JACKETS" in i[1]["Styles"]:
					clas = "40A"
				elif "PANTS" in i[1]["Styles"]:
					clas = "50A"
				elif "HANDBAG" in i[1]["Styles"]:
					clas = "805"
				elif "JEWELLERY" in i[1]["Styles"]:
					clas = "903"	
				else:			
					clas = clas.split(" ")[0][:2]
			str_num = str("{0:03d}".format(int(i[1]["Store"])))
			key = str_num + "__" + clas
			if key not in output.keys():
				output[key] = get_data_template()
			output[key]["coo"][0] += i[1][2]
			output[key]["roo"][0] += i[1][3]
			counter = 0
			duo_check = 0
			for j in range(4,16):
				if (j % 2 == 0):			
					output[key]["coo"][counter] += i[1][j]
					duo_check += 1
				else:
					output[key]["roo"][counter] += i[1][j]
					duo_check += 1
					
				if duo_check == 2:	
					counter += 1
					duo_check = 0
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
	
	
	def parse_rec(output,dname):
		df = pd.read_excel(dname, header = 5, skip_footer = 1, convert_float = False)
		df.dropna(axis = 1, how = "all", inplace = True)
		df.dropna(axis = 0, how = "all", inplace = True)
                dname=cvgstr(dname)
		dex = dname.lower().find("str") + 4
		str_num = dname.lower()[dex:dex + 3]
		df.columns = ["Styles", "Ordered", "Recd", "Cost", "Markup", "Margin%", "Retail"]
		for i in df.iterrows():
			if "JACKETS" in i[1]["Styles"]:
				clas = "40A"
			elif "PANTS" in i[1]["Styles"]:
				clas = "50A"
			elif "HANDBAG" in i[1]["Styles"]:
				clas = "805"
			elif "JEWELLERY" in i[1]["Styles"]:
				clas = "903"	
			else:			
				clas = ((i[1]["Styles"].split(" "))[0])[:2]
				try:
					check = int(clas)
				except ValueError:
					continue
			key  =  str_num + "__" + clas
			if key not in output.keys():
				output[key] = get_data_template()
			output[key]["rec_cost"] += i[1]["Cost"]
			output[key]["rec_retail"] += i[1]["Retail"]
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
			
	def parse_inv(output,dname):
		df = pd.read_excel(dname, header = 5, skip_footer = 1, convert_float = False)
		df.dropna(axis = 1, how = "all", inplace = True)
		df.dropna(axis = 0, how = "all", inplace = True)
                dname=cvgstr(dname)
		dex = dname.lower().find("str") + 4
		str_num = dname.lower()[dex:dex + 3]
		df.columns = ["Styles", "Units", "Cost", "Retail", "Margin", "Margin%"]
		for i in df.iterrows():
			if str_num == "002":
				ignore = ["SUIT", "LEATHER", "SKIRTS"]
				if any(a in i[1]["Styles"] for a in ignore):
					continue
			if "JACKETS" in i[1]["Styles"]:
				clas = "40A"
			elif "PANTS" in i[1]["Styles"]:
				clas = "50A"
			elif "HANDBAG" in i[1]["Styles"]:
				clas = "805"
			elif "JEWELLERY" in i[1]["Styles"]:
				clas = "903"	
			else:			
				clas = ((i[1]["Styles"].split(" "))[0])[:2]
				try:
					check = int(clas)
				except ValueError:
					continue
			key  =  str_num + "__" + clas
			if key not in output.keys():
				output[key] = get_data_template()
			output[key]["inv"] += i[1]["Retail"]
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

        def cvgstr(name):
            name=name.lower()
            if 'str' not in name and '-' in name:
                name=name.split('-')
                name=name[0]+'- str '+name[1]
                name=name.replace('  ',' ')
            return name

#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
					
	output = {}
	for f in data["files"]:
		if "class" in f.name.lower():
			parse_inv(output, f.name)
		elif "sales" in f.name.lower():
			parse_sale(output, f.name)
		elif "receiving" in f.name.lower():
			parse_rec(output, f.name)
		elif "on order" in f.name.lower():
			parse_oo(output, f.name)
	return clean_output(output)