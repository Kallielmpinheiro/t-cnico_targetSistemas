def inverterString(s):
    if not isinstance(s, str):
        raise ValueError("A entrada deve ser uma string.")
    
    stringInvertida = ""
    for i in range(len(s) - 1, -1, -1):
        stringInvertida += s[i]
    
    return stringInvertida

def main():
    try:
        entrada = input("Digite uma string para inverter (ou deixe em branco para usar uma pré-definida): ")
        if entrada == "":
            entrada = "Exemplo de string"
        
        resultado = inverterString(entrada)
        print(f"String invertida: {resultado}")

    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
