from scipy.stats import norm

mean = 166.8
std = 5.8
value = 0.20

cdf = norm.ppf(q=value,loc=mean,scale=std)
print(value,"は下から",cdf*100,"%")
