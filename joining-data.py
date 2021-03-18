import pandas

def merge(left="C:\\Users\\brichardson\\Catalyte\\DataEngineering_ADT\\DataProcessingWithPython\\weather_csv\\concatenated.csv", 
    right="C:\\Users\\brichardson\\Catalyte\\DataEngineering_ADT\\DataProcessingWithPython\\weather_csv\\station-info.txt", 
    output="C:\\Users\\brichardson\\Catalyte\\DataEngineering_ADT\\DataProcessingWithPython\\weather_csv\\Concatenated-Merged.csv"):
    leftDf = pandas.read_csv(left)
    rightDf = pandas.read_fwf(right, converters={"USAF":str, "WBAN":str})   # 'fwf' is for fixed-width-file
    rightDf["USAF_WBAN"] = rightDf["USAF"] + "-" + rightDf["WBAN"]
    mergedDf = pandas.merge(leftDf, rightDf.loc[: , ["USAF_WBAN", "STATION NAME", "LAT", "LON"]], left_on="ID", right_on="USAF_WBAN")
    mergedDf.to_csv(output)

merge()