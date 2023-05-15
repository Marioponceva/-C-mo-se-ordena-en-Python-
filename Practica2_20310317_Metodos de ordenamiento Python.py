#Mario Alberto Ponce Vazquez_20310317_6E_Inteligencia Artificial

#Metodos de ordenamiento en python

from __future__ import print_function
from random import sample 
# Importamos un metodo de la biblioteca random para generar listas aleatorias

lista = range(100) 
# Creamos la lista base con números del 1 al 100

#Listas aleatorias del largo de 8 elementos para cada ordenamiento 
vectorbsort         = sample(lista,8) 
vectorselectsort    = sample(lista,8)
vectorinsort        = sample(lista,8) 
vectorshellsort     = sample(lista,8)
vectormergesort     = sample(lista,8)
vectorquicksort     = sample(lista,8)
vectorheapsort      = sample(lista,8)
vectorcombsort      = sample(lista,8)
vectorcocktailsort  = sample(lista,8)
vectortreeSort      = sample(lista,8)
vectoradixsort      = sample(lista,8)

def bubblesort(vectorbsort):
    """Esta función ordenara el vector que se paso como argumento
    con el metodo de Bubble Sort"""
    
    #Lista de elementos obtenida al principio(Desordenados)
    print("----------------------------------------------------------------------")
    print("El vector a ordenar con bubble es:",vectorbsort)
    
    n = 0 # Contador para obtener el largo del vector 
    
    for _ in vectorbsort:
        n += 1 #Cuenta la cantidad de caracteres dentro del vector 
    
    for i in range(n-1): 
    # Rango n para que complete el proceso. 
        for j in range(0, n-i-1): 
            # Revisa la matriz de 0 hasta n-i-1
            if vectorbsort[j] > vectorbsort[j+1] :
                vectorbsort[j], vectorbsort[j+1] = vectorbsort[j+1], vectorbsort[j]
            #Aqui se intercambian si el elemento que fue encontrado resulto mayor
            #se pasa al siguiente
            
    print ("El vector ordenado con bubble es: ", vectorbsort)

#------------------------------------------------------------------------
def selectionsort(vectorselectsort):
    """Esta función ordenara el vector que se paso como argumento 
    con el metodo Selection Sort"""
    
    # Imprimimos la lista obtenida al principio (Desordenada)
    
    print("----------------------------------------------------------------------")
    print ("El vector a ordenar con selección es:",vectorselectsort)
    
    largo = 0 #inicializamos el contador largo en 0
    
    for _ in vectorselectsort:
        largo += 1 # obtengo el largo del vector
        
    for i in range(largo): 
      
        # Encontrar el minimo elemento de los restantes sin ordenar
        minimo = i 
        for j in range(i+1, largo): 
            if vectorselectsort[minimo] > vectorselectsort[j]: 
                minimo = j 
                
        #Cambio el elemento minimo encontrado por el primer elemento de la matriz 
        vectorselectsort[i], vectorselectsort[minimo] = vectorselectsort[minimo], vectorselectsort[i]
        # Repetimos el proceso hasta terminar
    print("El vector ordenado con selección es: ",vectorselectsort)

#----------------------------------------------------------------------------
def insertionsort(vectorinsort): 
    """Esta función ordenara el vector que le pases como argumento 
    con el metodo Insertion Sort"""
    
    # La lista obtenida al principio (Desordenada)
    print("----------------------------------------------------------------------")
    print("El vector a ordenar con inserción es:", vectorinsort)
    
    largo = 0 # contador del largo
     
    for i in vectorinsort:
        largo += 1 # Obtengo  el largo del vector
    
    #Recorremos  la lista de 1 hasta el largo del vector
    for i in range(1, largo): 
    
        elemento = vectorinsort[i] 
  
        # Movemos los elementos de vectorins[0...i-1], que son mayores que el elemento a una posición adelante de su posición actual
        j = i-1
        while j >= 0 and elemento < vectorinsort[j] : 
                vectorinsort[j+1] = vectorinsort[j] 
                j -= 1
        vectorinsort[j+1] = elemento 
    print("El vector ordenado con inserción es: ", vectorinsort)


#----------------------------------------------------------------------------------
def shellsort(vectorshellsort):
    
    """Esta función ordenara el vector que le pases como argumento 
    con el metodo Shell Sort"""
    
    print("----------------------------------------------------------------------")
    print("El vector a ordenar con shell es:", vectorshellsort)
    
    largo = 0
    
    for i in vectorshellsort:
        largo += 1
    
    distancia = largo // 2
    
     # Creamos un bucle según las distancias
    while distancia > 0:
        # Utilizamos el Insertionsort
        for i in range(distancia, largo):
            val = vectorshellsort[i]
            j = i
            while j >= distancia and vectorshellsort[j - distancia] > val:
                vectorshellsort[j] = vectorshellsort[j - distancia]
                j -= distancia
            vectorshellsort[j] = val
        distancia //= 2 # Acotamos la distancia nuevamente y continua el ciclo
    print("El vector ordenado con shell es: ", vectorshellsort )


#--------------------------------------------------------------------
def mergesort(vectormergesort): 
    """Esta función ordenara el vector que le pases como argumento 
    con el metodo Merge Sort"""
    
    print("----------------------------------------------------------------------")
    # La lista obtenida al principio (Desordenada)
    print("El vector a ordenar con merge es:", vectormergesort)
    
    def merge(vectormergesort):
    
        def largo(vec):
                largovec = 0 # contador del largovec
                for _ in vec:
                    largovec += 1 # Obtengo el largo del vector
                return largovec
        
        
        if largo(vectormergesort) >1: 
            medio = largo(vectormergesort)//2 # Busco el medio del vector
            
            # Lo divido en 2 partes 
            izq = vectormergesort[:medio]  
            der = vectormergesort[medio:]
            
            merge(izq) # Mismo procedimiento a la primer mitad
            merge(der) # Mismo procedimiento a la segunda mitad
            
            i = j = k = 0
            
            # Copio los datos a los vectores temporales izq[] y der[] 
            while i < largo(izq) and j < largo(der): 
                if izq[i] < der[j]: 
                    vectormergesort[k] = izq[i] 
                    i+= 1
                else: 
                    vectormergesort[k] = der[j] 
                    j+= 1
                k += 1
            
            # Reviso  si quedaron elementos en la lista
            # Esto es tanto para la  derecha como izquierda 
            while i < largo(izq): 
                vectormergesort[k] = izq[i] 
                i+= 1
                k+= 1
            
            while j < largo(der): 
                vectormergesort[k] = der[j] 
                j+= 1
                k+= 1
    merge(vectormergesort)
    print("El vector ordenado con merge es: ", vectormergesort)
    
#--------------------------------------------------------------------------------------
def quicksort(vectorquicksort, start = 0, end = len(vectorquicksort) - 1 ):
    """Esta función ordenara el vector que le pases como argumento 
    con el metodo Quick Sort"""
    print("----------------------------------------------------------------------")
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con quick es:", vectorquicksort)
    
    def quick(vectorquicksort, start = 0, end = len(vectorquicksort) - 1):
        
        
        if start >= end:
            return

        def particion(vectorquicksort, start = 0, end = len(vectorquicksort) - 1):
            pivot = vectorquicksort[start]
            menor = start + 1
            mayor = end

            while True:
                #Si el valor actual  es mayor que el pivot
                #significa que esta en el lugar correcto(a la derecha del pivot)
                #entonces nos movemos a la izquierda, al siguiente elemento.
                #tambien puedo asegurarme de que no haya superado el puntero bajo, ya  que este indica
                #que ya hemos movido todos los elemento del lado correcto del pivote
                while menor <= mayor and vectorquicksort[mayor] >= pivot:
                    mayor = mayor - 1

                # Proceso opuesto al anterior            
                while menor <= mayor and vectorquicksort[menor] <= pivot:
                    menor = menor + 1

                #ya que se encuentra un valor que sea mayor o menor y que se encuentre fuera del arreglo
                #o menor es mas gran que mayor,dado ese caso salimos del ciclo
                if menor <= mayor:
                    vectorquicksort[menor], vectorquicksort[mayor] = vectorquicksort[mayor], vectorquicksort[menor]
                    # Continua el bucle
                else:
                    # Salimos del bucle
                    break

            vectorquicksort[start], vectorquicksort[mayor] = vectorquicksort[mayor], vectorquicksort[start]
            
            return mayor
        
        p = particion(vectorquicksort, start, end)
        quick(vectorquicksort, start, p-1)
        quick(vectorquicksort, p+1, end)
        
    quick(vectorquicksort)
    print("El vector ordenado con quick es:", vectorquicksort)
    
#----------------------------------------------------------------------------------------------------
def heapsort(vectorheapsort):
    """Esta función ordenara el vector que le pases como argumento 
    con el metodo Heap Sort"""
    
    print("----------------------------------------------------------------------")
    # La lista obtenida al principio (Desordenada)
    print("El vector a ordenar con heap es:", vectorheapsort)

    largo = 0 # contador del largo
        
    for _ in vectorheapsort:
        largo += 1 # Obtengo el largo del vector

    # Para amontonar la subparte a partir de i. 
    # n es el tamaño del montón.
    def amontonar(vectorheapsort, n, i): 
        mas_largo = i # Tomo i como el más grande 
        izq = 2 * i + 1      
        der = 2 * i + 2    
    
        
        if izq < n and vectorheapsort[i] < vectorheapsort[izq]: 
            mas_largo = izq 
    
        #tenemos que ver si existe la subparte perteneciente a i de manera correcta
        #si es mayor que i
        if der < n and vectorheapsort[mas_largo] < vectorheapsort[der]: 
            mas_largo = der 
            
    
        if mas_largo != i: 
            vectorheapsort[i],vectorheapsort[mas_largo] = vectorheapsort[mas_largo],vectorheapsort[i]
            # Cambiar el origen, si es necesario
            # amontonar el origen. 
            amontonar(vectorheapsort, n, mas_largo)
            
    def heap(vectorheapsort):
        
        n = largo
        # Crear un montón maximo 
        for i in range(n//2 - 1, -1, -1): 
            amontonar(vectorheapsort, n, i) 
    
        # Extraer elementos uno a uno
        for i in range(n-1, 0, -1): 
            vectorheapsort[i], vectorheapsort[0] = vectorheapsort[0], vectorheapsort[i] 
            # Intercambio 
            amontonar(vectorheapsort, i, 0)
        
    heap(vectorheapsort)
    print("El vector ordenado con heap es:", vectorheapsort)
    
#-------------------------------------------------------------------------------------------------
def combsort(vectorcombsort):
    """Esta función ordenara el vector que le pases como argumento
    con el metodo de Comb Sort"""
    
    
    print("----------------------------------------------------------------------")
    # La lista obtenida al principio (Desordenada)
    print("El vector a ordenar con comb es:",vectorcombsort)
    
    largo = 0 # Establecemos un contador del largo del vector
    
    for _ in vectorcombsort:
        largo += 1
    
    
    # Comenzamos con la diferencia o distancia igual al largo del vector
    diferencia = largo
    
    #Establesco la variable que define si es necesario o no 
    #intercambio los numeros que se estan comparando 
    cambiar = True
    
    while diferencia > 1 or cambiar:
        diferencia = max(1, int(diferencia / 1.25))  
        # La diferencia minima es 1
        # En cada iteración vamos bajando la diferencia
        cambiar = False
        for i in range(largo - diferencia):
            j = i+diferencia 
            # Ubico el número que está a la distancia x de i
            if vectorcombsort[i] > vectorcombsort[j]:
                vectorcombsort[i], vectorcombsort[j] = vectorcombsort[j], vectorcombsort[i]
                # Intercambio de los numeros
                cambiar = True
    
    print("El vector ordenado con comb es: ",vectorcombsort)
#-----------------------------------------------------------------------------------------------------------------------
def cocktailsort(vectorcocktailsort):
    """Esta función ordenara el vector que le pases como argumento
    con el metodo de Cocktail Sort"""
    
    print("----------------------------------------------------------------------")
    # La lista obtenida al principio (Desordenada)
    print("El vector a ordenar con cocktail es:",vectorcocktailsort)
    
    largo = 0 # Establecemos un contador del largo
    
    for _ in vectorcocktailsort:
        largo += 1 # Obtenemos el largo del vector
    
    for i in range(largo//2): # Comenzamos desde la mitad aprox
        cambiar = False 
        # Declaramos la variable que indica si es necesario intercambiar o no 
        for j in range(1+i, largo-i):
            # Probar si los dos elementos están en el orden incorrecto
            if vectorcocktailsort[j] < vectorcocktailsort[j-1]:
                # Entonces ambos elementos cambian de lugar
                vectorcocktailsort[j], vectorcocktailsort[j-1] = vectorcocktailsort[j-1], vectorcocktailsort[j]
                cambiar = True
        # Si no ocurren cambios salimos del bucle
        if not cambiar:
            break
        cambiar = False
        for j in range(largo-i-1, i, -1):
            # Probar si los dos elementos están en el orden incorrecto
            if vectorcocktailsort[j] < vectorcocktailsort[j-1]:
                # Entonces ambos elementos cambian de lugar
                vectorcocktailsort[j], vectorcocktailsort[j-1] = vectorcocktailsort[j-1], vectorcocktailsort[j]
                cambiar = True
        if not cambiar:
            break
    print("El vector ordenado con cocktail es: ",vectorcocktailsort)
    print("----------------------------------------------------------------------")

#--------------------------------------------------------------------
#RadixSort

def countingSort(vectoradixsort,place):
    size   = len(vectoradixsort)
    output = [0] * size 
    count  = [0] * 10
    # Calculo de los elementos contables 
    for i in range(0,size):
        index = vectoradixsort[i] // place
        count [index % 10] += 1
    
    # Calculo de la cuenta acumilativa
    for i in range(1,10):
        count[i] += count[i - 1]
    
    # Colocar el elemento en el orden sorteado 
    i = size - 1
    while i >= 0:
        index = vectoradixsort[i] // place
        output[count[index % 10] - 1] = vectoradixsort[i]
        count[index % 10] -= 1
        i -= 1
    
    for i in range(0,size):
        vectoradixsort[i] = output[i]

#Funcion principal
def radixSort(vectoradixsort):
    """Esta función ordenara el vector que le pases como argumento
    con el metodo de Radix Sort"""
    print("----------------------------------------------------------------------")
    print("El vector a ordenado con RadixSort es :",vectoradixsort)
    
    #Obtener el elemento maximo
    max_element = max(vectoradixsort)
    
    # Aplicar el counting sort para acomodar los elementos en base a su valor 
    place = 1
    while max_element // place > 0:
        countingSort(vectoradixsort,place)
        place *= 10
        
radixSort(vectoradixsort)
#--------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
bubblesort(vectorbsort)
selectionsort(vectorselectsort)
insertionsort(vectorinsort)
shellsort(vectorshellsort)
mergesort(vectormergesort)
quicksort(vectorquicksort)
heapsort(vectorheapsort)
combsort(vectorcombsort)
cocktailsort(vectorcocktailsort)
radixSort(vectoradixsort)