# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 23:24:02 2018

@author: zhenw
"""

import pandas as pd
import numpy as np
import sys

#load datasets and review data type
data=pd.read_table('data.txt',header=None,sep=',')

sys.stdout.write("Number of Rows of Data = " + str(data.shape[0]) + '\n')
sys.stdout.write("Number of Columns of Data = " + str(data.shape[1])+'\n\n')
sys.stdout.write("data type is \n")

print(data.dtypes.tail())

#statistics summuary
Col=data.iloc[:,0]
colMean=Col.mean()
colsd=Col.std()
sys.stdout.write("Mean = " + '\t' + str(colMean) + '\t\t' +
"Standard Deviation = " + '\t ' + str(colsd) + "\n")

#calculate quantile boundaries
ntiles = 4
percentBdry = []
for i in range(ntiles+1):
    percentBdry.append(np.percentile(Col, i*(100)/ntiles))
sys.stdout.write("\nBoundaries for 4 Equal Percentiles \n")
print(percentBdry)
sys.stdout.write(" \n")


#run again with 10 equal intervals
ntiles = 10
percentBdry = []
for i in range(ntiles+1):
    percentBdry.append(np.percentile(Col, i*(100)/ntiles))
sys.stdout.write("Boundaries for 10 Equal Percentiles \n")
print(percentBdry)
sys.stdout.write(" \n")

#The last column contains categorical variables
col = 60
colData = data.iloc[:,col]
unique = set(colData)
sys.stdout.write("Unique Label Values \n")
print(unique)
#count up the number of elements having each value
catDict = dict(zip(list(unique),range(len(unique))))
catCount = [0]*2
for elt in colData:
  catCount[catDict[elt]] += 1
sys.stdout.write("\nCounts for Each Value of Categorical Label \n")
print(list(unique))
print(catCount)

#qqplot
import pylab
import scipy.stats as stats
import matplotlib.pyplot as plt
stats.probplot(np.array(data.iloc[:,2]), dist="norm", plot=pylab)
pylab.show()


#using pandas to summarize data
#print head and tail of data frame
print(data.head())
print(data.tail())
#print summary of data frame
summary = data.describe()
print(summary)

#print line
for i in range(208):
   #assign color based on "M" or "R" labels
   if data.iloc[i,60] == "M":
      pcolor = "red"
   else:
      pcolor = "blue"
   #plot rows of data as if they were series data
   dataRow = data.iloc[i,0:60]
   dataRow.plot(color=pcolor)
plt.xlabel("Attribute Index")
plt.ylabel(("Attribute Values"))
plt.show()

#calculate correlations between real-valued attributes
dataRow2 = data.iloc[1,0:60]
dataRow3 = data.iloc[2,0:60]
plt.scatter(dataRow2, dataRow3)
plt.xlabel("2nd Attribute")
plt.ylabel(("3rd Attribute"))
plt.show()
dataRow21 = data.iloc[20,0:60]
plt.scatter(dataRow2, dataRow21)
plt.xlabel("2nd Attribute")
plt.ylabel(("21st Attribute"))
plt.show()

#change the targets to numeric values
target = []
for i in range(208):
#assign 0 or 1 target value based on "M" or "R" labels
   if data.iloc[i,60] == "M":
      target.append(1.0)
   else:
      target.append(0.0)
#plot 35th attribute
dataRow = data.iloc[0:208,35]
plt.scatter(dataRow, target)
plt.xlabel("Attribute Value")
plt.ylabel("Target Value")
plt.show()
#
#To improve the visualization, this version dithers the points a little
# and makes them somewhat transparent
import random
target = []
for i in range(208):
#assign 0 or 1 target value based on "M" or "R" labels
# and add some dither
   if data.iloc[i,60] == "M":
      target.append(1.0 + random.uniform(-0.1, 0.1))
   else:
      target.append(0.0 + random.uniform(-0.1, 0.1))
#plot 35th attribute with semi-opaque points
dataRow = data.iloc[0:208,35]
plt.scatter(dataRow, target, alpha=0.5, s=120)
plt.xlabel("Attribute Value")
plt.ylabel("Target Value")
plt.show()


#calculate correlations between real-valued attributes
dataRow2 = data.iloc[1,0:60]
dataRow3 = data.iloc[2,0:60]
dataRow21 = data.iloc[20,0:60]
mean2 = 0.0; mean3 = 0.0; mean21 = 0.0
numElt = len(dataRow2)
for i in range(numElt):
   mean2 += dataRow2[i]/numElt
   mean3 += dataRow3[i]/numElt
   mean21 += dataRow21[i]/numElt
var2 = 0.0; var3 = 0.0; var21 = 0.0
for i in range(numElt):
    var2 += (dataRow2[i] - mean2) * (dataRow2[i] - mean2)/numElt
    var3 += (dataRow3[i] - mean3) * (dataRow3[i] - mean3)/numElt
    var21 += (dataRow21[i] - mean21) * (dataRow21[i] - mean21)/numElt
corr23 = 0.0; corr221 = 0.0
for i in range(numElt):
    corr23 += (dataRow2[i] - mean2) * \
    (dataRow3[i] - mean3) / (np.sqrt(var2*var3) * numElt)
    corr221 += (dataRow2[i] - mean2) * \
    (dataRow21[i] - mean21) / (np.sqrt(var2*var21) * numElt)
sys.stdout.write("Correlation between attribute 2 and 3 \n")
print(corr23)
sys.stdout.write(" \n")
sys.stdout.write("Correlation between attribute 2 and 21 \n")
print(corr221)
sys.stdout.write(" \n")


#calculate correlations between real-valued attributes
corMat = pd.DataFrame(data.iloc[:,0:60].corr())
#visualize correlations using heatmap
plt.pcolor(corMat)
plt.title('corr heatmap')
plt.show()

print("My name is Zhen Wang")
print("My NetID is: zhenw3")
print("I hereby certify that I have read the University policy on Academic Integrity and that I am not in violation.")


   
   


