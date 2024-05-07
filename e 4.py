matriz = [['-','B','C','D','E','F'],['G','H','I','J','K','L'],['M','N','O','P','Q','R'],[]]#HACEMOS LA MATRIZ
import os 
def fnt_limpiar():
    os.system('cls')
    print('autor:ANDRES FELIPE')
    print('7-05-2024')
    print('\n\n')
    
def fnt_agregar(dato,i,j):
    if matriz [i][j] == '-':
       matriz [i][j] == dato.lower()
       input('no se encontro')
    elif matriz[i][j] == 'A':
        input('\nFelicidades acertaste <ENTER> PARA CONTINUAR ')
    elif matriz[i][j] == 'B':
        input('\nFelicidades acertaste <ENTER> PARA CONTINUAR ')
    elif matriz [i][j]== 'C':
        input('\nFelicidades acertaste <ENTER> PARA CONTINUAR')
    
def agregar_dato():
    dato =input('Agregue una letra')
    fila = input('fila :')
    columna= input('Columna:')
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if  matriz[fila][columna] == dato:
                print(matriz[i][j],end=' ')
        print()


def fnt_impresion(): #Se busca el dato proporcionado por el usuario dentrio de la matriz  
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j],end=' ')
        print()
        

sw = True
while sw == True:
    os.system('cls')

    
        


