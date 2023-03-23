import random;
import pandas as pd;
import matplotlib.pyplot as plt;
import seaborn as sns;

sns.set(font=["Meiryo", "Yu Gothic", "Hiragino Maru Gothic Pro"]);

def galton(steps, count):
    ans = [];
    for i in range(count):
        val = 50;
        for j in range(steps):
            val -= random.randrange(-1,2,2)
        ans.append(val);
    df = pd.DataFrame(ans);
    df[0].plot.hist();
    plt.title(str(steps) + "段：" + str(count) + "個");
    plt.ylabel("");
    plt.show();

galton(10, 10000);

