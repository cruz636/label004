# -*- coding: cp1252 -*-
import os,random


global diccionario
leerDiccionario = open('diccionario.txt','r')
listaDeDiccionario  = (leerDiccionario.read()).split(",")

leerDiccionario.close()
diccionario = {}
n = 0
longitudDeListaDeDiccionario = len(listaDeDiccionario)
while n <= (longitudDeListaDeDiccionario-2):
    palabra = listaDeDiccionario[n]
    significado = listaDeDiccionario[n+1]
    diccionario[palabra] = [significado]
    n = n+2



def main():
    #global consulta
    comando = raw_input(">> ")
    listaPalabrasComando = comando.split()
    longitudDeListaDePalabras = len(listaPalabrasComando)

    i = 1
    consulta = ""
    while (i < longitudDeListaDePalabras):
        consulta = consulta + " " + listaPalabrasComando[i]
        i = i + 1
    print "consulta = " + consulta


    #aca tienen que ir los if con los comandos principales que se aplican 
    #segun la primer palabra del comando

    if listaPalabrasComando[0] == "como" and listaPalabrasComando[1] == "hago":
        consulta = "como " + consulta
        buscar(consulta)
        main()

    if listaPalabrasComando[0]== "ver":
        video(consulta)
        
        main()

    if listaPalabrasComando[0] == "leer" and listaPalabrasComando[1] == "diccionario":
        diccionarioDos()
        main()

    if listaPalabrasComando[0] == "pass":
        print "hcjvkt9q"
        main()

    if listaPalabrasComando[0] == "multiplicar":
        primerValor = float(listaPalabrasComando[1])
        segundoValor = float(listaPalabrasComando[3])
        multiplicacion(primerValor,segundoValor)
        main()

    if listaPalabrasComando[0] == "dividir" :
        primerValor = float(listaPalabrasComando[1])
        segundoValor = float(listaPalabrasComando[3])
        division(primerValor,segundoValor)
        main()

    if listaPalabrasComando[0] == "cociente" :
        primerValor = float(listaPalabrasComando[2])
        segundoValor = float(listaPalabrasComando[4])
        cociente(primerValor,segundoValor)
        main()

    if listaPalabrasComando[0] == "resto" :
        primerValor = int(listaPalabrasComando[2])
        segundoValor = int(listaPalabrasComando[4])
        restoDe(primerValor,segundoValor)
        main()

    if listaPalabrasComando[0] == "restar" : 
        primerValor = float(listaPalabrasComando[1])
        segundoValor = float(listaPalabrasComando[3])
        restaDe(primerValor,segundoValor)
        main()

    if listaPalabrasComando[0] == "recargar" or listaPalabrasComando[0] == "r":
        path = 'cd C:\Users\Cruz619\Documents\python'
        os.system(path)
        os.system('"yuri v1.py"')

    if listaPalabrasComando[0] == "hibernar" or listaPalabrasComando[0]=="h":
        print "Hibernando"
        os.system("shutdown /h")
        main()

    if listaPalabrasComando[0]=="clean":
        os.system("cls")
        main()
   

    if diccionario.has_key(comando):
        print diccionario[comando]
        main()

    else:
        primerPalabra = diccionario.get(comando)

        if primerPalabra == None :
            significado = raw_input("Qué significa " + comando + "?")
            diccionario[comando] = [significado]
            escribirDiccionario = open('diccionario.txt','a')
            escribirDiccionario.write(","+comando+","+significado)           
            escribirDiccionario.close()
            
            print "Diccionario actualizado"

        print primerPalabra
        main()

def diccionarioDos():
    archivo = open('diccionario.txt','r')
    diccionario = archivo.read()
    archivo.close()
   


def buscar(consulta): 
    url = '"' + "https://www.google.com.ar/search?q="+ consulta + '"'
    os.system("start firefox.exe "+url)

def video(videoId):
    url = '"'+ " https://www.youtube.com/results?search_query="+ videoId + '"'
    os.system("start firefox.exe "+url)

def multiplicacion(primerValor,segundoValor):
    print (primerValor * segundoValor)

def division(primerValor,segundoValor):
    print (primerValor / segundoValor)

def cociente(primerValor,segundoValor):
    print (primerValor // segundoValor)

def restoDe(primerValor,segundoValor):
    print (primerValor % segundoValor)

def restaDe(primerValor,segundoValor):
    print (primerValor - segundoValor)





main()






