from os import name
from os import system

os_type = name

def es_primo(num, n=2):
    if n >= num:
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        return False

def generar_Xcantidad_numeros_primos(cantidad):
    numero_evaluado = 2
    contador = 0
    salida = []

    try:
        while contador < cantidad:
            response = es_primo(numero_evaluado)
            if response:
                salida.append(numero_evaluado)
                contador = contador + 1
            numero_evaluado = numero_evaluado + 1
    except Exception as error:
        print(f"Error2: \n  {error=} \n  {type(error)=}")

    print(' '.join(str(i) for i in salida))
    print(f'{len(salida)} números primos desde 2 hasta {numero_evaluado - 1}')
    if os_type == 'nt':
        system('pause')

def preguntar_cantidad():
    if(os_type == 'posix'):
        system('clear')
    else:
        system('cls')
    print('¿Cuántos números primos quieres generar desde el 2?')

    try:
        cantidad = int(input('Cantidad de números primos: '))
        if cantidad > 0 :
            generar_Xcantidad_numeros_primos(cantidad)
        else:
            print('La cantidad debe ser ℕ (número natural)')
    except Exception as error:
        print(f"Error1: \n  {error=} \n  {type(error)=}")

preguntar_cantidad()
