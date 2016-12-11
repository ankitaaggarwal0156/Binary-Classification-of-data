'''
Created on Oct 16, 2016

@author: Ankita
'''

from numpy import random
import sys
from matplotlib import pyplot as plt
Data_list = []
output_coordinate_list=[]
thr=0.01
alpha=0.01
w1 =random.rand(3)
w=[-thr, w1[0],w1[1],w1[2]]
j=0
count=0
m=0
iter1=0
list_point=[]
weightMatrix=[]
def ReadFile():
    list_of_coordinates = []
    global Data_list
    global output_coordinate_list
    with open("./classification.txt", "r") as fo:
        for line in fo:
            list_of_coordinates.append(line)
    fo.close()
    for line in list_of_coordinates:
        list_of_items_in_line = line.split(",")
        Data_list.append([1,float(list_of_items_in_line[0]),float(list_of_items_in_line[1]),float(list_of_items_in_line[2])])
        output_coordinate_list.append(int(list_of_items_in_line[4]))
    #for r in Data_list:
    #    print  r
    #print "output", output_coordinate_list
    
    
def constraintVerify(X,Y):
    global w
    if (((w[0]*X[0])+(w[1]*X[1])+(w[2]*X[2])+(w[3]*X[3]))>=0 and Y==1):
        return True
    elif (((w[0] * X[0]) + (w[1] * X[1]) + (w[2] * X[2]) + (w[3] * X[3])) < 0 and Y == -1):
        return True
    else:
        return False
    
    
def updateW(i):
    global w
    if ((output_coordinate_list[i] == 1) and (
                (w[0] * Data_list[i][0]) + (w[1] * Data_list[i][1]) + (w[2] * Data_list[i][2]) + (
        w[3] * Data_list[i][3])) < 0): # use true or false from abov method
        w[0] = w[0] + (alpha * Data_list[i][0])
        w[1] = w[1] + (alpha * Data_list[i][1])
        w[2] = w[2] + (alpha * Data_list[i][2])
        w[3] = w[3] + (alpha * Data_list[i][3])
    elif ((output_coordinate_list[i] == -1) and (               
                (w[0] * Data_list[i][0]) + (w[1] * Data_list[i][1]) + (w[2] * Data_list[i][2]) + (
        w[3] * Data_list[i][3])) >= 0):
        w[0] = w[0] - (alpha * Data_list[i][0])
        w[1] = w[1] - (alpha * Data_list[i][1])
        w[2] = w[2] - (alpha * Data_list[i][2])
        w[3] = w[3] - (alpha * Data_list[i][3])
    if constraintVerify(Data_list[i], output_coordinate_list[i]):
        pass
    else:
        updateW(i)
           

def Perceptron(w_old): 
    global j, count, m,iter1, list_point, Data_list
    #print " Weight Matrix =", weightMatrix
    #M1 = w_old
    #print "old W", M1
    while (count<7000): 
        count+=1
        j=0  
        for i in range(len(Data_list)):
            if constraintVerify(Data_list[i], output_coordinate_list[i]):
                j=j+1
            else:
                updateW(i)
        #print " Here W", w
        Weightupdate(w)
        #print "Not classified constraints", 2000-j
        list_point.append(len(Data_list)-j)
        #print " Weight Matrix =", weightMatrix
        if((len(Data_list)-j)<m):
            m = len(Data_list)-j
            iter1 = count
        if(m==0):
            break
    
    if(count ==7000 or m==0):
        #print iter1
        print "\n------------------Pocket Algorithm output for 7000 iterations -------------------------\n"
        print "W final for min misclassified constraints:\n ", weightMatrix[iter1-1]
        #print " classified constraints", j 
        #print " No. of iterations", count
        print "minimum misclassified constraints", m
        print "-----------------------------------------------------------------------------------"
        plotting()
        



def Weightupdate(m):
    global weightMatrix
    temp=m[:]
    weightMatrix.append(temp)
    #print " new method \n \n"
    #for r in weightMatrix:
    #   print r

def plotting():
    global list_point
    plt.plot(list_point,'ro')
    plt.ylabel("Misclassied points")
    plt.xlabel("Iteration#")
    plt.axis([0, 7000, 900, 1050])            
    plt.show()

  
sys.setrecursionlimit(15000)
print "Inital Random Weight: \n", w
ReadFile()
flagViolated=0
for i in range(len(Data_list)):
    if constraintVerify(Data_list[i], output_coordinate_list[i]):
        j=j+1
    else:
        updateW(i)

        
#print "New W 1", w
#print " Not classified constraints", 2000-j
m=len(Data_list)-j
list_point.append(len(Data_list)-j)
iter1=1
j=0
count+=1
Weightupdate(w)
#print "i am heree", weightMatrix
Perceptron(w)
