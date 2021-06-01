from nodos.node import Node
from listas_enlazadas.single_linked_list import SinglyLinkedList

def recorre_lista(mensaje=None):
    # * Recorrer e imprimir valores de la lista
    probe = head
    if mensaje!=None:
        print('')
        print(mensaje)
    else:
        pass
    while probe != None:
        print(probe.data)
        probe = probe.next

# * Creación de los nodos enlazados (linked list)
head = None
for count in range(1,6):
    head = Node(count, head)

recorre_lista("primer recorrido")

# * Busqueda de un elemento
probe = head
target_item = 9
while probe != None and target_item != probe.data:
    probe = probe.next

if probe != None:
    print(f'Target item {target_item} has been found')
else:
    print(f'Target item {target_item} has not been found')

#Reemplazo de un elemento
probe = head
target_item = 3
new_item = 'A'
while probe != None and target_item != probe.data:
    probe = probe.next
if probe != None:
    probe.data = new_item
    print(f'Target item {target_item} has been replaced with {new_item}')
    recorre_lista()
else:
    print(f'Target item {target_item} has not been found')
    recorre_lista()



# * Insertar un nuevo elemento/nodo al inicio(head)
head = Node("F", head)

recorre_lista('insertado F al inicio')

# * Insertar un nuevo elemento/nodo al final(tail)
new_node = Node("K")
if head is None:
    head = new_node
else:
    probe = head
    while probe.next != None:
        probe = probe.next
    probe.next = new_node

recorre_lista('insertado K al final')

# * Eliminar un elmento/nodo al inicio(head)
removed_item = head.data
head = head.next

recorre_lista(f'Eliminado elemento {removed_item} en el inicio')

# * Eliminar un elmento/nodo al final(tail)
removed_item = head.data
if head.next is None:
    head = None
else:
    probe = head
    while probe.next.next != None:
        probe = probe.next
    removed_item = probe.next.data
    probe.next = None

recorre_lista(f'Eliminado elemento {removed_item} al final')

# * Agregar un nuevo elemento/nodo por "indice" inverso(Cuenta de Head - Tail)
new_item = input("Enter new item: ")
index = int(input("Enter the position to insert the new item: "))
index2=index

if head is None or index <= 0:
    head = Node(new_item, head)
else:
    probe = head
    while index > 1 and probe.next != None:
        probe = probe.next
        index -= 1
    probe.next = Node(new_item, probe.next)

recorre_lista(f'Agregado elemento {new_item} en posicion {index2}')

# * Eliminar un nuevo elemento/nodo por "indice" inverso(Cuenta de Head - Tail)
index = 3
index2=index

if head is None or index <= 0:
    removed_item = head.data
    head = head.next
    print(removed_item)
else:
    probe = head
    while index > 1 and probe.next.next != None:
        probe = probe.next
        index -= 1
    removed_item = probe.next.data
    probe.next = probe.next.next

recorre_lista(f'ELiminado elemento {removed_item} en posicion {index2}')

# ********* TO-DO ***************#

#PENDIENTE: REFACTOR A ESTE CODIGO PARA ELIMINAR CODIGO REDUNDANTE
#PENDIENTE: CREAR  UNA LISTA CIRCULAR - EL ULTIMO NODO (TAIL) APUNTA AL PRIMERO (HEAD)
#PENDIENTE: CREAR  UNA LISTA CIRCULAR DOBLEMENTE ENLAZADA DE 5 NODOS
#PENDIENTE: AGREGAR LOS METODOS DE LA LISTA ENLAZADA SIMPLE A ESTA LISTA CIRCULAR DOBLEMENTE ENLAZADA


