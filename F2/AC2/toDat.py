
def to_dat(output):
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
	cilent = "BU4"
	month = '04'
	year = "2018"
	
	filename = "{0}{1}{2}.DAT".format(cilent, month, year[2:])
	dat = open(filename, "w")
	dat.write("$$ARS{0}{1}{2}\r\n".format((" "*64), month, year[2:]))
	cil = "{:<6}".format(cilent)
	cust= "{:<4}".format(cilent)
	for k,v in output.iteritems():
		tag_list = k.split("_")
		st = "{:<5}".format(tag_list[0])
		dep = "{:<5}".format(tag_list[1])
		clas = "{:<5}".format(tag_list[2])
		sclas = "{:<5}".format(tag_list[3])
		
		#Add subclass here for the subclass
		for key, val in v.iteritems():
			transtype = dic[key]
			if val == 0:
				continue
			value = str(val) + (" " * (26 - len(str(val))))
			end_blank = str(sclas) + (" " * (30 - len(str(sclas))))  # subclass will goes in here
			if key == "coo" or key == "roo":
				for j in range(12):
					if j < 9:
						transtype_oo = transtype + "0" + str(j + 1)
					else:
						transtype_oo = transtype + str(j + 1)
					if val[j] == 0:
						continue
					value = str(val[j]) + (" " * (26 - len(str(val[j]))))
					dat.write("{0}{1}{2}{3}{4}{5}{6}{7}\r\n".format(cil, cust, dep, clas, st, transtype_oo, value, end_blank))
			else:
				dat.write("{0}{1}{2}{3}{4}{5}{6}{7}\r\n".format(cil, cust, dep, clas, st, transtype, value, end_blank))
	dat.write("$$RMSEND")
	
	dat.close()
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

