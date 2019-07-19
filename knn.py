# _*_ coding: utf-8 _*_
"""
date: '2019/7/19 13:57'
....................................

"""
import numpy as np
def autonorm(dataset):
    minval=dataset.min(0)#min(0)每一列最小min(1)每一行最小,此处为一行三列
    maxval=dataset.max(0)
    ranges=maxval-minval
    normdataset=np.zeros(np.shape(dataset))
    m=dataset.shape[0]#shape[0]为第一维的长度，[1]为第二维的长度
    normdataset=dataset-np.tile(minval,(m,1))
    #print(np.tile(minval,(m,1)))
    normdataset=normdataset/np.tile(ranges,(m,1))
    print(normdataset)
    return normdataset, ranges, minval
def classify0(inX,dataset,labels,k):
    datasize=dataset.shape[0]
    diffmat=np.tile(inX,(datasize,1))-dataset
    sqdiffmat=diffmat**2
    seqdistance=sqdiffmat.sum(axis=1)#1行相加，0列相加
    finalDistance=seqdistance**0.5
    #print(type(finalDistance))#<class 'numpy.ndarry>
    sortedDistance=finalDistance.argsort() #arg返回从小到大数的索引
    classCount={}#记录类别次数的字典dict
    for i in range(k):
        choiceLabel=labels[sortedDistance[i]]
        classCount[choiceLabel]=classCount.get(choiceLabel,0)+1#记录该标签被选择了几次#0的意思是如果不存在返回零
    sortedClassCount=sorted(classCount.items(),key=lambda x:x[0],reverse=True)#对选择的次数从大到小进行排序
    #print('[0]and[0][0]',sortedClassCount[0],sortedClassCount[0][0])#(3,2) 3#一个dict方便取key和value的方法
    return sortedClassCount[0][0] # key=operator.itemgetter(1)根据字典的值进行排序# key=operator.itemgetter(0)根据字典的键进行排序


