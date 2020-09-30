# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:18:01 2020

@author: 15-db0011
"""
import numpy as np
import math as mat

    
def distancia(matriz,fila,columna):
    dist=np.zeros((fila,1))
    for i in range(0,len(matriz)-1):
        a=matriz[i,:]
        b=matriz[i+1,:]
        dist[i]= np.linalg.norm(a-b) 
    dist[fila-1]=np.linalg.norm(matriz[0,:]-matriz[fila-1,:])
    return dist

def vibracion(kmax,u1,u2,D):
    resultado=np.zeros((fila,1))
    e=0
    ki=1
    for i in range (0,len(D)):
        e=((1-(ki/kmax))*u1*D[i])
        resultado[i]=e
    return resultado

def ecua_2_3(E,matriz,R1,R2,pathfinder1):
    sol=np.zeros((fila,columna))
    for i in range(0,len(matriz)-1):
        sol[i,:]=matriz[i,:]+(R1*(matriz[i+1,:]-matriz[i,:]))+(R2*(pathfinder1[0,:]-matriz[i,:]))+E[i]    
    sol[fila-1,:]=matriz[fila-1,:]+R1*(matriz[0,:]-matriz[fila-1,:])+R2*(pathfinder1[0,:]-matriz[fila-1,:])+E[fila-1] 
  
    for i in range(fila-1):
        for j in range(columna):
            if sol[i,j]<-5.12:
                sol[i,j]=-5.12
            if sol[i,j]>5.12:
                sol[i,j]=5.12
    return sol
                
def tasa_fluctuacion(u2,kmax):
    resultado=np.zeros((fila,1))
    ki=1
    for i in range (fila):
        a=u2*mat.e**((-2*ki)/kmax)
        resultado=a
    return resultado
       
def Rastrigin(matriz,fila,columna):  
    resultado=np.zeros((fila,1))
    for i in range(fila):
        acum=0
        suma=0
        for j in range(columna):
            acum=((matriz[i,j]**2)-(10*mat.cos(2*mat.pi*matriz[i,j])))+acum
        suma=(10*columna)+acum
        resultado[i]=suma
    return resultado

def valor(vector,columna,matriz):
    menor = np.Inf
    sol=np.zeros((1,columna))
    posic=0
    for i in (range(0, len(vector))):
        if vector[i]<menor:
            menor = vector[i]
            posic=i
#            print(posic)
            sol[:]=matriz[posic,:]
    return menor,sol

def ecuacion_2_4(pathfinder,r3,A,Mejoranterior):
    x=pathfinder+2*r3*(pathfinder-Mejoranterior)+A
    return x

def actualizacion(verificacion,fdx,pathfinder1,pathfinder2):
      if fdx>verificacion:
          optimo=verificacion
          posic=pathfinder2
      else:
          optimo=fdx
          posic=pathfinder1
      return optimo,posic
  
def mejoramatriz(matrizvieja,fdxvieja,matriz,fitness):
    lamejormatriz=np.zeros((fila,columna))
    mejorfitness=np.zeros((fila,1))
    menor=np.Inf
    posic=0
    for i in range((fila)):
        if fitness[i]<fdxvieja[i]:
            menor=fdx
            mejorfitness[i]=menor
            posic=i
            lamejormatriz=matriz[posic,:]
        else:
            lamejormatriz[i,:]=matrizvieja[i]
            mejorfitness[i]=fdxvieja[i]
    return lamejormatriz,mejorfitness
        
fila=500
columna=3
u1=0.01
#u1=np.random.rand(-1,1)
u2=0.05
#u2=np.random.rand(-1,1)
α=0.05
#α=np.random.rand(1,2)
β=0.01
#β=np.random.rand(1,2)
kmax=1000
r1=0.01
#r1=np.random.rand(0,1)
r2=0.05
#r2=np.random.rand(0,1)
r3=0.05
#r3=np.random.rand(0,1)
vector =[]
R1=α*r1
R2=β*r2


a=-5.12
b=5.12
#print("INICIO DE PROGRAMA")
matriz=a+(b-a)*np.random.rand(fila,columna)
#print(matriz)
fitness =Rastrigin(matriz,fila,columna)
#print("Vector Rastrigin - Calculo de fitness -")
#print(fitness)
fdx, pathfinder1=valor(fitness,columna,matriz)
Mejoranterior=pathfinder1
#print('')
#print("Mejor fitness: " + str (fdx))
#print("Pathfinder" + str (pathfinder1))
for i in range(0, kmax):
    matrizvieja=matriz
    fdxvieja=fitness
    A=tasa_fluctuacion(u2,kmax)
 #   print("Valor de A: " + str (A))
    pathfinder2=ecuacion_2_4(pathfinder1,r3,A,Mejoranterior)
    verificacion=Rastrigin(pathfinder2,1,columna)
#    print("Pathfinder con actualizacion " + str (pathfinder2))
#    print("fitness "+ str (verificacion))
    fdx, pathfinder1=actualizacion(verificacion,fdx,pathfinder1,pathfinder2)
#    print("El optimo local es : " + str (fdx))
#    print("Pathfinder" + str (pathfinder1))
#    print("Distancias")
    D=distancia(matriz,fila,columna)
#    print(D)
#    print("Vibracion")    
    E=vibracion(kmax,u1,u2,D)
#    print(E)
    matriz=ecua_2_3(E,matriz,R1,R2,pathfinder1)
#    print("Ecuacion 2.3")
#    print(matriz)
    newfitness=Rastrigin(matriz,fila-1,columna)
#    print("Fitness para miembro en ec 2.3")
#    print(newfitness)
    fdx2, pathfinder3=valor(newfitness,columna,matriz)
#    print("Mejor fitness : " + str (fdx2))
#    print("Pathfinder" + str (pathfinder3))
    fdx,pathfinder1=actualizacion(fdx2,fdx,pathfinder1,pathfinder3)
    matrizvieja,fdxvieja=mejoramatriz(matrizvieja,fdxvieja,matriz,fitness)
#    print(matrizvieja)
#    print(fdxvieja)
    nuevaA=tasa_fluctuacion(u2,kmax)
#    print(nuevaA)
    d2=distancia(matrizvieja,fila,columna)
    nuevaE=vibracion(kmax,u1,u2,d2)
#    print(nuevaE)
print("SOLUCIONES")
print("El optimo global es : " + str (fdx))
print("Pathfinder" + str (pathfinder1))
    


    
        
        
        
    
    

