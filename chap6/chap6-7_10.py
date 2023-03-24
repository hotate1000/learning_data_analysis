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

sns.heatmap(df.corr(), annot=True, vmax=1, vmin=1, center=0);
plt.show();

sns.pairplot(data=df, kind="reg");
plt.show();
