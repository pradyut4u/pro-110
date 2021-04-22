import pandas as pd
import csv
import plotly.figure_factory as pff
import statistics
import random

df = pd.read_csv(r"D:/python/py/pro-110.csv")
fig = pff.create_distplot([df["claps"].tolist()],["Claps"],show_hist=False)
fig.show()

Claplist = df["claps"].tolist()

pmean = statistics.mean(Claplist)
psd = statistics.stdev(Claplist)

print(pmean)
print(psd)

def samplespace():

    newlist = []

    for i in range(0,30):
        q = Claplist[random.randint(0,len(Claplist) - 1)]
        newlist.append(q)

    smean = statistics.mean(newlist)
    return(smean)
    print(smean)

def repeat():
    newlist2 = []

    for w in range(0,100):
        e = samplespace()
        newlist2.append(e)

    dig = pff.create_distplot([newlist2],["Mean"])
    dig.show()

    n2mean = statistics.mean(newlist2)
    n2sd = statistics.stdev(newlist2)
    print(n2mean)
    print(n2sd)

r = repeat()