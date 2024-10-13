count = 0
suma = 0

while True:
  numero = int(input('Ingrese un número, para salir ingrese 0 '))
  if numero == 0:
    break
  count += 1
  suma = suma + numero


print(f'La suma de los números ingresados es {count} y el promedio es {round(suma / count,3)}' if count!= 0 else 'No se ingresaron numeros  ')