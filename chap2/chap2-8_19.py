from pathlib import Path;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent));

import pandas as pd;

# df = pd.read_csv("sample/testNoHeader.csv", index_col=0, header=None);
df = pd.read_csv("sample/test.csv", index_col=0);
print(df);
print("-----");

print(df.columns);
print(df.index);
print("-----");

list1 = [i for i in df.columns];
print(list1);
list2 = [i for i in df.index];
print(list2);
print("-----");

print(df.dtypes);
print("-----");

print(len(df));
print("-----");

print(df["国語"]);
print("-----");

print(df.iloc[0]);
print("-----");

print(df["国語"][0]);
print("-----");
