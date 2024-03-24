from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def prepare_data(source_path):
    # Importa os dados
    files = Path(source_path).glob('*.csv')
    df = pd.concat(map(pd.read_csv, files))

    # Remove linhas com valores nulos
    df.dropna(inplace=True)

    return df


def plot_top_products(source_path):
    """ Exibe os produtos mais vendidos """

    df = prepare_data(source_path)

    top_products = df.groupby('Produto', as_index=False).sum("Quantidade").sort_values(by="Quantidade", ascending=False).head(5)
    top_products.drop(['IdVenda', 'ValorUnitario'], inplace=True, axis=1)
    sns.catplot(x='Produto', y='Quantidade', data=top_products, kind='bar')
    top_products.to_csv('results/top_products.csv', index=False)

    plt.show()


def plot_count_sales(source_path):
    """ Conta o total de vendas por região """

    df = prepare_data(source_path)

    count_sales = df.groupby(['IdVenda', 'Regiao'], as_index=False).count()
    count_sales.drop(['Data', 'Vendedor', 'Produto', 'Categoria', 'Quantidade', 'ValorUnitario'], inplace=True, axis=1)
    sns.countplot(count_sales, x="Regiao")
    count_sales.to_csv('results/count_sales.csv', index=False)

    plt.show()
