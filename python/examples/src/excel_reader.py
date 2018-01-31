import os
import pandas as pd

if __name__ == '__main__':
    infile = os.path.expanduser('~/Downloads/excel.xlsx')
    sheetno = 0
    df = pd.read_excel(infile, sheetno)
    cols = list(df.columns.values)
    col0 = cols[0]
    col1 = cols[1]
    for index, row in df.iterrows():
        print("'{}': '{}',".format(row[col0], row[col1]))
