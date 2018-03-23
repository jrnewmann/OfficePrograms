# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 11:40:14 2018

@author: justin
"""
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

with open('Percents.txt', 'r+') as f: #change file name to your needs
        lines = f.readlines()
        newlines = [float(x[:-3]) for x in lines] #change value in brackets to fit your data
        
sdr = round(np.std(newlines),2)
mean = round(np.average(newlines),2)
median = round(np.median(newlines),2)

bins = 20 #set number of bins for histogram

plt.figure(figsize=(10,8))
plt.hist(newlines,bins,color='#39B21E',edgecolor='grey',linewidth=0.2)
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

n = len(newlines)
plt.text(tx,ty,'n =',horizontalalignment = 'right')
plt.text(tx,ty,n)

x = np.arange(-1,101)
norm = mlab.normpdf(x,mean,sdr)

plt.plot(x,norm*100,color='Black')

plt.savefig('103Histogram.png')