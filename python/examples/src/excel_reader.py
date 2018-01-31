import os
import pandas as pd

if __name__ == '__main__':
    infile = os.path.expanduser('~/Downloads/excel.xlsx')
    sheetno = 1
    df = pd.read_excel(infile, sheetno)
    cols = list(df.columns.values)
    col0 = cols[0]
    col1 = cols[1]
    for index, row in df.iterrows():
        val0 = row[col0].strip()
        val1 = row[col1].strip().replace('\n', ' ').strip()
        val0 = val0.replace('(not E300)', '').strip()
        if val0.endswith('(I,J,K)'):
            val0 = val0.replace('(I,J,K)', '').strip()
            for dir in ['I', 'J', 'K']:
                print("'{}{}': '{} ({})',".format(val0, dir, val1, dir))
        else:

            print("'{}': '{}',".format(val0, val1))
