def pertenceFibonacci(numero):
    if numero < 0:
        raise ValueError("O número deve ser não negativo.")
    a, b = 0, 1
    while b <= numero:
        if b == numero:
            return True
        a, b = b, a + b
    return False

try:
    numero = int(input("Informe um número: "))
    if pertenceFibonacci(numero):
        print(f"{numero} pertence à sequência de Fibonacci.")
    else:
        print(f"{numero} não pertence à sequência de Fibonacci.")
except ValueError as e:
    print(e)
