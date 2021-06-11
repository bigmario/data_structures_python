from stacks.stacks import Stack

def run():
    pila = Stack()

    pila.push('egg')
    pila.push('ham')
    pila.push('spam')

    print(pila.pop())
    print(pila.peek())
    pila.clear()
    print(pila.peek())

    [pila.push(i) for i in range(1, 10)]
    print(pila.peek())

    for i in range(pila.len()):
        print(pila.pop())

if __name__ == '__main__':
    run()