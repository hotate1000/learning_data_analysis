import pandas as pd;

data = {
    "国語" : [90,50,None,40],
    "数学" : [80,None,None,50]
}
idx = ["A太","B介","C子","D部"];
dfA = pd.DataFrame(data, index=idx);
print(dfA);
print("-----");

print(dfA.isnull());
print(dfA.isnull().sum());
print("-----");

dfB = pd.DataFrame(data, index=idx);
dfB = dfB.dropna();
print(dfB);
print("-----");

dfC = pd.DataFrame(data, index=idx);
dfC = dfC.dropna(subset=["国語"]);
print(dfC);
print("-----");

dfD = dfA.fillna(dfA.mean());
print(dfD);
print("-----");

dfE = dfA.fillna(method="ffill");
print(dfE);
print("-----");