from scipy.stats import norm;

scoreM = 60;
meanM = 50;
stdM = 5;

scoreE = 80;
meanE = 70;
stdE = 8;

cdfM = norm.cdf(x=scoreM, loc=meanM, scale=stdM);
print("数学の", scoreM, "点は、上から", (1-cdfM)*100,"%");

cdfE = norm.cdf(x=scoreE, loc=meanE, scale=stdE);
print("英語の",scoreE,"点は、上から", (1-cdfE)*100,"%");
