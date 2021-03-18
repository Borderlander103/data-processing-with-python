import pandas
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))


leftDf = pandas.read_csv("IncomeByStateByYearNoDupl.csv")
rightDf = pandas.read_csv("Geoids and states.csv")
# rightDf["State"] = rightDf["GEOID"] + "-" + rightDf["WBAN"]
mergedDf = pandas.merge(leftDf, rightDf, left_on="GEOID", right_on="GEOID")
mergedDf.set_index(["GEOID", "State"], inplace=True)
mergedDf.to_csv("IncomeByState.csv")