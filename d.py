import pandas as pd


a=pd.read_csv("nba.csv")
#not including count of nones
way1=a["Salary"].mean()
print(way1)

#way2 including count of nones

b=a["Salary"]
counter=0
while counter<459:
    for i in b:
        i+=i
        counter += 1

        break


print(i/457)















print(a)