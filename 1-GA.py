# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:48:33 2020

@author: 15-db0011
"""

import numpy as np
import math as mat

def Rastrigin(matriz):  
    Resultado=np.zeros((fila,1))
    for i in range(fila):
        acum=0
        suma=0
        for j in range(columna):
            acum=((matriz[i,j]**2)-(10*mat.cos(2*mat.pi*matriz[i,j])))+acum
        suma=(10*columna)+acum
        Resultado[i]=suma
    return Resultado 
    
def valor(vector,columna,matriz):
    menor = vector[0]
    sol=np.zeros((columna))
    posic=0
    for i in (range(0, len(vector))):
        if vector[i]<menor:
            menor = vector[i]
            posic=i
#            print(posic)
            sol[:]=matriz[posic,:]
    return menor,sol


def Seleccion(matriz):
    a=Rastrigin(matriz)
#    print(a)
    b=np.zeros((fila,columna))
   
    for i in range(fila):
        na1=np.random.randint(0,fila)
        na2=np.random.randint(0,fila)
        
        while na1==na2: 
            na1=np.random.randint(0,fila)
            na2=np.random.randint(0,fila)
#        print(na1,na2)
        fila1=a[na1]
        fila2=a[na2]
        if fila1<fila2:
            b[i]=matriz[na1]
        else:
            b[i]=matriz[na2]
    return b    

def cruce(matriz):
#    print(matriz) 
    w=np.zeros((fila,columna))
    #acum=0
    for i in range(0,fila,2):
        na1=np.random.randint(0, columna-1)
        na=np.random.rand()
#        print(na1)
#        print(na)
        if na<=pc:
            w[i,0:na1+1]=matriz[i,0:na1+1]
            w[i+1,na1+1:]=matriz[i,na1+1:]
            w[i+1,0:na1+1]=matriz[i+1,0:na1+1]
            w[i,na1+1:]=matriz[i+1,na1+1:]
        
        else:
             w[i,:]=matriz[i,:]
             w[i+1,:]=matriz[i+1,:]
    return w

def mutacion(Hijos_Cruce):
    a=-5.12
    b=5.12
    for i in range(fila):
        na1=np.random.rand()
#        print(na1)
        if na1<=pm:
            na=np.random.randint(0,columna)
#            print("La Posicion a mutar es:")
#            print(na)
            Hijos_Cruce[i,na]=a+(b-a)*np.random.rand()
#            print("El nuevo Gen es: ")
#            print( Hijos_Cruce[i,na])
        else:
            Hijos_Cruce[i]=Hijos_Cruce[i]
    return(Hijos_Cruce)  
    
def actualizar(Posicion,Mejorx,Posicion2,Mejorx2,fila):
    optimo= np.zeros(columna)
    optimo2= 10000000000000000000000000000.0
    for i in range(fila):
          if optimo2>Mejorx:
              optimo[:]=Posicion[:]
              optimo2= Mejorx
          if optimo2>Mejorx2:
              optimo2=Mejorx2
              optimo[:]=Posicion2[:]
    return(optimo2,optimo)              
    
print("Inicia programa principal")
x=int(input("Digite el numero de filas de la matriz:"))
y=int(input("Digite el numero de columnas de la matriz:"))
#z=int(input("Diga el numero de iteraciones"))
z=int(input("Ingrese el numero de generaciones: "))
#pc=float(input("ingrese la probabilidad de Cruzamiento: "))
pc=0.90
#pm=float(input("ingrese la probabilidad de mutacion: "))
pm=0.75

"Parametro de la matriz:"
a=-5.12
b=5.12
vector = []
Mejorx = 0 
matriz=a+(b-a)*np.random.rand(x,y)
"Redinmensionamiento"
fila,columna=matriz.shape

for i in range (z):
#    print(matriz)
    vector = (Rastrigin(matriz))
#    print("Vector Rastrigin")
#    print(vector)
    Mejorx, Posicion=(valor(vector,columna,matriz))
#    print('')
#    print("El mejor de f(x) es: " + str (Mejorx))
#    print('')
#    print("Los mejores genes son: " + str (Posicion))
#    print('')
    Padres=(Seleccion(matriz))
#    print('')
#    print("Esta es la matriz de padres:")
#    print('')
#    print((Padres))
#    print('')
    Hijos_Cruce=(cruce(matriz))
#    print("Los hijos son: ")
#    print('')
#    print(Hijos_Cruce)
#    print('')
    Hijos_Muta = mutacion(Hijos_Cruce)
#    print('')
#    print("Los hijos mutados son: ")
#    print('')
#    print(Hijos_Muta)
#    print('')
    Rastrigin2 = Rastrigin(Hijos_Muta)
#    print(Rastrigin2)
#    print('')
    Mejorx2, Posicion2=(valor(Rastrigin2,columna,Hijos_Muta))
#    print("El mejor f(x) del final"+ str (Mejorx2))
#    print('')
#    print("Los mejores genes finales son: "+ str (Posicion2))
#    print('')
#    print('')
    matriz=Hijos_Muta.copy()
    Optimoglobal, Genes= actualizar(Posicion,Mejorx,Posicion2,Mejorx2,fila)
print("El mejor al final es : ")
print("el mejor f(x) es: "+ str (Optimoglobal))
print('')
print("Los mejores genes son: "+ str (Genes))
    

