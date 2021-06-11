from queues.list_based_queue import ListQueue
from queues.stack_based_queue import Queue as stackQueue
from queues.node_based_queue import Queue as nodeQueue

def run():
    #LIST BASED
    print('LIST BASED')
    x = ListQueue()
    x.enqueue('eegs')
    x.enqueue('ham')
    x.enqueue('spam')
    x.items

    for i in range(x.size):
        print(x.items[i])

    #STACK BASED
    print('\nSTACK BASED')
    y = stackQueue()
    y.enqueue(5)
    y.enqueue(6)
    y.enqueue(7)
    print(y.inbound_stack)
    y.dequeue()
    print(y.inbound_stack)
    print(y.outbound_stack)
    y.dequeue()
    print(y.outbound_stack)

    
    #NODE BASED
    print('\nNODE BASED')

    z = nodeQueue()
    z.enqueue('eggs')
    z.enqueue('ham')
    z.enqueue('spam')
    print(z.head.data)
    print(z.head.next.data)
    print(z.tail.data)
    print(z.count)
    z.dequeue()
    print(z.head.data)

if __name__ == '__main__':
    run()