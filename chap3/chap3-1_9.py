import pandas as pd;

data1 = {
    "Aクラス" : [82,89,93,85,76],
    "Bクラス" : [100,62,82,70,86]
}

df1 = pd.DataFrame(data1);
print(df1);
print("-----");

print("Aクラス =", df1["Aクラス"].mean());
print("Bクラス =", df1["Bクラス"].mean());
print("-----");

print(df1.mean());
print("-----");

data2 = {
    "予想価格" : [240,250,150,240,300,5000]
}
df2 = pd.DataFrame(data2);
print(df2);
print(df2.mean());
print("-----");

print(df2.median());
print("-----");

print(df2.mode());
print("-----");