import math

def area_circulo(radio):
    '''
    (num) -> float

    >>> area_circulo(1)
    3.141592653589793

    >>> area_circulo(3)
    9.42477796076938

    :param radio: num que representa el radio del circulo
    :return: float que representa el area del circulo
    '''

    area = radio * math.pi
    return area

def perimetro_trangulo(ladoA, ladoB, ladoC):
    '''
    (num) -> float

    calcular el perimetro de un triagulo segun sus lados

    >>> perimetro_trangulo(2, 2, 2)
    6

    >>> perimetro_trangulo(3, 8, 6,)
    17

    :param ladoA: num que representa un lado del triangulo
    :param ladoB: num que representa un lado del triangulo
    :param ladoC: num que representa un lado del triangulo
    :return: float que representa el perimetro de un triangulo
    '''

    perimetro = ladoA + ladoB + ladoC

    return perimetro

def semi_perimetro_trinagulo(ladoA, ladoB, ladoC):
    '''
    (num) -> float

    calcular semi perimetro del triangulo

    >>> semi_perimetro_trinagulo(2, 6, 4)
    6.0

    >>> semi_perimetro_trinagulo(3, 4, 1)
    4.0

    :param ladoA:
    :param ladoB:
    :param ladoC:
    :return:
    '''

    return perimetro_trangulo(ladoA, ladoB, ladoC) / 2

def area_triangulo(ladoA, ladoB, ladoC):
    '''
    (unm) -> float

    area del triangulo formula de heron

    >>> area_triangulo(4, 5, 3)
    6.0

    >>> area_triangulo(6, 7, 2)
    5.562148865321747

    :param ladoA:
    :param ladoB:
    :param ladoC:
    :return:
    '''

    semiperimetro = semi_perimetro_trinagulo(ladoA, ladoB, ladoC)
    valor = semiperimetro * (semiperimetro - ladoA) * (semiperimetro - ladoB) * (semiperimetro - ladoC)

    area = math.sqrt(valor)

    return area

def es_impar(numero):
    '''
    (num) -> boleano

    >>> es_impar(2)
    False

    >>> es_impar(3)
    True

    :param numero:
    :return:
    '''

    numeroinmpar = (numero % 2) != 0

    return numeroinmpar

def es_par(numero):
    '''
    (num) -> boleano

    >>> es_par(2)
    True

    >>> es_par(3)
    False

    :param numero:
    :return:
    '''

    numeropar = not(es_impar(numero))

    return  numeropar

def es_vocal(letra):
    '''
    str(1) -> boleano

    >>> es_vocal('o')
    True

    >>> es_vocal('b')
    False

    :param letra:
    :return:
    '''

    esVocal = len(letra) == 1 and letra in 'aeiouAEIOU'

    return esVocal

def area_sombreada(radio):
    '''
    (num) -> float

    Determina el area sombreada

    >>> area_sombreada(5)
    -34.29203673205103

    >>> area_sombreada(2)
    -1.7168146928204138

    :param radio:
    :return:
    '''

    areaDelCirculo = area_circulo(radio)
    areaDelCuadro = 2*radio**2

    areaSombreada = areaDelCirculo - areaDelCuadro

    return areaSombreada
