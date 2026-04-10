from scipy.stats import norm

scorelist = [0.1586,0.02265,0.00134]
for score in scorelist:
    cdf = norm.cdf(x=score,loc=50,scale=10)
    print("上から",score * 100,"％入るには、偏差値",cdf,"以上必要")
