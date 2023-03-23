from scipy.stats import norm;

scorelist = [60, 70, 80];

for score in scorelist:
    cdf = norm.cdf(x=score, loc=50, scale=10);
    print("偏差値", score, "は、上から", (1-cdf)*100, "%");
print("-----");

perlist = [0.1586, 0.02275, 0.00134];
for per in perlist:
    ppf = norm.ppf(q=(1-per), loc=50, scale=10);
    print("上から", per * 100, "%以上に入るには、偏差値", ppf, "以上が必要");
print("-----");
