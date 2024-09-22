# Primeiro desafio
def validarIndice(indice: int):
    if indice <= 0:
        raise ValueError("O valor de INDICE deve ser maior que zero.")

def calcularSoma(indice: int):
    try:
        validarIndice(indice)

        soma = 0
        k = 0
        
        while k < indice:
            k += 1
            soma += k

        print(f"SOMA calculada: {soma}")
        return soma

    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

calcularSoma(13)

