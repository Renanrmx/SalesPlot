__author__ = 'Renanrmx'

import analysis

current_choice = 0

# Modelos de plotagem disponíveis
query_options = ['top_products', 'count_sales']

# Caminho da pasta contendo os arquivos csv para a análise
source_path = r'D:\Projetos\Programming\Anatel\SalesPlot\relatorios'


def choose_query(name):
    if name == "top_products":
        analysis.plot_top_products(source_path)
    elif name == "count_sales":
        analysis.plot_count_sales(source_path)


def select_list(options, choice):
    while choice != 'q':
        choice = input("Digite o número da posição ou um dos nomes da lista (Q para sair): ")

        if choice.isnumeric():
            index = int(choice)
            if index <= len(choice):
                choose_query(options[index])

            else:
                print("Escolha inválida: Posição fora da lista")

        else:
            if choice in options:
                choose_query(choice)
            else:
                print("Escolha inválida: Nome incorreto ou não existe na lista")


if __name__ == "__main__":
    while current_choice != 'q':
        if len(query_options) > 0:
            print(query_options)
            select_list(query_options, current_choice)
            break
        else:
            print("Lista vazia, preenche-a antes de continuar")
