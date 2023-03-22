# UTF-8形式
from pathlib import Path;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent));

import pandas as pd;

df = pd.read_csv("sample/test.csv");
print(df);
