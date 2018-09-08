

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

    def parse_sales(dname, output):
        df = pd.read_csv(dname)
        df.dropna(axis=0, how="all", inplace=True)

        for i in df.iterrows():
            clas = "".join(i[1]["RMSA Category"].split())
            dept = ""
            c_list = clas.split('-')
 
            try:
                c_list[0] = int(c_list[0])
                c_list[0] = str(c_list[0])
            except:
                continue

            if c_list[0] == "99":
                clas = "99"
                dept = c_list[1][0:1]
            elif c_list[0] == "304H":
                clas = "304"
            else:
                clas = c_list[0]
            key = "001_" + dept + "_" + clas
            if key not in output.keys():
                output[key] = get_data_template()
            output[key]["sales"] += i[1]["Total Sell"]
            output[key]["mdown"] += i[1]["Total Discount"]

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

    def parse_oo(dname, output):
        df = pd.read_csv(dname)
        df.dropna(axis=0, how="all", inplace=True)
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
            key = "001_" + dept + "_" + clas
            if key not in output.keys():
                output[key] = get_data_template()
            if "f18" in dname.lower():
                output[key]["coo"][2] += i[1][" Total Cost"]
                output[key]["roo"][2] += i[1][" Total Sell"]
            else:
                output[key]["coo"][0] += i[1][" Total Cost"]
                output[key]["roo"][0] += i[1][" Total Sell"]

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

    def parse_rec(dname, output):
        df = pd.read_csv(dname, header=3)
        df.dropna(axis=0, how="all", inplace=True)
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
            key = "001_" + dept + "_" + clas
            if key not in output.keys():
                output[key] = get_data_template()
            output[key]["rec_retail"] += i[1]["Sum of Total Sell"]
            output[key]["rec_cost"] += i[1]["Total Cost"]

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

    def parse_inv(dname, output):
        df = pd.read_csv(dname, header=3)
        df.dropna(axis=0, how="all", inplace=True)
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
            key = "001_" + dept + "_" + clas
            if key not in output.keys():
                output[key] = get_data_template()
            output[key]["inv"] += i[1][" Total Sell"]

    def parse_vend(dname,output):
        df = pd.read_csv(dname, header = 1)
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
            key = "001_" + dept + "_" + clas
            if key not in output.keys():
                output[key] = get_data_template()
            output[key]["venret"] += i[1]["Sum of Total Sell"]
        print output
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

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
        elif "vendor" in f.name.lower():
            parse_vend(f.name, output)

    return clean_output(output)