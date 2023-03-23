import pandas as pd;

data1 = {
    "A案" : [1,10,1,10,1,10,1,10],
    "B案" : [5,5,5,5,6,6,6,6],
    "C案" : [1,2,3,4,7,8,9,10]
}

df1 = pd.DataFrame(data1);
print(df1);
print("-----");

bins = [1,3,5,7,9,11];
cutA = pd.cut(df1["A案"], bins=bins, right=False);
cutA_change = cutA.value_counts(sort=False);
print(cutA_change);
print("-----");

cutB = pd.cut(df1["B案"], bins=bins, right=False);
cutB_change = cutB.value_counts(sort=False);
print(cutB_change);
print("-----");

cutC = pd.cut(df1["C案"], bins=bins, right=False);
cutC_change = cutC.value_counts(sort=False);
print(cutC_change);
print("-----");
