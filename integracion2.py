# @autor: Juan Mercado
# date: 14-07-22
from sympy import true
import numpy as np
import math as m
from math import pi
import serial
import time
import trayectoria_v03 as ty

def main():
    z = float(input("Ingrese el valor de Z"))
    # con z=5 se realiza el algoritmo
    if z==5:
        # comunicacion serial
        arduino = serial.Serial("COM8",9600,timeout=1.0) 
        time.sleep(1)
        art_var_each_point = [] # lista de variables articulares
        for i in range(0,len(ty.sampled_coord)):
            z=ty.sampled_coord[i][0]
            x=ty.sampled_coord[i][1]
            if (int(z)<5):
                q1 = 0
                R = int( m.sqrt(m.pow((z-15),2)+m.pow(x,2)))
                q2 = int(m.atan((z-20)/(x-3.5))*(180/m.pi)+85)
            elif (int(z)<=35 & int(z)>=5):
                q1 = 1
                R = int( m.sqrt(m.pow((z-20),2)+m.pow(x,2)))
                q2 = int(m.atan((z-20)/(x-3.5))*(180/m.pi)+85)
            #elif (z>35):
            else:
                q1 = 2
                R = int( m.sqrt(m.pow((z-25),2)+m.pow(x,2)))
                q2 = int(m.atan((z-20)/(x-3.5))*(180/m.pi)+85)
            if R == 0:
                q = np.array([q1,q2,98, 0, 129])
            elif R == 1:
                q = np.array([q1,q2,100, 0, 128])
            elif R == 2:
                q = np.array([q1,q2,104, 0, 128])
            elif R == 3:
                q = np.array([q1,q2,107, 0, 126])
            elif R == 4:
                q = np.array([q1,q2,109, 0, 124])
            elif R == 5:
                q = np.array([q1,q2,110, 0, 121])
            elif R == 6:
                q = np.array([q1,q2,112, 0, 118])
            elif R == 7:
                q = np.array([q1,q2,113, 0, 115])
            elif R == 8:
                q = np.array([q1,q2,115, 0, 112])
            elif R == 9:
                q = np.array([q1,q2,115, 0, 108])
            elif R == 10:
                q = np.array([q1,q2,116, 0, 105])
            elif R == 11:
                q = np.array([q1,q2,116, 0, 101])
            elif R == 12:
                q = np.array([q1,q2,116, 0, 96])
            elif R == 13:
                q = np.array([q1,q2,112, 4, 98])
            elif R == 14:
                q = np.array([q1,q2,112, 4, 93])
            elif R == 15:
                q = np.array([q1,q2,102, 16, 102])
            elif R == 16:
                q = np.array([q1,q2,104, 16, 98])
            elif R == 17:
                q = np.array([q1,q2,96, 24, 105])
            elif R == 18:
                q = np.array([q1,q2,96, 24, 100])
            elif R == 19:
                q = np.array([q1,q2,92, 30, 103])
            elif R == 20:
                q = np.array([q1,q2,92, 30, 100])
            elif R == 21:
                q = np.array([q1,q2,90, 30, 94])
            elif R == 22:
                q = np.array([q1,q2,90, 30, 90])
            elif R == 23:
                q = np.array([q1,q2,89, 30, 85])
            elif R == 24:
                q = np.array([q1,q2,92, 26, 77])
            elif R == 25:
                q = np.array([q1,q2,90, 24, 68])
            elif R == 26:
                q = np.array([q1,q2,87, 30, 71])
            elif R == 27:
                q = np.array([q1,q2,87, 27, 62])
            elif R == 28:
                q = np.array([q1,q2,85, 27, 53])
            elif R == 29:
                q = np.array([q1,q2,81, 30, 53])
            elif R == 30:
                q = np.array([q1,q2,79, 34, 53])
            elif R == 31:
                q = np.array([q1,q2,77, 34, 45])
            elif R == 32:
                q = np.array([q1,q2,73, 45, 59])
            elif R == 33:
                q = np.array([q1,q2,71, 47, 55])
            elif R == 34:
                q = np.array([q1,q2,66, 54, 61])
            elif R == 35:
                q = np.array([q1,q2,64, 54, 61])
            elif R == 36:
                q = np.array([q1,q2,61, 58, 52])
            elif R == 37:
                q = np.array([q1,q2,60, 58, 45])
            elif R == 38:
                q = np.array([q1,q2,56, 70, 57])
            elif R == 39:
                q = np.array([q1,q2,52, 80, 62])
            elif R == 40:
                q = np.array([q1,q2,48, 80, 54])
            elif R == 42:
                q = np.array([q1,q2,40, 88, 50])
            q = [int(q[0]),int(q[1]),int(q[2]),int(q[3]),int(q[4])]

            art_var_each_point.append(q)    
            print(art_var_each_point)
        for k in range(0,len(art_var_each_point)):
            cad = ""
            mot=str(art_var_each_point[k][0])+","+str(art_var_each_point[k][1]) +","+str(art_var_each_point[k][2]) +","+str(art_var_each_point[k][3])+","+str(art_var_each_point[k][4])
            #mot=(var1)+","+(var2) +","+(var3) +","+(var4)+","+(var5)
            cad="mot:"+mot
            arduino.write(cad.encode('ascii'))
            time.sleep(3)
            print(cad)
        mot=str(1)+","+str(85) +","+str(170) +","+str(30)+","+str(180)
        #mot=(var1)+","+(var2) +","+(var3) +","+(var4)+","+(var5)
        cad="mot:"+mot
        arduino.write(cad.encode('ascii'))
        print(cad)
        mot=str(1)+","+str(85) +","+str(170) +","+str(30)+","+str(180)
        #mot=(var1)+","+(var2) +","+(var3) +","+(var4)+","+(var5)
        cad="mot:"+mot
        arduino.write(cad.encode('ascii'))
        print(cad)
    else:
        print("m")  
     

if __name__=="__main__": main()
