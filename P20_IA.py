edad = int(input('¿Cuál es tu edad?\n'))
if edad <= 0:
	print('Nadie puede tener esa edad')
elif edad >= 1 and edad < 18:
	print('Eres menor de edad')
elif edad >= 18 and edad <= 45:
    print("Eres un adulto promedio")
elif edad >= 46 and edad <= 99:
	print('Eres mayor de edad')
elif edad >= 100 and edad <= 120:
    print("Tas muy ruco")
else:
	print('Edad no válida')