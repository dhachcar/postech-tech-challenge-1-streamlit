import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patheffects as pe
import pandas as pd
import seaborn as sns
import global_config


def plot_linha_consolidado(df: pd.DataFrame, col: str, ylabel: str, title: str = None, top: int = 5, xlabel: str = 'País', legend: bool = False, grid: bool = False, escala_y=250_000):
    ordenados = df.sort_values(by=col, ascending=False)
    paises = ordenados.pais.unique()[:top]
    top5 = ordenados.query('pais in @paises')

    plt.figure(figsize=(12, 8))

    ax = sns.lineplot(data=top5, x=top5.ano, y=col, hue='pais',
                      palette='tab10', linewidth=2, marker='o')
    ax.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.2f}'))
    ax.set_xlabel(xlabel, fontdict=global_config.fontconfig,
                  labelpad=global_config.padding)
    ax.set_ylabel(ylabel, fontdict=global_config.fontconfig,
                  labelpad=global_config.padding)

    # adiciona um label ao ponto mais alto de cada ano
    for x, y in zip(df.ano, df[col]):
        maior_por_ano = df.query(f'ano == {x}').max()[col]

        if (y == maior_por_ano):
            plt.text(
                x=x,
                # posiciona o label um pouco acima do ponto (considerando a escala em milhões do eixo Y)
                y=y + escala_y,
                s='{:,.2f}'.format(y),
                color='#000',
                path_effects=[pe.withStroke(linewidth=1.5, foreground="#ccc")],
                fontsize=7,
                rotation=10
            )

    if (title != None):
        ax.set_title(title, fontdict=global_config.fontconfig,
                pad=global_config.padding)

    if (grid):
        plt.grid(color='#ccc', linestyle='dashed', linewidth=1)

    if (legend):
        leg = plt.legend(title='País', loc='upper left', bbox_to_anchor=(
            1, 1), title_fontproperties=global_config.fontconfig)

        # espessura da linha, dentro da legenda
        for obj in leg.legend_handles:
            obj.set_linewidth(2)

    plt.ylim(0, top5[col].max() + top5[col].max() * 0.05)
    plt.box(False)

    plt.show()
