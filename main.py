import pandas as pd
import streamlit as st
import seaborn as sns
from plots.plot_bar_consolidado import plot_bar_consolidado as bar_consolidado
from plots.plot_linha_consolidado import plot_linha_consolidado as linha_consolidado


df_vinho = pd.read_csv('exports/export-vinho.csv', sep=',')
df_espumante = pd.read_csv('exports/export-espumante.csv', sep=',')
df_suco = pd.read_csv('exports/export-suco.csv', sep=',')
df_uva = pd.read_csv('exports/export-uva.csv', sep=',')

df_vinho_consolidado = pd.read_csv(
    'exports/export-vinho-consolidado.csv', sep=',')
df_espumante_consolidado = pd.read_csv(
    'exports/export-espumante-consolidado.csv', sep=',')
df_suco_consolidado = pd.read_csv(
    'exports/export-suco-consolidado.csv', sep=',')
df_uva_consolidado = pd.read_csv(
    'exports/export-uva-consolidado.csv', sep=',')

divider_color = 'blue'

sns.set_style('whitegrid', {'grid.color': '.6', 'grid.linestyle': '--'})
sns.set_context("notebook", font_scale=1, rc={"lines.linewidth": 1})
st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

st.write('# Análise de exportações de produtos')
tab0, tab1, tab2, tab3, tab4 = st.tabs(
    tabs=['Vinho', 'Espumante', 'Suco', 'Uva', 'Dados do aluno'])

with tab0:
    st.write('## Exportações de vinho')

    with st.container():
        col0, col1 = st.columns([1, 1])

        with col0:
            st.subheader(
                ':blue[TOP 15] maiores compradores de vinho (em US$) nos últimos :blue[15 anos] :bar_chart:', divider=divider_color)

            bar_consolidado(
                df=df_vinho_consolidado,
                col='valor',
                title='',
                ylabel='Valor (em US$)',
                legend=True,
                output_mean_line=True,
                output_median_line=True
            )
            st.pyplot()

            with st.expander("Descrição"):
                st.write('''
                    O gráfico de barras acima mostra os maiores compradores de vinho (considerando o volume monetário). Podemos observar que o :blue[Paraguai] junto da :blue[Rússia] são os maiores exportadores neste cenário.
                ''')

        with col1:
            st.subheader(
                ':blue[TOP 15] maiores compradores de vinho (em litros) nos últimos :blue[15 anos] :bar_chart:', divider=divider_color)

            bar_consolidado(
                df=df_vinho_consolidado,
                col='quantidade',
                ylabel='Valor (em litros)',
                legend=True,
                output_mean_line=True,
                output_median_line=True
            )
            st.pyplot()

            with st.expander("Descrição"):
                st.write('''
                    O gráfico de barras acima mostra os maiores compradores de vinho (considerando a quantidade). Podemos observar que a :blue[Rússia] junto do :blue[Paraguai] são os maiores exportadores neste cenário.
                ''')

    with st.container():
        _, col1, _ = st.columns([1, 3, 1])

        with col1:
            st.subheader(
                'Evolução do :blue[TOP 5] maiores compradores de vinho (em litros) nos últimos :blue[15 anos] :chart_with_upwards_trend:', divider=divider_color)

            linha_consolidado(
                df=df_vinho,
                col='quantidade',
                ylabel='Valor (em litros)',
                xlabel='Ano',
                legend=True,
                escala_y=15_000
            )
            st.pyplot()

            with st.expander("Descrição"):
                st.write('''
                    O gráfico de linha acima mostra a evolução do top 5 maiores compradores de vinho. Podemos observar que o :blue[Paraguai] se tornou o maior parceiro comercial dos últimos anos.
                ''')


with tab1:
    st.write('## Exportações de espumante')

    with st.container():
        col0, col1 = st.columns([1, 1])

        with col0:
            st.subheader(
                ':blue[TOP 15] maiores compradores de espumante (em US$) nos últimos :blue[15 anos] :bar_chart:', divider=divider_color)

            bar_consolidado(
                df=df_espumante_consolidado,
                col='valor',
                title='',
                ylabel='Valor (em US$)',
                legend=True,
                output_mean_line=True,
                output_median_line=True
            )
            st.pyplot()

            with st.expander("Descrição"):
                st.write('''
                    O gráfico de barras acima mostra os maiores compradores de espumante (considerando o volume monetário). Podemos observar que os :blue[Estados Unidos] estão isolados como os maiores exportadores do produto neste cenário.
                ''')

        with col1:
            st.subheader(
                ':blue[TOP 15] maiores compradores de espumante (em litros) nos últimos :blue[15 anos] :bar_chart:', divider=divider_color)

            bar_consolidado(
                df=df_espumante_consolidado,
                col='quantidade',
                ylabel='Valor (em litros)',
                legend=True,
                output_mean_line=True,
                output_median_line=True
            )
            st.pyplot()

            with st.expander("Descrição"):
                st.write('''
                    O gráfico de barras acima mostra os maiores compradores de espumante (em litros). Podemos observar que os :blue[Estados Unidos] estão isolados como os maiores exportadores do produto neste cenário.
                ''')

    with st.container():
        _, col1, _ = st.columns([1, 3, 1])

        with col1:
            st.subheader(
                'Evolução do :blue[TOP 10] maiores compradores de espumante (em litros) nos últimos :blue[15 anos] :chart_with_upwards_trend:', divider=divider_color)

            linha_consolidado(
                df=df_espumante,
                col='quantidade',
                ylabel='Valor (em litros)',
                xlabel='Ano',
                legend=True,
                escala_y=15_000,
                top=10
            )
            st.pyplot()

            with st.expander("Descrição"):
                st.write('''
                    O gráfico de linha acima mostra a evolução do top 10 maiores compradores de espumante. Podemos observar que os :blue[Estados Unidos] ainda continuam isolados como os maiores exportadores.
                    Para este caso específico trouxemos o top 10 para também considerarmos o :blue[Paraguai] na análise. Por ser o maior exportador de vinho, há oportunidades de fecharmos novas
                    parcerias e aplicarmos técnicas de cross-selling para vendermos ambos os tipos de produto (vinho e espumante) com condições vantajosas para ambas as partes.
                ''')

with tab2:
    st.write('## Exportações de suco')

    with st.container():
        col0, col1 = st.columns([1, 1])

        with col0:
            st.subheader(
                ':blue[TOP 15] maiores compradores de suco (em US$) nos últimos :blue[15 anos] :bar_chart:', divider=divider_color)

            bar_consolidado(
                df=df_suco_consolidado,
                col='valor',
                ylabel='Valor (em US$)',
                legend=True,
                output_mean_line=True,
                output_median_line=True
            )
            st.pyplot()

            with st.expander("Descrição"):
                st.write('''
                    O gráfico de barras acima mostra os maiores compradores de suco (considerando o volume monetário). Podemos observar que o :blue[Japão] está isolado como o maior exportador do produto neste cenário.
                ''')

        with col1:
            st.subheader(
                ':blue[TOP 15] maiores compradores de suco (em litros) nos últimos :blue[15 anos] :bar_chart:', divider=divider_color)

            bar_consolidado(
                df=df_suco_consolidado,
                col='quantidade',
                ylabel='Valor (em litros)',
                legend=True,
                output_mean_line=True,
                output_median_line=True
            )
            st.pyplot()

            with st.expander("Descrição"):
                st.write('''
                    O gráfico de barras acima mostra os maiores compradores de suco (em litros). Podemos observar que o :blue[Japão] está isolado como o maior exportador do produto neste cenário.
                ''')

    with st.container():
        _, col1, _ = st.columns([1, 3, 1])

        with col1:
            st.subheader(
                'Evolução do :blue[TOP 5] maiores compradores de suco (em litros) nos últimos :blue[15 anos] :chart_with_upwards_trend:', divider=divider_color)

            linha_consolidado(
                df=df_suco,
                col='quantidade',
                ylabel='Valor (em litros)',
                xlabel='Ano',
                legend=True,
                escala_y=15_000
            )
            st.pyplot()

            with st.expander("Descrição"):
                st.write('''
                    O gráfico de linha acima mostra a evolução do top 5 maiores compradores de suco. Podemos observar que o :blue[Japão] ainda está isolado como o maior exportador.
                    Aqui também observamos o :blue[Paraguai] figurando no top 5. Tomando como base o cross-selling sugerido para espumantes e vinhos, podemos considerar também incluir
                    a venda de suco na estratégia.
                ''')

with tab3:
    st.write('## Exportações de uva')

    with st.container():
        col0, col1 = st.columns([1, 1])

        with col0:
            st.subheader(
                ':blue[TOP 15] maiores compradores de uva (em US$) nos últimos :blue[15 anos] :bar_chart:', divider=divider_color)

            bar_consolidado(
                df=df_uva_consolidado,
                col='valor',
                ylabel='Valor (em US$)',
                legend=True,
                output_mean_line=True,
                output_median_line=True
            )
            st.pyplot()

            with st.expander("Descrição"):
                st.write('''
                    O gráfico de barras acima mostra os maiores compradores de uva (considerando o volume monetário). Podemos observar que os :blue[Países Baixos] estão isolados como o maior exportador do produto neste cenário.
                ''')

        with col1:
            st.subheader(
                ':blue[TOP 15] maiores compradores de uva (em kg) nos últimos :blue[15 anos] :bar_chart:', divider=divider_color)

            bar_consolidado(
                df=df_uva_consolidado,
                col='quantidade',
                ylabel='Valor (em kg)',
                legend=True,
                output_mean_line=True,
                output_median_line=True
            )
            st.pyplot()

            with st.expander("Descrição"):
                st.write('''
                    O gráfico de barras acima mostra os maiores compradores de uva (em kg). Podemos observar que os :blue[Países Baixos] estão isolados como o maior exportador do produto neste cenário.
                ''')

    with st.container():
        _, col1, _ = st.columns([1, 3, 1])

        with col1:
            st.subheader(
                'Evolução do :blue[TOP 5] maiores compradores de uva (em kg) nos últimos :blue[15 anos] :chart_with_upwards_trend:', divider=divider_color)

            linha_consolidado(
                df=df_uva,
                col='quantidade',
                ylabel='Valor (em kg)',
                xlabel='Ano',
                legend=True,
                escala_y=15_000
            )
            st.pyplot()

            with st.expander("Descrição"):
                st.write('''
                    O gráfico de linha acima mostra a evolução do top 5 maiores compradores de uva. Podemos observar que os :blue[Países Baixos] estão isolados como o maior exportador.
                    Recentemente, em 2022, a :blue[Romênia] também desponta como um parceiro comercial promissor.
                ''')

with tab4:
    st.write('## 1º Tech Challenge')
    st.write(':orange[Aluno:] Danilo Henrique Achcar')
    st.write(':orange[RM:] 351516')
    st.write(':orange[Turma:] 2DTAT')
    st.write(
        ':orange[Github:] https://github.com/dhachcar/postech-tech-challenge-1')
    st.write('FIAP - Pós Tech')
