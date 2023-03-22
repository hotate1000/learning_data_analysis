from pathlib import Path;
import sys;
sys.path.append(str(Path(__file__).resolve().parent.parent));

import pandas as pd;

dfA = pd.read_csv("sample/test.csv", index_col=0);
# 空のデータフレームを作成する
dfB = pd.DataFrame();
dfB = dfA["国語"];
print(dfB);
print("-----");

dfC = pd.DataFrame();
dfC = dfC.append(dfA.iloc[0]);
print(dfC);
print("-----");

dfD = pd.read_csv("sample/test.csv", index_col=0);
dfD = dfD.drop("国語", axis=1);
print(dfD);
print("-----");

dfE = pd.read_csv("sample/test.csv", index_col=0);
dfE = dfE.drop(dfE.index[3]);
print(dfE);
print("-----");

dfF = pd.read_csv("sample/test.csv", index_col=0);
print(dfF["国語"] > 80);
print("-----");
print(dfF[dfF["国語"] > 80]);
print("-----");
print(dfF[(dfF["国語"] > 80) & (dfF["数学"] > 80)]);
print("-----");
