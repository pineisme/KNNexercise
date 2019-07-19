# _*_ coding: utf-8 _*_
"""
date: '2019/7/19 10:10'
....................................

"""
#help(numpy.tile)
import dataset
import knn
import ploitmap
if __name__=='__main__':
    #reee=open('iris.data','r')
    #print(reee.read())
    testratio=0.1#测试0.1个数据集
    dataa,labelvec=dataset.creat_data('datingTestSet2.txt')
    data2knn=dataa[:,0:3]
    nordata,chazhi,minvalue=knn.autonorm(data2knn)
    #ploitmap.plotpic(nordata,labelvec)
    m=nordata.shape[0]
    testNum=int(m*testratio)
    print('testnum= %d'%testNum)
    errnum=0
    for i in range(testNum-1):
        calssifyResult=knn.classify0(nordata[i,:],nordata[testNum:m,:],labelvec[testNum:m],3)
        print('the classifier come back with: %d,the real answer is: %d'%(calssifyResult,labelvec[i]))
        if calssifyResult!=labelvec[i]:
            errnum+=1
    print('the error occured %d times and error ratio is: %f'%(errnum,errnum/testNum))