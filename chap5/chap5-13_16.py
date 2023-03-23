from scipy.stats import norm;

mean = 166.8;
std = 5.8;
value = 170.0;
per = 0.20;

cdf = norm.cdf(x=value, loc=mean, scale=std);
print(value, "は、下から", cdf*100, "%");
print("-----");

ppf = norm.ppf(q=per, loc=mean, scale=std);
print("下から", per*100, "%の値は、", ppf, "です。");
print("-----");
