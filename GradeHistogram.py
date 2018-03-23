# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 10:47:10 2018

@author: jrnewmann
"""
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np
import csv

# Class name
class_name = 'Example Class'
# Input file name
input_file_name = 'ncol_test_data.csv'
# Read CSV and just save percentages
percentages = []
with open(input_file_name, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    count = 0
    for row in spamreader:
        if count == 0:
            #read header to find % col index
            col = row.index("Course total (Percentage)") 
        if count > 0:
            # col is the one that has above percentages
            percentages.append(float(row[col].strip(' %')))
        count += 1
print('Percentages are: \n{}'.format(percentages))

# with open('Percents.txt', 'r+') as f: #change file name to your needs
#         lines = f.readlines()
#         newlines = [float(x[:-3]) for x in lines] #change value in brackets to fit your data

sdr = round(np.std(percentages),2)
mean = round(np.average(percentages),2)
median = round(np.median(percentages),2)
print('Standard error={0}, Mean={1}, Median={2}'.format(sdr, mean, median))

bins = 40 #set number of bins for histogram

plt.figure(figsize=(10,8))
plt.hist(percentages,bins,color='#39B21E',edgecolor='grey',linewidth=0.2)
plt.xlabel('Grade (%)')
plt.ylabel('Freq')
plt.title('Earth 103 Grade Histogram')
plt.xlim(0,100)
plt.ylim(0,6) #adjust ylim to your data

tx = 20 #set x location of statistics text
ty = 1  #set y location of stats
ti = 0.5 #set interval between text

plt.text(tx,ty+4*ti,'Std Dev =',horizontalalignment = 'right')
plt.text(tx,ty+4*ti,sdr)

plt.text(tx,ty+3*ti,'Median =',horizontalalignment = 'right')
plt.text(tx,ty+3*ti,median)

plt.text(tx,ty+2*ti,'Mean =',horizontalalignment = 'right')
plt.text(tx,ty+2*ti,mean)

plt.text(tx,ty+ti,'Bins =',horizontalalignment = 'right')
plt.text(tx,ty+ti,bins)

n = len(percentages)
plt.text(tx,ty,'n =',horizontalalignment = 'right')
plt.text(tx,ty,n)

x = np.arange(-1,101)
norm = mlab.normpdf(x,mean,sdr)

plt.plot(x,norm*100,color='Black')

plt.savefig('103Histogram.png')
