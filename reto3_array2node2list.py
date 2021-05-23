from listas_enlazadas.single_linked_list import SinglyLinkedList
from arreglos.arrays import Array
import random

def run():
    """
    Se genera el array de tamaño 'size', cuyos elementos 
    se convertiran en un alista enlazada
    """
    size = int(input('Ingrese el tamaño del arreglo a convertir: '))
    arreglo = Array(size)

    # se agregan elementos aleatorios al array
    [arreglo.__setitem__(i,random.randint(0, 10)) for i in range(arreglo.__len__())]

    print(f'Array => {arreglo}') # mostramos el arreglo

    
    lista = SinglyLinkedList() #se instancia la lista enlazada que recibira los elementos del array

    for elemento in arreglo:
        lista.append(elemento)
    
    current = lista.tail

    print("Lista enlazada => ", end="")
    
    while current:
        print(f"[{current.data}]", end=",") # se muestra, elemento a elemento, la nueva lista enlazada
        current = current.next


if __name__ == '__main__':
    run()