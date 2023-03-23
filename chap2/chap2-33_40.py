import pandas as pd;

data = [
    [10, 30, 40],
    [20, 30, 40],
    [20, 30, 40],
    [30, 30, 50],
    [20, 30, 40]
];

dfA = pd.DataFrame(data);
print(dfA);
print("-----");

print(dfA.duplicated().value_counts());
print("-----");

dfB = dfA.drop_duplicates();
print(dfB);
print("-----");

data2 = {
    "A" : ["100", "300"],
    "B" : ["500", "1,500"]
};
dfC = pd.DataFrame(data2);
print(dfC);
print("-----");

print(dfC.dtypes);
print("-----");

dfC["A"] = dfC["A"].astype(int);
print(dfC.dtypes);
print("-----");

dfC["B"] = dfC["B"].str.replace(",","").astype(int);
print(dfC.dtypes);
print(dfC);
