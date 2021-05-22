from arreglos.cube import Cube
from arreglos.arrays import Array
from arreglos.grids import Grid

def arregloReto():
    size = int(input('Ingrese el tamaño del arreglo: '))
    arreglo = Array(size)
    print('Longitud del arreglo:\n', arreglo.__len__())
    print('Arreglo sin datos iniciales:\n',arreglo.__str__())
    [arreglo.__setitem__(i,i+1) for i in range(arreglo.__len__())]
    print('Arreglo con datos secuenciales:\n', arreglo.__str__())
    arreglo.__randReplace__()
    print('Arreglo con datos al azar:\n', arreglo.__str__())
    print('Sumatoria del arreglo:\n', arreglo.__sum__() )

def gridReto():
    matrix = Grid(3, 3)
    print(matrix)
    for row in range(matrix.get_height()):
        for column in range(matrix.get_width()):
            matrix[row][column] = row * column

    print(matrix)
    print(matrix.get_height())
    print(matrix.get_width())
    print(matrix.__getitem__(1))
    print(matrix.__getitem__(2)[0])
    print(matrix.__str__())

def cubeReto():
    cubo = Cube(3,3,3)
    
    for row in range(cubo.get_height()):
        for column in range(cubo.get_width()):
            for depth in range(cubo.get_depth()):
                cubo[row][column][depth] = f'[fila {row}, columna {column}, casilla {depth}]'
    
    print(cubo)

def run():
    cubeReto()

if __name__ == '__main__':
    run()