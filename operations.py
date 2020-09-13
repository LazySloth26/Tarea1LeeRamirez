
# Se crea una función que realiza las operaciones según el número de operación ingresado
def basic_ops_auxiliar(x, y, operation):
    if operation == 1: # Si se envía un 1 al parámetro operation, realiza una suma
        result = x + y
        return result
    elif operation == 2: # Si se envía un 1 al parámetro operation, realiza una resta
        result = x - y
        return result
    elif operation == 3: # Si se envía un 1 al parámetro operation, realiza una AND
        result = x & y
        return result
    elif operation == 4: # Si se envía un 1 al parámetro operation, realiza una OR
        result = x | y
        return result

class operations:
    def __init__(self):
        pass
    def basic_ops(self, x, y, operation):
        '''Esta función devuelve las operaciones básicas.
        Además, tiene un código especial de errores detallados a continuación:
        ENADV = Error no se aceptan decimales en las variables matemáticas
        ENACV = Error no se aceptan caracteres en las variables matemáticas
        EFDRV = Error fuera de rango las variables matemáticas
        ENADOP = Error no se aceptan decimales en la operación
        ENACOP = Error no se aceptan caracteres en la operación
        EFDROP = Error fuera de rango la operación
        '''

        # El isinstance pregunta si el parámetro es o no de cierto tipo
        # Errores para las variables matemáticas
        if isinstance(x, float) or isinstance(y, float): # Pregunta si "x" o "y" es float
            raise TypeError("ENADV. Por favor ingrese solamente números enteros, no se aceptan decimales")
        if not isinstance(y, int):# Pregunta si "y" NO es un int
            raise TypeError("ENACV. Por favor ingrese solamente números enteros, no se aceptan caracteres")
        if x not in range(-127, 128) or y not in range(-127, 128):# Pregunta si "x" o "y" NO están en el rango aceptado
            raise ValueError("EFDRV. Por favor ingrese números dentro del rango [-127,127]")

        # Errores para el valor de operation
        if isinstance(operation, float): # Pregunta si operation es un float
            raise TypeError("ENADOP. Por favor ingrese solo valores enteros en la selección de la operación, no se aceptan decimales")
        if not isinstance(operation, int): # Pregunta si operation NO es un int
            raise TypeError("ENACOP. Por favor ingrese solo valores enteros en la selección de la operación, no se aceptan letras")
        if operation not in range(1, 5): # Pregunta si operation está en el rango aceptado
            raise ValueError("EFDROP. Por favor ingrese una operación en el rango aceptado [1,4]") # Error en caso de que ingrese un número sin operación asignada

        print("El resultado de la operación es:", basic_ops_auxiliar(x, y, operation)) # Imprime el resultado de la operación solicitada
