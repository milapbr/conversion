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
	
