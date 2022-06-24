import operaciones

def main():
    Suma = operaciones.sumar(a=float(input('Introduce el primer numero: ')),
                             b= float(input('Introduce el segundo numero: ')))

    print('El valor de la suma es: ', Suma)

    Resta = operaciones.restar(c=float(input('Introduce el primer numero: ')),
                             d= float(input('Introduce el segundo numero: ')))

    print('El valor de la resta es: ', Resta)

    Multiplicar = operaciones.multiplicar(e=float(input('Introduce el primer numero: ')),
                             f= float(input('Introduce el segundo numero: ')))

    print('El valor de la multiplicacion es: ', Multiplicar)




if __name__ == '__main__':
    main()
else: pass