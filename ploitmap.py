# _*_ coding: utf-8 _*_
"""
date: '2019/7/19 10:59'
....................................

"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def plotpic(datamat,labels):
    #print(datamat)
    #print(type(labels[1]))
    #print(labels)
    type1x=[]
    type1y=[]
    type2x=[]
    type2y=[]
    type3x = []
    type3y = []
    fig=plt.figure()
    for i in range(len(labels)):
        if labels[i]==1:
            type1x.append(datamat[i][0])#[i][1]
            type1y.append(datamat[i][1])#[i][2]
        if labels[i] == 2:
            type2x.append(datamat[i][0])
            type2y.append(datamat[i][1])
        if labels[i] == 3:
            type3x.append(datamat[i][0])
            type3y.append(datamat[i][1])
    ax=fig.add_subplot(111)
    #print(type1x)
    type1=ax.scatter(type1x,type1y,label='type1', s=30,c='red',edgecolors='white')
    type2 = ax.scatter(type2x, type2y, s=30, label='type2',c='black',edgecolors='white')
    type3 = ax.scatter(type3x, type3y, s=30, label='type3',c='green',edgecolors='white')
    plt.xlabel('no3')
    plt.ylabel('no2')
    plt.legend()
    plt.show()