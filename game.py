#game
print "memory game by anmol and ankit"
raw_input("press enter to start the game:")
import os
import time

def print_2D(ck_lst_x,ck_lst_o,ck_lst_r):
    count=0 
    for i in range(36):
        if i in ck_lst_x:
            print "X",
        elif i in ck_lst_o:
            print "O",
        elif i in ck_lst_r:
            print "R",
        else :
            print "#",
        count+=1
        if count%6==0:
            print '\n'
def print_2D2(ck_lst_x,ck_lst_o,ck_lst_r,ck_pt_f1,a,ck_pt_f2,b):
    count=0
    for i in range(36):
        if i in ck_lst_x:
            print "X",
        elif i in ck_lst_o:
            print "O",
        elif i in ck_lst_r:
            print "R",
        else:
            if i == ck_pt_f1:
                print a,
            elif i == ck_pt_f2:
                print b,
            else :
                print "#",
        count+=1
        if count%6==0:
            print '\n'
import random
moves=0
points = range(36)
list_x=random.sample(points,12)
list_rem=[ y for y in points if y not in list_x]
list_o = random.sample(list_rem,12)
list_r = [z for z in list_rem if z not in list_o]
list_dx=[]
list_do=[]
list_dr=[]
while(True):
        input_1str=raw_input("please enter the 1 point: ")
        input_2str=raw_input("please enter the 2 point: ")
        input_1=map(int,input_1str.split(","))
        input_2=map(int,input_2str.split(","))
        point_f1= 6*(input_1[0]-1)+(input_1[1]-1)
        point_f2= 6*(input_2[0]-1)+(input_2[1]-1)
        if input_1[0]>6 or input_1[1]> 6 or input_2[0]> 6 or input_2[1]> 6:
            print "plz enter a number between 1-6"        

        elif point_f1==point_f2:
            print "plz enter distinct points !!"
        elif point_f1 in list_dx or point_f1 in list_do or point_f1 in list_dr or point_f2 in list_dx or point_f2 in list_do or point_f2 in list_dr:
            print "one of the entered box is already open ,plz enter another value"
        else:
  
            if point_f1 in list_x and point_f2 in list_x   :
                list_dx.append(list_x.pop(list_x.index(point_f1)))
                list_dx.append(list_x.pop(list_x.index(point_f2)))
                print_2D(list_dx,list_do,list_dr)
                print "your guess was right!! :)"
                raw_input("press enter for next turn ")
                os.system('cls')
            elif point_f1 in list_o and point_f2 in list_o   :
                list_do.append(list_o.pop(list_o.index(point_f1)))
                list_do.append(list_o.pop(list_o.index(point_f2)))
                print_2D(list_dx,list_do,list_dr)
                print "your guess was right!! :)"
                raw_input("press enter for next turn ")
                os.system('cls')    
            elif point_f1 in list_r and point_f2 in list_r   :
                list_dr.append(list_r.pop(list_r.index(point_f1)))
                list_dr.append(list_r.pop(list_r.index(point_f2)))
                print_2D(list_dx,list_do,list_dr)
                print "your guess was right!! :)"
                raw_input("press enter for next turn ")
                os.system('cls')
            else:    
                if point_f1 in list_x and point_f2 not in list_x:
                    if point_f2 in list_o:
                        print_2D2(list_dx,list_do,list_dr,point_f1,"X",point_f2,"O")#print karwana  
                    else:
                        print_2D2(list_dx,list_do,list_dr,point_f1,"X",point_f2,"R")#print karwana
                    print "your guess was wrong"
                    raw_input("press enter for next turn ")
                    os.system('cls')   
                elif point_f1 in list_o and point_f2 not in list_o:
                     if point_f2 in list_r:
                        print_2D2(list_dx,list_do,list_dr,point_f1,"O",point_f2,"R")#print karwana  
                     else:
                        print_2D2(list_dx,list_do,list_dr,point_f1,"O",point_f2,"X")#print karwana
                     print "your guess was wrong"
                     raw_input("press enter for next turn ")
                     os.system('cls')  
                elif point_f1 in list_r and point_f2 not in list_r:
                    if point_f2 in list_o:
                        print_2D2(list_dx,list_do,list_dr,point_f1,"R",point_f2,"O")#print karwana  
                    else:
                        print_2D2(list_dx,list_do,list_dr,point_f1,"R",point_f2,"X")#print karwana
                    print "your guess was wrong"
                    raw_input("press enter for next turn ")
                    os.system('cls')            
        if len (list_dx) == 12 and len(list_do) == 12 and len(list_dr)==12:  
            print moves
            break 
        moves+=1
