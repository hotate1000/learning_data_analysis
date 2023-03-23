import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;

sns.set(font=["Meiryo", "Yu Gothic", "Hiragino Maru Gothic Pro"]);

data1 = {
    "A案" : [1,10,1,10,1,10,1,10],
    "B案" : [5,5,5,5,6,6,6,6],
    "C案" : [1,2,3,4,5,6,7,8]
}
df = pd.DataFrame(data1);
print(df);

bins = [1,3,5,7,9,11];
df.plot.hist(bins=bins);
plt.title("ケーキの感想はどのように違うか？");
plt.show();
