import sys

import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QApplication
from spyder.widgets.variableexplorer.dataframeeditor import DataFrameEditor

df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6]]), columns=['a', 'b', 'c'])
print(df)

app = QApplication([])
editor = DataFrameEditor(None)
editor.setup_and_check(df)
editor.show()

sys.exit(app.exec_())