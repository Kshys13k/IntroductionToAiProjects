from ID3 import ID3
import pandas as pd
import numpy as np

df=pd.read_csv("smallDataSet.csv", header=None)

df=df.rename(columns={0:"class",1:"pogoda", 2:"wiatr", 3:"pora"})
trainingDataDf=df.iloc[:-2,:]
dataClassT=trainingDataDf.iloc[:,0:1]
dataT=trainingDataDf.iloc[:,1:]
data=df.iloc[:,1:]

id3=ID3()
id3.train(dataT,dataClassT)
ans=id3.predict(data)
print(ans)
# df=pd.concat([data,dataClass], axis=1)
#
# uniqueValues=["no-recurrence-events","recurrence-events"]
# r=ID3.calcInfoGain("age",df,uniqueValues)
# print(r)
