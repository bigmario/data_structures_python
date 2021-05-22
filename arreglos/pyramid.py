"""
acumula recursivamente la sumatoria desde 'lower' hasta 'upper', almacenada
en 'result', mostrando primero el valor de lower en cada iteracion o llamada recursiva y
cuando 'lower' supera a 'upper' va mostrando los valores acumulados de 'result'
en cada cada iteracion
"""

def pyramid_sum(lower, upper, margin=0):
    blanks = " " * margin
    print(blanks, lower, upper)
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + pyramid_sum(lower+1, upper, margin +4)
        print(blanks, result)
        return result

pyramid_sum(2,6)