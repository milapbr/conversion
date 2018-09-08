def convert(data):

    def check_file_type(f):
        if "rmsa" and "on order" in f.name.lower():
            return "oo"
        elif "rmsa" in f.name.lower():
            return "data"
        else:
            return "skip"

    def parse_data(f,output):
        try:
            book = xlrd.open_workbook(f.name)
            sh = book.sheet_by_index(0)
        except:
            raise ConversionError("Data not in Excel format.")
        # preassigning negative index so that it will be ignore
        index = {
            "sales_index" : -1,
            "inv_fom": -1,
            "inv_index" : -1,
            "mdown_index" : -1,
            "mup_index" : -1,
            "rec_cost_index" : -1,
            "rec_retail_index" : -1,
            "tfrin_index" : -1,
            "tfrout_index" : -1,
            "venret_index" : -1
        }

        # assigning index for each information so I do not have to match the key word every loop
        for col in range (sh.ncols):
            if "net sales" in sh.cell_value(0, col).lower():
                index["sales_index"] = col
            elif "ending inventory: price" in sh.cell_value(0,col).lower():
                index["inv_index"] = col
            elif "net markdowns" in sh.cell_value(0,col).lower():
                index["mdown_index"] = col
            elif "net markups" in sh.cell_value(0,col).lower():
                index["mup_index"] = col
            elif "purchasing: net received cost" in sh.cell_value(0, col).lower():
                index["rec_cost_index"] = col
            elif "purchasing: net received price" in sh.cell_value(0, col).lower():
                index["rec_retail_index"] = col
            elif "transfer in" in sh.cell_value(0, col).lower():
                index["tfrin_index"] = col
            elif "transfer out" in sh.cell_value(0, col).lower():
                index["tfrout_index"] = col
            elif "vender return" in sh.cell_value(0, col).lower():
                index["venret_index"] = col
        # end assigning

        for r in range (sh.nrows):
            if "Category" in sh.cell_value(r,0):
                continue
            key = "002__" + sh.cell_value(r,0)

            # if output has the key already, update the value, if not create the key and update the value
            if key not in output.keys():
                output[key] = get_data_template()
            for k, v in index.iteritems():
                if v > 0:
                    output[key].update({k.split("_index")[0]: int(round(sh.cell_value(r, v)))})
        return output

    def parse_oo(f,output):
        try:
            book = xlrd.open_workbook(f.name)
            sh = book.sheet_by_index(0)
        except:
            raise ConversionError ("Data not in Excel format.")
        # preassigning negative index so that it will be ignore

        for r in range (sh.nrows):
            if "Category" in sh.cell_value(r,0):
                continue
            key = "002__" + sh.cell_value(r,0)

            # if output has the key already, update the value, if not create the key and update the value
            if key not in output.keys():
                output[key] = get_data_template()
            coo = sh.row_values(r, start_colx = 1, end_colx = None)
            templist = sh.row_values(r, start_colx = 1, end_colx = None)
            coo = [int(round (n,0)) for n in templist]
            for i in range(12 - len(coo)):
                coo.append(0)
            output[key]["coo"] = coo

        return output

    output = {}
    for f in data['files']:
        file_type = check_file_type(f)
        if 'skip' in file_type:
            print "Imporper file name."
            continue
        if 'data' in file_type:
            output = parse_data(f, output)
        if 'oo' in file_type:
            output = parse_oo(f, output)

    return output
