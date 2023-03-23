import pandas as pd;

import matplotlib.pyplot as plt;
import seaborn as sns; 

data1 = {
    "ID" : [0,1,2,3,4,5,6,7,8,9],
    "A" : [59,24,62,48,58,19,32,88,47,63],
    "B" : [49,50,49,54,45,52,56,48,45,52]
}

df = pd.DataFrame(data1);
meanA = df["A"].mean();
stdA = df["A"].std();
meanB = df["B"].mean();
stdB = df["B"].std();
print(meanA);
print(meanB);
print(stdA);
print(stdB);
print("-----");

sns.set(font=["Meiryo", "Yu Gothic", "Hiragino Maru Gothic Pro"]);
df.plot.scatter(x="ID", y="A", color="b", ylim=(0,100));
plt.axhline(y=50, c="Magenta");
plt.title("Aのばらつき：大きい", fontsize=24);
plt.show();
print("-----");

df.plot.scatter(x="ID", y="B", color="b", ylim=(0,100));
plt.axhline(y=50, c="Magenta");
plt.title("Bのばらつき：小さい", fontsize=24);
plt.show();
print("-----");

print(df.var());
print("-----");

print(df.std());
print("-----");

bins=[10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100];

df["A"].plot.hist(bins=bins, color="c", ylim=(0.6));
plt.axvline(x=meanA, color="magenta");
plt.axvline(x=meanA-stdA, color="blue", linestyle="--");
plt.axvline(x=meanA+stdA, color="red", linestyle="--");
plt.title("Aのばらつき：大きい");
plt.show();
print("-----");

df["B"].plot.hist(bins=bins, color="c", ylim=(0,6));
plt.axvline(x=meanB, color="magenta");
plt.axvline(x=meanB-stdB, color="blue", linestyle="--");
plt.axvline(x=meanB+stdB, color="red", linestyle="--");
plt.title("Bのばらつき：小さい");
plt.show();
print("-----");
