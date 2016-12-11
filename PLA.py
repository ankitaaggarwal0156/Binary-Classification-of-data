'''
Created on Oct 13, 2016

@author: Ankita
'''
from numpy import random
import sys
Data_list = []
output_coordinate_list=[]
thr=0.01
alpha=0.01
w1 =random.rand(3)
w=[-thr, w1[0],w1[1],w1[2]]
j=0
count=0
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
        output_coordinate_list.append(int(list_of_items_in_line[3]))
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
    global j, count, Data_list 
    #M1 = w_old
    count+=1
    #print "old W", M1   
    for i in range(len(Data_list)):
        if constraintVerify(Data_list[i], output_coordinate_list[i]):
            j=j+1
        else:
            updateW(i)
    #print " Here W", w
    #print "Not classified constraints", 2000-j
    if(j==len(Data_list)):
        print "\n--------------------Output--------------------------------\n"
        print "W final ", w
        print " classified constraints", j 
        print " No. of iterations", count
        print "-------------------------------------------------------------"
    else:
        j=0
        Perceptron(w)



sys.setrecursionlimit(10000)
print "Initial random Weight :\n", w
ReadFile()
flagViolated=0
for i in range(len(Data_list)):
    if constraintVerify(Data_list[i], output_coordinate_list[i]):
        j=j+1
    else:
        updateW(i)
        
        #w_init = M1
        
#print "New W 1", w
#print " Not classified constraints", 2000-j
j=0
count+=1
Perceptron(w)
