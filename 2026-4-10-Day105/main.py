from scipy.stats import norm

scorelist = [60,70,80]
for score in scorelist:
    cdf = norm.cdf(x=score,loc=50,scale=10)
    print("偏差値",score,"は上から",(1-cdf)*100,"%")
