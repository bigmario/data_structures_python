from listas_enlazadas.single_linked_list import SinglyLinkedList

def run():
    words = SinglyLinkedList()
    words.append('egg')
    words.append('ham')
    words.append('span')
    current = words.tail

    print('Recorrido de la lista, metodo 1 (ciclo while)')
    while current:
        print(current.data)
        current = current.next

    print('')

    print('Recorrido de la lista, metodo 2 (ciclo for)')
    for word in words.iter():
        print(word)




if __name__ == '__main__':
    run()