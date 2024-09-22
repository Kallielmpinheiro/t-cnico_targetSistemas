def calcularPercentuais(faturamento):
    if not faturamento:
        raise ValueError("Nenhum dado de faturamento encontrado.")
    
    total = sum(faturamento.values())
    
    if total == 0:
        raise ValueError("O total de faturamento é zero, não é possível calcular percentuais.")
    
    for estado, valor in faturamento.items():
        percentual = (valor / total) * 100
        print(f"{estado}: {percentual:.2f}%")

def main():
    try:
        faturamento = {
            "SP": 67836.43,
            "RJ": 36678.66,
            "MG": 29229.88,
            "ES": 27165.48,
            "Outros": 19849.53
        }
        calcularPercentuais(faturamento)

    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()
