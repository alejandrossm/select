from alumnito import Alumno
from random import randint
from time import sleep

from os import system
system("cls")

alumnos=[]
alumnosobj=[]

f=open("csvs7.csv","r")

while True:
    
    datos=f.read()
    alumnos=datos.split("\n")
    #print(alumnos)
    
    for aluline in alumnos:
        
        if len(aluline)>0:
            alulist=aluline.split(";")
            #print(alulist)
            #input()
            al=Alumno()
            al.rut=alulist[0]
            al.paterno=alulist[1]
            al.materno=alulist[2]
            al.nombre=alulist[3]
            alumnosobj.append(al)
        
    if not datos:
        f.close()
        break

print(alumnosobj)

total=len(alumnosobj)
suerte=randint(1,total)
sec=0.01
mult=0.01
for a in range(4):
    for b in alumnosobj:
        system("cls")
        print(b)
        sleep(sec*mult)
        mult+=0.2

system("cls")

print("******************Resuelve el Ejercicio******************")
print(f"\t😊🍀🍀 {alumnosobj[suerte-1]}😁😁")
print("\n\n***************************************")
