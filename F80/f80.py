def convert(data):
	import pandas as pd
	from datetime import datetime
# -----------------------------------------------------------------------------------------------
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
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
	def parse_sales(dname,output):
		df = pd.read_excel(dname, header = 8, skip_footer = 2)
		df.dropna(axis = 1, how = "all", inplace = True)
		df.dropna(axis = 0, how = "all", inplace = True)

		for i in df.iterrows():
			str_num = str(int(i[1]["Str"])).rjust(3,'0')
			dcs = i[1]["DCS Code"].split("  ")
			while len(dcs) < 3:
				dcs.append(" ")
			dept = dcs[0]
			clas = dcs[1]
			sub = dcs[2]
			key = "".join((str_num + "_" + dept + "_" + clas + "_" + sub).split())

			if key not in output.keys():
				output[key] = get_data_template()
			output[key]["sales"] += i[1]["Ext Price"]
			output[key]["mdown"] += i[1]["EXT_DISC_AMT"]
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
	def parse_inv(dname,output):
		df = pd.read_excel(dname, header = 5, skip_footer = 1)
		df.dropna(axis = 1, how = "all", inplace = True)
		df.dropna(axis = 0, how = "all", inplace = True)
		df.dropna(subset = ["DCS Code"], inplace = True)

		for i in df.iterrows():
			str_num = str(int(i[1]["Store"])).rjust(3,'0')
			dcs = i[1]["DCS Code"].split("  ")
			while len(dcs) < 3:
				dcs.append(" ")
			dept = dcs[0]
			clas = dcs[1]
			sub = dcs[2]
			key = "".join((str_num + "_" + dept + "_" + clas + "_" + sub).split())

			if key not in output.keys():
				output[key] = get_data_template()
			output[key]["inv"] += i[1]["Ext Price"]
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
	def parse_rec(dname,output):
		df = pd.read_excel(dname, header = 19, skip_footer = 7)
		df.dropna(axis = 1, how = "all", inplace = True)
		df.dropna(axis = 0, how = "all", inplace = True)
		df = df[["DCS","Cost", "Price"]]
		df.dropna(subset = ["DCS"], inplace = True)
		for i in df.iterrows():
			str_num = "900"
			dcs = i[1]["DCS"].split("  ")
			while len(dcs) < 3:
				dcs.append(" ")
			dept = dcs[0]
			clas = dcs[1]
			sub = dcs[2]
			key = "".join((str_num + "_" + dept + "_" + clas + "_" + sub).split())

			if key not in output.keys():
				output[key] = get_data_template()
			output[key]["rec_retail"] += i[1]["Price"]
			output[key]["rec_cost"] += i[1]["Cost"]
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
	def parse_ret(dname,output):
		df = pd.read_excel(dname, header = 20, skip_footer = 8)
		df2 = pd.concat([df.iloc[:,15],df["Price"]], axis = 1, keys = ["DCS", "Price"])
		df2.dropna(subset = ["DCS"], inplace = True)
		df2.reset_index(drop = True, inplace = True)
		for i in df2.iterrows():
			str_num = "050"
			dcs = i[1]["DCS"].split("  ")
			while len(dcs) < 3:
				dcs.append(" ")
			dept = dcs[0]
			clas = dcs[1]
			sub = dcs[2]
			key = "".join((str_num + "_" + dept + "_" + clas + "_" + sub).split())

			if key not in output.keys():
				output[key] = get_data_template()
			output[key]["venret"] += abs(i[1]["Price"])
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
	def parse_trans(dname,output):
		df = pd.read_excel(dname, header = 8, skip_footer = 1)
		df.dropna(axis = 1, how = "all", inplace = True)
		df.dropna(axis = 0, how = "all", inplace = True)
		for i in df.iterrows():
			str_num1 = str(int(i[1]["Out Store"])).ljust(2,'0')
			str_num1 = str_num1.rjust(3,'0')
			if str_num1 == "000":
				str_num1 = "900"
			str_num2 = str(int(i[1]["In Store"])).ljust(2,'0')
			str_num2 = str_num2.rjust(3,'0')
			if str_num2 == "000":
				str_num2 = "900"
			dcs = i[1]["Dept Name"].split("  ")
			while len(dcs) < 3:
				dcs.append(" ")
			dept = dcs[0]
			clas = dcs[1]
			sub = dcs[2]
			key1 = "".join((str_num1 + "_" + dept + "_" + clas + "_" + sub).split())
			key2 = "".join((str_num2 + "_" + dept + "_" + clas + "_" + sub).split())
			if key1 not in output.keys():
				output[key1] = get_data_template()
			if key2 not in output.keys():
				output[key2] = get_data_template()
			output[key1]["tfrout"] += i[1]["Ext Price"]
			output[key2]["tfrin"] += i[1]["Ext Price"]
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
	def parse_oo(dname,output):
		df = pd.read_excel(dname, header = 13, skip_footer = 6)
		df.dropna(axis = 1, how = "all", inplace = True)
		df.dropna(axis = 0, how = "all", inplace = True)
		d_m = data['data_month']
		d_y = data['data_year']
		if d_m + 1 > 12:
			d_m = 1
			d_y = d_y + 1
		else:
			d_m = d_m + 1
		currentdate = ''

		for i in df.iterrows():
			temp = "".join(str(i[1]["Item #"]).split())
			try:
				currentdate = datetime.strptime(temp,"%m/%d/%Y")
				continue
			except ValueError:
				flag = True

			if flag:
				str_num = "900"
				dcs = i[1]["DCS"].split("  ")
				while len(dcs) < 3:
					dcs.append(" ")
				dept = dcs[0]
				clas = dcs[1]
				sub = dcs[2]
				key = "".join((str_num + "_" + dept + "_" + clas + "_" + sub).split())
				o_c = "".join(i[1]["Ord C$"].split(","))
				if key not in output.keys():
					output[key] = get_data_template()
				if d_y > currentdate.year:
					output[key]["coo"][0] += float(o_c)
					output[key]['roo'][0] += i[1]["Due P$"]
				elif d_y == currentdate.year:
					diff = currentdate.month - d_m
					if diff <= 0:
						output[key]["coo"][0] += float(o_c)
						output[key]['roo'][0] += i[1]["Due P$"]
					else:
						output[key]["coo"][diff] += float(o_c)
						output[key]['roo'][diff] += i[1]["Due P$"]
				elif d_y < currentdate.year:
					diff = currentdate.month - d_m + 12
					output[key]["coo"][diff] += float(o_c)
					output[key]['roo'][diff] += i[1]["Due P$"]
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

	output1 = {}

	for f in data["files"]:
		if "po" in f.name.lower():
			parse_oo(f.name, output1)
		elif "trans" in f.name.lower():
			parse_trans(f.name, output1)
		elif "ret" in f.name.lower():
			parse_ret(f.name, output1)
		elif "rec" in f.name.lower():
			parse_rec(f.name, output1)
		elif "inv" in f.name.lower():
			parse_inv(f.name, output1)
		elif "sales" in f.name.lower():
			parse_sales(f.name, output1)

	return clean_output(output1)