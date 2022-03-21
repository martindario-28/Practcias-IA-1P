tupla = ("rojo","azul","verde","amarillo")
color = (input('Introduzca el color que quiere saber si está admitido:\n'))
if color in tupla:
    print("El color ", color, " está admitido")
else:
    print("El color ", color, " no está admitido")