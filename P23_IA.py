x = 0

while x < 30:
    x += 1
    if x == 15:
        print("se rompió la ejecución dle bucle cuano x valía ", x)
        break
    if x == 4 or x == 6 or x == 10:
        continue
    print(x)
    
print("Se saltaron los valores 4, 6 y 10 del bucle de x")