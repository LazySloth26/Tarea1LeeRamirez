
# ERR7 (-5)
# ERR11
# Se crea una función que realiza las operaciones según el número de operación ingresado
def basic_ops_auxiliar(x, y, operation):
    if operation == 1:  # Si se envía un 1 al parámetro operation, realiza una suma
        result = x + y
        return result
    elif operation == 2:  # Si se envía un 1 al parámetro operation, realiza una resta
        result = x - y
        return result
    elif operation == 3:  # Si se envía un 1 al parámetro operation, realiza una AND
        result = x & y
        return result
    elif operation == 4:  # Si se envía un 1 al parámetro operation, realiza una OR
        result = x | y
        return result


def error_handling(x, operation):  # Esta funcion maneja los errores que se puedan producir en el array_ops
    '''Esta función devuelve las operaciones básicas.
    Además, tiene un código especial de errores detallados a continuación:
    ENADV = Error no se aceptan decimales en las variables matemáticas.
    ENACV = Error no se aceptan caracteres en las variables matemáticas.
    EFDRV = Error fuera de rango las variables matemáticas.
    ENADOP = Error no se aceptan decimales en la operación.
    ENACOP = Error no se aceptan caracteres en la operación.
    EFDROP = Error fuera de rango la operación.
    ELDT = Error lista de diferente tamaño.
    '''

    '''if len(x) != len(y):  # Revisa que sean del mismo tamaño
        raise TypeError('ELDT: Por favor ingrese listas del mismo tamaño.')  # levanta el error si son diferentes
    else:'''
    for i in x:  # Revisa cada instancia de la lista
        if isinstance(i, float):  # Pregunta si es float
            raise TypeError("ENADV: Por favor ingrese solamente números enteros, no se aceptan decimales")
        if not isinstance(i, int):  # Pregunta si NO es un integer/entero
            raise TypeError("ENACV: Por favor ingrese solamente números enteros, no se aceptan caracteres")
        if i not in range(-127, 128):  # Pregunta si NO están en el rango aceptado
            raise ValueError("EFDRV: Por favor ingrese números dentro del rango [-127,127]")

        # Errores para el valor de operation
        if isinstance(operation, float):  # Pregunta si operation es un float
            raise TypeError("ENADOP: Por favor ingrese solo valores enteros en la selección de la operación, no se aceptan decimales")
        if not isinstance(operation, int):  # Pregunta si operation NO es un int
            raise TypeError("ENACOP: Por favor ingrese solo valores enteros en la selección de la operación, no se aceptan letras")
        if operation not in range(1, 5):  # Pregunta si operation está en el rango aceptado
            raise ValueError("EFDROP: Por favor ingrese una operación en el rango aceptado [1,4]")  # Error en caso de que ingrese un número sin operación asignada

    '''for j in y:
        if isinstance(j, float):  # Pregunta si es float
            raise TypeError("ENADV: Por favor ingrese solamente números enteros, no se aceptan decimales")
        if not isinstance(j, int):  # Pregunta si NO es un int
            raise TypeError("ENACV: Por favor ingrese solamente números enteros, no se aceptan caracteres")
        if j not in range(-127, 128):  # Pregunta si NO están en el rango aceptado
            raise ValueError("EFDRV: Por favor ingrese números dentro del rango [-127,127]")

        # Errores para el valor de operation
        if isinstance(operation, float):  # Pregunta si operation es un float
            raise TypeError("ENADOP: Por favor ingrese solo valores enteros en la selección de la operación, no se aceptan decimales")
        if not isinstance(operation, int):  # Pregunta si operation NO es un int
            raise TypeError("ENACOP: Por favor ingrese solo valores enteros en la selección de la operación, no se aceptan letras")
        if operation not in range(1, 5):  # Pregunta si operation está en el rango aceptado
            raise ValueError("EFDROP: Por favor ingrese una operación en el rango aceptado [1,4]")  # Error en caso de que ingrese un número sin operación asignada
'''


class operations:
    def __init__(self):
        pass

    def basic_ops(self, x, y, operation):
        '''Esta función devuelve las operaciones básicas.
        Además, tiene un código especial de errores detallados a continuación:
        ENADV = Error no se aceptan decimales en las variables matemáticas.
        ENACV = Error no se aceptan caracteres en las variables matemáticas.
        EFDRV = Error fuera de rango las variables matemáticas.
        ENADOP = Error no se aceptan decimales en la operación.
        ENACOP = Error no se aceptan caracteres en la operación.
        EFDROP = Error fuera de rango la operación.
        '''

        # El isinstance pregunta si el parámetro es o no de cierto tipo
        # Errores para las variables matemáticas
        if isinstance(x, float) or isinstance(y, float):  # Pregunta si "x" o "y" es float
            raise TypeError("ENADV. Por favor ingrese solamente números enteros, no se aceptan decimales")
        if not isinstance(y, int):  # Pregunta si "y" NO es un int
            raise TypeError("ENACV. Por favor ingrese solamente números enteros, no se aceptan caracteres")
        if x not in range(-127, 128) or y not in range(-127, 128):  # Pregunta si "x" o "y" NO están en el rango aceptado
            raise ValueError("EFDRV. Por favor ingrese números dentro del rango [-127,127]")

        # Errores para el valor de operation
        if isinstance(operation, float):  # Pregunta si operation es un float
            raise TypeError("ENADOP. Por favor ingrese solo valores enteros en la selección de la operación, no se aceptan decimales")
        if not isinstance(operation, int):  # Pregunta si operation NO es un int
            raise TypeError("ENACOP. Por favor ingrese solo valores enteros en la selección de la operación, no se aceptan letras")
        if operation not in range(1, 5):  # Pregunta si operation está en el rango aceptado
            raise ValueError("EFDROP. Por favor ingrese una operación en el rango aceptado [1,4]")  # Error en caso de que ingrese un número sin operación asignada

        print("El resultado de la operación es:", basic_ops_auxiliar(x, y, operation))  # Imprime el resultado de la operación solicitada

    def array_ops(self, x, y, operation):  # recibe dos arreglos y realiza operaciones con dichos arreglos
        temp = True  # condicion para el ciclo while
        cont = 0  # se le asigna un valor inicial al contador
        z = []  # se inicializa un arreglo para almacenar los resultados de las operaciones

        if len(x) != len(y):  # Revisa que sean del mismo tamaño
            raise TypeError('ELDT: Por favor ingrese listas del mismo tamaño.')  # levanta el error si son diferentes
        else:
            error_handling(x, operation)  # llama la funcion que maneja los errores a verificar en array_ops
            error_handling(y, operation)  # se analizan errores por separado para evitar errores de complejidad en flake8

        while (temp):  # inicia el ciclo para pasar por cada instancia de las listas
            aux1 = x[cont]  # asigna a una variable los valores de la lista uno por uno, cambia de instancia con cada ciclo hasta que se interrumpe el while
            aux2 = y[cont]

            z.append(basic_ops_auxiliar(aux1, aux2, operation))  # agrega cada resultado de basic_ops a la lista del resultado

            cont += 1  # aumenta el contador que genera el avance en las listas
            if cont == len(x):  # verifica que el contador no se pase del tamaño de las listas
                temp = False  # si es igual termina el ciclo

        print('El resultado de la operación es: ', z)  # aunque no es necesario puede que le simplifique la revisión del código
        return z  # retorna el resultado de las operaciones
