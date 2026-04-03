from scipy.stats import norm

mean = 166.8
std = 5.8
value = 160.0

cdf = norm.cdf(x=value,loc=mean,scale=std)
print(value,"は下から",cdf*100,"%")
