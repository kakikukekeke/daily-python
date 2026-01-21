import random 

s = ["私","君"]
p = ["が","は","を"]
o = ["リンゴ","サッカー"]
v = ["好き","する"]


subject = random.choice(s)
particle = random.choice(p)
particle_2 = random.choice(p)
object = random.choice(o)
verb = random.choice(v)

if object ==  "リンゴ":
    verb = random.choices(v,weights=[0.8,0.2])[0]

if object == "サッカー":
    particle_2 = random.choices(v,weights=[0.1,0.1,0.8])[0]
    verb = random.choices(v,weights=[0.2,0.8])[0]

print(subject,particle,object,particle_2,verb)
