import json
import os
import xml.etree.ElementTree as ET

def processarJson(caminhoArquivo):
    try:
        with open(caminhoArquivo, 'r') as file:
            dados = json.load(file)

        faturamento = [item['valor'] for item in dados]

        if not faturamento:
            raise ValueError("Nenhum dado de faturamento encontrado.")

        faturamento = [dia for dia in faturamento if dia > 0]

        if not faturamento:
            raise ValueError("Todos os valores de faturamento são zero.")

        menorValor = min(faturamento)
        maiorValor = max(faturamento)

        mediaMensal = sum(faturamento) / len(faturamento)

        diasAcimaDaMedia = sum(1 for dia in faturamento if dia > mediaMensal)

        print(f"Menor valor de faturamento: {menorValor}")
        print(f"Maior valor de faturamento: {maiorValor}")
        print(f"Dias com faturamento acima da média: {diasAcimaDaMedia}")

    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho do arquivo.")
    except json.JSONDecodeError:
        print("Erro ao decodificar o arquivo JSON. Verifique a sintaxe.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def processarXml(caminhoArquivo):
    try:
        tree = ET.parse(caminhoArquivo)
        root = tree.getroot()

        faturamento = []
        for row in root.findall('row'):
            valor = float(row.find('valor').text)
            faturamento.append(valor)

        faturamento = [dia for dia in faturamento if dia > 0]

        if not faturamento:
            raise ValueError("Todos os valores de faturamento são zero.")

        menorValor = min(faturamento)
        maiorValor = max(faturamento)

        mediaMensal = sum(faturamento) / len(faturamento)

        diasAcimaDaMedia = sum(1 for dia in faturamento if dia > mediaMensal)

        print(f"Menor valor de faturamento: {menorValor}")
        print(f"Maior valor de faturamento: {maiorValor}")
        print(f"Dias com faturamento acima da média: {diasAcimaDaMedia}")

    except FileNotFoundError:
        print("Arquivo XML não encontrado. Verifique o caminho do arquivo.")
    except ET.ParseError:
        print("Erro ao analisar o arquivo XML. Verifique a sintaxe.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def main():
    escolha = input("Escolha a base de dados (1 - JSON, 2 - XML): ")
    if escolha == '1':
        caminhoArquivo = os.path.join("dados", "dados.json")
        processarJson(caminhoArquivo)
    elif escolha == '2':
        caminhoArquivo = os.path.join("dados", "dados.xml")
        processarXml(caminhoArquivo)
    else:
        print("Escolha inválida. Por favor, selecione 1 ou 2.")

if __name__ == "__main__":
    main()
