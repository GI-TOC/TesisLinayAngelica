# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:59:26 2020

@author: 15-db0011
"""
import numpy as np
def Pob_ini(tpob, c,):
    Pob=np.zeros((tpob,c))
    Pob=Pob.astype(int)
    for i in range(tpob):
        for j in range(c):
            tmp=np.random.permutation(c)+1
            Pob[i,:]=tmp
    return Pob
def decod2(Pob_ini,c,tpob):
    matriz=np.zeros((tpob,(c*2)+1))
    matriz=matriz.astype(int)
    tmp=0
    q=25
    #Nodo y Primer cliente
    for i in range(tpob):
            matriz[i,1]=Pob_ini[i,0]
    #Del segundo cliente en adelante
    for i in range(tpob):
            tmp=Dmd1[Pob_ini[i,0]-1]
            pos=1
            j=1
            while j<c:
                tmp=tmp+Dmd1[Pob_ini[i,j]-1]
                if tmp<=q:
                    matriz[i,pos+1]=Pob_ini[i,j]
                    pos=pos+1
                    j=j+1
                else:
                    matriz[i,pos+1]=0
                    pos=pos+1
                    tmp=0
    return matriz
def costo(rutas1,c,tpob,Dmd1):
    arco=np.array([[0,1,2,1,1,2],[1,0,1,1,2,2],[1,1,0,1,2,1],[1,2,2,0,1,1]
                   ,[2,1,1,2,0,2],[1,2,1,1,2,0]])
    m=(c*2)-1
    valor=np.zeros((tpob,1))
    valor=valor.astype(int)
    cont=0
    for i in range(tpob):
        cont=0
        for j in range(m):
            cont= cont+arco[rutas1[i,j],rutas1[i,j+1]]
            valor[i,0]=cont
    return valor
def valor(costo1,Pob_ini,c):
    menor=costo1[0]
    sol=np.zeros((c))
    sol=sol.astype(int)
    posic=0
    for i in (range(0, len(Pob_ini))):
        if costo1[i]<=menor:
            menor =costo1[i]
            posic=i
            sol[:]=Pob_ini[posic,:]  
    return menor,sol
def seleccion(Pob_ini, tpob,c,costo1):
    padres=np.zeros((tpob,c))
    padres=padres.astype(int)
    for i in range(tpob):
        a1=np.random.randint(0,tpob)
        a2=np.random.randint(0,tpob)      
        while a1==a2:
            a1=np.random.randint(0,tpob)
            a2=np.random.randint(0,tpob)    
#        print(a1,a2)
        if costo1[a1]<=costo1[a2]:
            padres[i,:]=Pob_ini[a1,:]
        else:
            padres[i,:]=Pob_ini[a2,:]
    return padres
def cruce(padres,tpob,c,pc):
    hj=np.zeros((tpob,c))
    hj=hj.astype(int)
    for i in range(0,tpob,2):
        na1=np.random.rand()
#        print('N° aleatorio es: '+ str (na1))
        if na1<=pc:
            nac=np.random.randint(0, c-1)            
#           print('El punto de corte es: ' +str (nac))
            for j in range(c):
                if padres[i,j] == padres[i+1,j]:
                    hj[i,j]=padres[i,j]
                    hj[i+1,j]=padres[i+1,j]
#                    print(hj)  
            for j in range(c):
                 m=padres[i,0:nac+1]
                 n=padres[i+1,0:nac+1]
                 hj[i,0:nac+1]=m
                 hj[i+1,0:nac+1]=n
        else:
             hj[i,:]=padres[i,:]
             hj[i+1,:]=padres[i+1,:]
    return hj
def cruce2(cruce1,padres,tpob,c):
    for i in range(0,tpob,2):
        temp=0
        cc=0
        temp1=0
        cc1=0
        for j in range(c):
            temp=np.where(cruce1[i]==padres[i+1,j])
            if temp[0].size<=0:
                 cc=np.where(cruce1[i]==0)
                 cruce1[i,cc[0][0]]=padres[i+1,j]
                
            temp1=np.where(cruce1[i+1]==padres[i,j])
            if temp1[0].size<=0:
                cc1=np.where(cruce1[i+1]==0)
                cruce1[i+1,cc1[0][0]]=padres[i,j]
    return cruce1
def mutacion(hijos, tpob, c):
    c1=0
    c2=0
    a1=0
    a2=0
    for i in range(tpob):
        al=np.random.rand()
        if al<=pm:
            a1=np.random.randint(0,tpob-1)
            a2=np.random.randint(0,tpob-1)
        while a1==a2:
            a1=np.random.randint(0,tpob-1)
            a2=np.random.randint(0,tpob-1)
        c1=hijos[i,a1]
        c2=hijos[i,a2]
        hijos[i,a1]=c2
        hijos[i,a2]=c1 
    return hijos
def actualizar(menor_costo,posi,menor_costo2,posi2,tpob):
    optimo= np.zeros(c)
    optimo=optimo.astype(int)
    optimo2= 10000000000000000000000000000.0
    for i in range(tpob):
          if optimo2>menor_costo:
              optimo[:]=posi[:]
              optimo2= menor_costo
          if optimo2>menor_costo2:
              optimo2=menor_costo2
              optimo[:]=posi2[:]
    return(optimo2,optimo)
    
print("Programa Principal")
#tpob=int(input("Digite la cantidad de soluciones: "))
#c=int(input("Ingrese el numero de clientes: "))
#g=int(input("Ingrese el numero de generaciones: "))
#pc=float(input("ingrese la probabilidad de Cruzamiento: "))
#pm=float(input("ingrese la probabilidad de mutacion: "))
g=100
tpob=6
c=5
q=25
pc=0.95
pm=0.75
Dmd=np.random.randint(1,5,size=(1,tpob))
Dmd1=[5,7,10,9,11]
Pob_ini= Pob_ini(tpob, c)
for i in range (0,g):
    rutas1=decod2(Pob_ini,c,tpob)
    costo1=costo(rutas1,c,tpob,Dmd1)
    menor_costo,posi=valor(costo1,Pob_ini,c)
    padres=seleccion(Pob_ini, tpob,c,costo1)
    cruce1=cruce(padres,tpob,c,pc)
    hijos=cruce2(cruce1,padres,tpob,c)
    hijosm= mutacion(hijos, tpob, c)
    rutas2=decod2(hijosm,c,tpob)
    costo2=costo(rutas2,c,tpob,Dmd1)
    menor_costo2,posi2=valor(costo2,hijosm,c)
    minimo,rutafinal=actualizar(menor_costo,posi,menor_costo2,posi2,tpob)
    Pob_ini=hijos.copy()
print("El mejor al final es ")
print(' ')
print("Menor costo: "+ str (minimo))
print('')
print("Ruta: "+ str (rutafinal))
    




