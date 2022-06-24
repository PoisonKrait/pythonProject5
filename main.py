import operaciones
import time

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

hora = time.strftime('%H')
minutos = time.strftime('%M')

if int(hora) >= 19:
    print ("Es hora de irse a casa")
else:
    print ("Quedan {} horas y {} minutos para irnos a casa".format(18- int(hora), 59-int(minutos)))