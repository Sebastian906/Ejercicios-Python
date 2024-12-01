def sumatoria(limite, num1, num2):
    sum = 0
    for i in range(limite):
        if i % num1 == 0 or i % num2 == 0:
            sum += i
    return sum

limite = int(input("Ingresa el límite: "))
numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

resultado = sumatoria(limite, numero1, numero2)
print(resultado)
