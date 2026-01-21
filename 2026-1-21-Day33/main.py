import random 

s = ["私","君"]
p = ["が","は","を"]
o = ["リンゴ","サッカー"]
v = ["好き","する"]


subject = random.choice(s)
particle = random.choices(p,weights=[0.5,0.5,0])[0]
particle_2 = random.choice(p)
object = random.choice(o)
verb = random.choices(v,weights=[0.8,0.2])[0]

if particle == "が":
    object = "サッカー"
    particle_2 = "を"
    verb = "する"
if particle == "は":
    object = random.choice(o)
    if object == "リンゴ":
        particle_2 = "が"
        verb = "好き"
    elif object == "サッカー":
        particle_2  = random.choices(p,weights=[0.5,0,0.5])[0]
        if particle_2 == "を":
            verb = "する"
        elif particle_2 == "が":
            verb = "好き"



    



print(subject,particle,object,particle_2,verb)
