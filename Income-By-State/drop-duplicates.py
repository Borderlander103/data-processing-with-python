from os.path import realpath
import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

df = pd.read_csv("IncomeByStateByYear.csv")
deduped = df.T.drop_duplicates().T
deduped.to_csv("IncomeByStateByYearNoDupl.csv", index=0)