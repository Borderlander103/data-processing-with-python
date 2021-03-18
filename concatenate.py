import os
import glob
import pandas

def concatenate(indir = "Income-By-State", outfile = "IncomeByStateByYear.csv"):
    os.chdir(indir)
    fileList = glob.glob("*.xls")  # stores files in a list
    dfList = []
    # colnames = ["Year", "Month", "Day", "Hour", "Temp", "DewTemp", "Pressure", "WindDir", "WindSpeed", "Sky", "Precip1", "Precip6", "ID"]
    for filename in fileList:
        print(filename)
        df = pandas.read_excel(filename, header=3)
        dfList.append(df)
    concatDF = pandas.concat(dfList, axis = 1)
    # concatDF.columns = colnames
    concatDF.to_csv(outfile, index=None)

concatenate()