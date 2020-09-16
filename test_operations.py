import operations
import pytest

###### PRUEBAS PARA FUNCIÓN BASIC_OPS ######

# Test para cada caso de éxito de las operaciones disponibles
def test_suma(capsys): ##Suma
    basic_ops = operations.operations # Llama el init de la clase operations y crea el objeto
    basic_ops.basic_ops(basic_ops,1,2,1) # Llama la función a probar, pide el self
    out, err = capsys.readouterr()  # Inputs y outputs de la función,los outputs salen en orden
    assert out == "El resultado de la operación es: 3\n" # Se imprime el resultado que debe dar

def test_resta(capsys): ##Resta
    basic_ops = operations.operations
    basic_ops.basic_ops(basic_ops,1,2,2)
    out, err = capsys.readouterr()
    assert out == "El resultado de la operación es: -1\n"

def test_AND(capsys): ##AND
    basic_ops = operations.operations
    basic_ops.basic_ops(basic_ops,1,2,3)
    out, err = capsys.readouterr()
    assert out == "El resultado de la operación es: 0\n"

def test_OR(capsys): ##OR
    basic_ops = operations.operations  #
    basic_ops.basic_ops(basic_ops,1,2,4)
    out, err = capsys.readouterr()
    assert out == "El resultado de la operación es: 3\n"


'''def test_list_size(capsys): #Para los tamaños de las listas ingresadas
    array_ops = operations.operations
    with pytest.raises(Exception) as context: # El raise de la excepción se guarda en el context
        array_ops(array_ops, [1, 2, 3], [3, 2, 1], 1) # Se ingresan las listas en una de las variables numéricas
        assert "ELDT" in context # Se hace un assert para verificar que el código de la excepción está en el context'''

# basic ops tests
# Test para cuando se ingresan decimales
def test_a_decimal_V(capsys): ## Para las variables numéricas
    basic_ops = operations.operations
    with pytest.raises(Exception) as context: # El raise de la excepción se guarda en el context
        basic_ops(basic_ops, 1.5, 2, 1) # Se ingresa el valor decimal en una de las variables numéricas
        assert "ENADV" in context # Se hace un assert para verificar que el código de la excepción está en el context

def test_a_decimal_OP(capsys): ## Para el valor de operation
    basic_ops = operations.operations #
    with pytest.raises(Exception) as context:
        basic_ops(basic_ops, 1, 2, 1.5) # Se ingresa el valor decimal en la operación
        assert "ENADOP" in context

# Test para cuando se ingresan caracteres
def test_a_character_V(capsys):  ## Para las variables numéricas
    basic_ops = operations.operations
    with pytest.raises(Exception) as context:
        basic_ops(basic_ops, 1, F, 1)  # Se ingresa el caracter en una de las variables numéricas
        assert "ENACV" in context

def test_a_character_OP(capsys):
    basic_ops = operations.operations ## Para el valor de operation
    with pytest.raises(Exception) as context:
        basic_ops(basic_ops, 1, 2, H)  # Se ingresa el caracter en la operación
        assert "ENACOP" in context


# Test para cuando se ingresan valores fuera de rango
def test_a_range_V(capsys):  ## Para las variables numéricas
    basic_ops = operations.operations
    with pytest.raises(Exception) as context:
        basic_ops(basic_ops, 150, 2, 1) # Se ingresa el valor fuera de rango en la variable numérica
        assert "EFDRV" in context

def test_a_range_OP(capsys):
    basic_ops = operations.operations ## Para el valor de operation
    with pytest.raises(Exception) as context:
        basic_ops(basic_ops, 1, 2, 150) # Se ingresa el valor fuera de rango en la operación
        assert "EFDROP" in context




#array ops tests
def test_a_decimal_V_array(capsys): ## Para las variables numéricas
    array_ops = operations.operations
    with pytest.raises(Exception) as context: # El raise de la excepción se guarda en el context
        array_ops(array_ops, [1.5, 2, 3], [3, 2, 1], 1) # Se ingresa el valor decimal en una de las variables numéricas
        assert "ENADV" in context # Se hace un assert para verificar que el código de la excepción está en el context

def test_a_decimal_OP_array(capsys): ## Para el valor de operation
    array_ops = operations.operations
    with pytest.raises(Exception) as context:
        array_ops(array_ops, [1, 2, 3], [3, 2, 1], 1.5) # Se ingresa el valor decimal en la operación
        assert "ENADOP" in context

def test_a_character_V_array(capsys):  ## Para las variables numéricas
    array_ops = operations.operations
    with pytest.raises(Exception) as context:
        array_ops(array_ops, [1, 2, 3], [F, 2, 3], 1)  # Se ingresa el caracter en una de las variables numéricas
        assert "ENACV" in context

def test_a_character_OP_array(capsys):
    array_ops = operations.operations ## Para el valor de operation
    with pytest.raises(Exception) as context:
        array_ops(array_ops, [1, 2, 3], [3, 2, 1], H)  # Se ingresa el caracter en la operación
        assert "ENACOP" in context

#Test que revisa el rango de los datos que se ingresan
def test_a_range_V_array(capsys):  ## Para las variables numéricas
    array_ops = operations.operations
    with pytest.raises(Exception) as context:
        array_ops(array_ops, [150, 2, 3], [3, 2, 1], 1) # Se ingresa el valor fuera de rango en la variable numérica
        assert "EFDRV" in context

def test_a_range_OP_array(capsys):
    array_ops = operations.operations ## Para el valor de operation
    with pytest.raises(Exception) as context:
        array_ops(array_ops, [1, 2, 3], [3, 2, 1], 150) # Se ingresa el valor fuera de rango en la operación
        assert "EFDROP" in context
