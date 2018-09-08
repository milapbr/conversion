class file:
	name = ""
	
	def __init__(self, name):
		self.name = name
		
class cache:
	dic = None
	def store_data(self,dic):
		self.dic = dic
	def get_data():
		return dic
		
data = {"files":[file("C:\Users\WSio\Desktop\RMSA Cilent\CC7\\042018\companion's margin.xlsx"),
		file("C:\Users\WSio\Desktop\RMSA Cilent\CC7\\042018\Department Sales Summary 4-2018.xlsx"),
		file("C:\Users\WSio\Desktop\RMSA Cilent\CC7\\042018\Inventory Summary 4-2018.xlsx"),
		file("C:\Users\WSio\Desktop\RMSA Cilent\CC7\\042018\On Order Summary 4-2018.xlsx"),
		file("C:\Users\WSio\Desktop\RMSA Cilent\CC7\\042018\Receiving Summary 4-2018.xlsx")
		#file("/home/william/shareWin/Project/CC7/sales & inventory  - UCM12.01.17.xlsx")
		],
		"data_through" :0,
		"data_year" :2018,
		"data_month" :4,
		"cache":cache(),
		"client":"CC7"
		}


#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------
		
def sum(dic):
	total = {"sales":0, 
			"mdown":0, 
			"mup":0, 
			"inv":0, 
			"inv_fom":0, 
			"rec_retail":0, 
			"rec_cost":0, 
			"tfrin":0, 
			"venret":0,
			"tfrout":0, 
			"roo":[0,0,0,0,0,0,0,0,0,0,0,0], 
			"coo":[0,0,0,0,0,0,0,0,0,0,0,0]
			}
	for k, v in dic.iteritems():
		for key, val in v.iteritems():
			if key == "roo" or key == "coo":
				for j in range(12):
					total[key][j] += val[j]
			else:
				total[key] += val

	return total
	
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

def to_dat(output):
	import Mapping_table
	dic = {"sales":"SAL", 
			"mdown":"MKD", 
			"mup":"AMK", 
			"inv":"EOM", 
			"inv_fom":"CIN", 
			"rec_retail":"RCR", 
			"rec_cost":"RCC", 
			"tfrin":"TIN", 
			"tfrout":"TOU", 
			"roo":"R", 
			"coo":"C",
			"venret":"CBR"
			}
				
	cilent = (data["client"])
	month = "0" + str(data["data_month"])
	year = str(data["data_year"])[3:]

	filename = "{0}{1}{2}.DAT".format(cilent, month, year)
	dat = open(filename, "w")
	dat.write("$$ARS{0}{1}{2}\r\n".format((" "*64), month, year))
	cil = cilent + "   "
	customer = cilent + " "
	for k,v in output.iteritems():
		tag_list = k.split("_")
		st = tag_list[0] + (" " * 2)
		dep = tag_list[1] + (" " * 3)
		if dep.strip() == "":
			dep = (" " * 5)
		clas = Mapping_table.map_table[tag_list[2]] + (" " * 3)
		#Add subclass here for the subclass
		for key, val in v.iteritems():
			transtype = dic[key]
			value = str(val) + (" " * (20 - len(str(val))))
			end_blank = " " * 30  # subclass will goes in here
			if key == "coo" or key == "roo":
				for j in range(12):
					if j < 10:
						transtype_oo = transtype + "0" + str(j + 1)
					else:
						transtype_oo = transtype + str(j + 1)
					value = str(val[j]) + (" " * (20 - len(str(val[j]))))
					dat.write("{0}{1}{2}{3}{4}{5}{6}{7}\r\n".format(cil, customer, dep, clas, st, transtype_oo, value, end_blank))
			else:
				dat.write("{0}{1}{2}{3}{4}{5}{6}{7}\r\n".format(cil, customer, dep, clas, st, transtype, value, end_blank))
	dat.write("$$RMSEND")
	
	dat.close()
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

def convert(data):
	import pandas as pd
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

	def make_mup_dict(df):
		marg = {}
		df = pd.DataFrame(df[['Department', 'margin%']])
		df = df.apply(pd.to_numeric, errors='ignore')
		for i in df.iterrows():
			key = i[1][0].replace('\'', '')
			val = i[1][1]
			marg[key] = val
		data["cache"].store_data(marg)
		return marg

	def parse_sales(df, output):
		df = pd.concat([df.iloc[:, 0:1], df[['Ext Price', 'Ext Discount']]], axis=1)
		#df = df.apply(pd.to_numeric, errors='ignore')
		for i in df.iterrows():
			key = '001__' + i[1][0].replace('\'', '')
			if key not in output.keys():
				output[key] = get_data_template()
			output[key]["sales"] += int(round(i[1][1]))
			output[key]["mdown"] += int(round(i[1][2]))

	def parse_oo(df, output):
		df = pd.concat([df.iloc[:, 0:1], df[["Cancel Date", "Ship Date", "Ext Price Due", "Ext Cost Due"]]], axis=1)
		df = df.apply(pd.to_numeric, errors='ignore')
		d_m = data['data_month']
		d_y = data['data_year']
		if d_m + 1 > 12:
			d_m = 1
			d_y = d_y + 1
		else:
			d_m = d_m + 1
		for i in df.iterrows():
			key = '001__' + i[1][0].replace('\'', '')
			if key not in output.keys():
				output[key] = get_data_template()
			if str(i[1][1]) != 'NaT' and str(i[1][1]) != 'nan':
				currentdate = i[1][1]
			else:
				currentdate = i[1][2]
			if d_y > currentdate.year:
				output[key]["coo"][0] += int(round(i[1][4]))
				output[key]['roo'][0] += int(round(i[1][3]))
			elif d_y == currentdate.year:
				diff = currentdate.month - d_m
				if diff <= 0:
					output[key]["coo"][0] += int(round(i[1][4]))
					output[key]['roo'][0] += int(round(i[1][3]))
				else:
					output[key]["coo"][diff] += int(round(i[1][4]))
					output[key]['roo'][diff] += int(round(i[1][3]))
			elif d_y < currentdate.year:
				diff = currentdate.month - d_m + 12
				output[key]["coo"][diff] += int(round(i[1][4]))
				output[key]['roo'][diff] += int(round(i[1][3]))
		del df

	def parse_inv(df, output):
		df = pd.concat([df.iloc[:, 0:1], df["Inventory__Ext Price"]], axis=1)
		df = df.apply(pd.to_numeric, errors='ignore')
		for i in df.iterrows():
			key = '001__' + i[1][0].replace('\'', '')
			if key not in output.keys():
				output[key] = get_data_template()
			output[key]["inv"] += int(round(i[1][1]))
		del df

	def parse_rec(df, output,marg_data):
		df = pd.concat([df.iloc[:, 0:1], df["Ext Cost"]], axis=1)
		df = df.apply(pd.to_numeric, errors='ignore')
		for i in df.iterrows():
			key = '001__' + i[1][0].replace('\'', '')
			if key not in output.keys():
				output[key] = get_data_template()
			output[key]["rec_cost"] += int(round(i[1][1]))
			if key.strip("001__") in marg_data.keys():
				output[key]["rec_retail"] += int(round((i[1][1])/(1 - marg_data[key.strip("001__")])))
		del df

	def data_type(data_name, x, output, mkup): #check the date to see if it is oo or data
		if 'sales' in data_name:
			parse_sales(x, output)
		elif 'on order' in data_name:
			parse_oo(x, output)
		elif 'inventory' in data_name:
			parse_inv(x, output)
		elif 'receiving' in data_name:
			parse_rec(x, output, mkup)

	output = {}
	markup_file = False
	for f in data["files"]:
		if 'margin' in f.name.lower():
			markup_file = f

	if markup_file:
		x = pd.read_excel(markup_file.name)
		markup_data =  make_mup_dict(x)
	elif data["cache"].get_data():
		markup_data = data["cache"].get_data()
	else:
		raise ConversionError("No markups are available")

	# Setting up the table
	for f in data["files"]:
		if 'margin' in f.name:
			x = pd.read_excel(f.name)
			make_mup_dict(x)
			break
	for f in data["files"]:
		if 'margin' in f.name:
			continue
		else:
			x = pd.read_excel(f.name, skiprows=3)  # Trim the first 3 rows cos they will mess the data up
			x = x.dropna(axis=1, how="all")  # Take out the empty columns
			x = x.reset_index(drop='True')  # Reset index so it is easier to continue trimming
			x.columns = [i for i in range(x.shape[1])]  # Reset Column index for trimming
			col_name = []

			if x[x[0] == 'Department'].empty:
				ind = x[x[0] == 'Dept Name'].index.values[0]  # Get the index of where the headers at
			elif x[x[0] == 'Dept Name'].empty:
				ind = x[x[0] == 'Department'].index.values[0]  # Get the index of where the headers at
			# This loop is to get the all the headers into the list col_name
			# If the row above the headers are not NaN, I will combine that row with column because it will needed
			for i in range(len(x.columns)):
				if pd.notnull(x.iloc[ind - 1][i]):
					col_name.append(str(x.iloc[ind - 1][i]) + "__" + str(x.iloc[ind][i]))
				else:
					col_name.append(str(x.iloc[ind][i]))
			x.columns = col_name  # Set the columns name to col_name, which are the headers
			x = x[x.iloc[:,0].notnull()]  # take out the NaN in Department

			x = x.iloc[1:(x.shape[0]),:]  # trim headers row cos headers has already been set to Column name.
			x = x.reset_index(drop="True")  # Reset index again to make it looks good

		data_type(f.name.lower(), x, output,markup_data)

	return output

a = convert(data)
print sum(a)
