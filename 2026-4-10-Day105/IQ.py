from scipy.stats import norm

std = 15
scorelist = [110,130,148]
for score in scorelist:
    cdf = norm.cdf(x=score,loc=100,scale=std)
    print(score,1-cdf)
