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

	def make_mup_dict(df):
		marg = {}
		df = pd.DataFrame(df[['Class', '%']])
		df = df.apply(pd.to_numeric, errors='ignore')
		for i in df.iterrows():
			key = i[1][0].replace('\'', '')
			val = i[1][1]
			marg[key] = val
		data["cache"].store_data(marg)
		return marg

	def parse_sales(name,output):
		df = pd.read_table(name, header = 0)
		df.dropna(axis = 1, inplace = True, how = "all")
		df = df.astype(str)
		for i in df.iterrows():
			clas = i[1]["Class.1"]
			if clas.startswith("Clearance"):
				clas = "Clearance"
			elif clas == "$1,$3 Rack":
				continue
			key = "001__" + clas
			if key not in output.keys():
				output[key] = get_data_template()
			output[key]["sales"] += float("".join(i[1]["Total Sell"].split(",")))
			output[key]["mdown"] += float("".join(i[1]["Total Discount"].split(",")))
#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

	def parse_inv(name,output):
		df = pd.read_table(name, header = 0)
		df.dropna(axis = 1, inplace = True, how = "all")
		df.dropna(subset = ["Class.1"], inplace = True)
		for i in df.iterrows():
			clas = i[1]["Class.1"]
			if clas.startswith("Clearance"):
				clas = "Clearance"
			elif clas == "$1,$3 Rack":
				continue
			key = "001__" + clas
			if key not in output.keys():
				output[key] = get_data_template()
			output[key]["inv"] += float("".join(i[1]["Total Sell"].split(",")))


#-----------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------

	def parse_rec(name, output, marg):
		rec_dict = {"5,10,15 Racks": ["$5 Rack", "$10 Rack", "$15 Rack"],
					"Underwear":["Camisoles", "Bra Accesories", "Bralettes",],
					"Tops": ["Bandeaus", "Plus Size Tops"],
					"Accessories" : ["Head Wear", "Watches", "Brooches", "Sunglasses"],
					"Leggings" : ["Light Weight Leggings", "Fleece Leggings", "Capri Leggings", "Boot Cuffs"],
					"Home and Gift" : ["Face", "Stationary"],
					"Dress": ["Pageant and Prom Dresses"]
					}
		ign_list = ["Non-Charitable Donations","Damaged Inventory", "Birthday Discount", "Tax Adjustments",
					"Online Shipping","Giveaways", "Donations", "Charity Tee Shirt", "Punchcard",
					"Personal Inventory", "Perkville Discounts", "$10 Promo Giftcard", "Charitable Donations",
					"$1,$3 Rack"]

		df = pd.read_table(name, header = 0)
		df = df.loc[df["ID"].str.startswith("PO-")]
		df = df.astype(str)
		for i in df.iterrows():
			clas = i[1]["Class"]
			if clas.startswith("Clearance"):
				clas = "Clearance"
			elif clas in ign_list:
				continue
			key = "001__" + clas
			if key not in output.keys():
				output[key] = get_data_template()
			try:
				markup = marg[clas]
			except KeyError:
				for k,v in rec_dict.iteritems():
					if any(val == clas.strip() for val in v):
						clas = k
				markup = marg[clas]

			cost = float("".join(i[1]["Total Value"].split(",")))
			retail = cost/(1-markup)
			output[key]["rec_cost"] += cost
			output[key]["rec_retail"] += retail
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------
			
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

	for f in data["files"]:
		if "sales report" in f.name.lower():
			parse_sales(f.name,output)
		elif "inventory history" in f.name.lower():
			parse_rec(f.name, output, markup_data)
		elif "inventory on hand" in f.name.lower():
			parse_inv(f.name, output)
		elif "margin" in f.name.lower():
			pass

	return clean_output(output)