import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;

sns.set(font=["Yu Gothic", "Hiragino Maru Gothic Pro"]);

data = {
    "数学" : [100,85,90,95,80,80,75,65,65,60,55,45,45],
    "理科" : [94, 90,95,90,85,80,75,70,60,60,50,50,48],
    "社会" : [80, 88,70,62,86,70,79,65,75,67,75,68,60]
}

df = pd.DataFrame(data);
print(df.head());
print("-----");

df.plot.scatter(x="数学", y="理科", c="b");
plt.title("数学と理科の関係性");
plt.show();

df.plot.scatter(x="数学", y="社会", c="b");
plt.title("数学と社会の関係性");
plt.show();
print("-----"):

print("数学と理科=", df.corr()["数学"]["理科"]);
print("数学と社会=", df.corr()["数学"]["社会"]);
print("-----");

print(df.corr());
print("-----");

sns.regplot(data=df, x="数学", y="理科", line_kws={"color":"red"});
plt.show();
sns.regplot(data=df, x="数学", y="社会", line_kws={"color":"red"});
plt.show();
print("-----");

sns.jointplot(data=df, x="数学", y="理科", kind="reg", line_kws={"color":"red"});
plt.show();
sns.jointplot(data=df, x="数学", y="社会", kind="reg", line_kws={"color":"red"});
plt.show();
print("-----");

