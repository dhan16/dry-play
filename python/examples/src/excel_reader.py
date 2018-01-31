import os
import pandas as pd

if __name__ == '__main__':
    infile = os.path.expanduser('~/Downloads/excel.xlsx')
    numsheets = 7
    for sheetno in range(numsheets):
        df = pd.read_excel(infile, sheetno)
        print(df)

