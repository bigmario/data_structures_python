from listas_enlazadas.node import Node

def run():
    print('**** Forma Manual *****')
    nodo3 = Node("C", None)
    nodo2 = Node("B", nodo3)
    nodo1 = Node("A", nodo2)

    print(f'nodo 1: {nodo1}', f'nodo 2: {nodo2}', f'nodo 3: {nodo3}', sep='\n')

    print('**** Forma Iterariva ****')
    head =None
    for count in range(1,5):
        head = Node(count, head)

    numero_nodo = 0
    while head != None:
        print(f'nodo {numero_nodo}: {head}', f'; data del nodo {numero_nodo}: {head.data}')
        head = head.next
        numero_nodo = numero_nodo +1

if __name__ == '__main__':
    run()
