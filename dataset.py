# _*_ coding: utf-8 _*_
"""
date: '2019/7/19 9:40'
....................................

"""
import numpy as np
def creat_data(inputpath):
    index=0
    classlabel=[]
    with open(inputpath,'r') as f:
        reader=f.readlines()
        linenumber=len(reader)
        returnmat = np.zeros((linenumber, 3))
        for rows in reader:
            lines=rows.strip()
            listline=lines.split('\t')
            #print(listline)
            returnmat[index,:]=listline[0:3]
            classlabel.append(int(listline[-1]))
            #print(type(classlabel[0]))
            index+=1

    #print(returnmat)
    #print(classlabel)
    return returnmat,classlabel



