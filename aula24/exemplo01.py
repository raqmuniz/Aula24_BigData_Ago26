import pandas as pd
from datetime import datetime
import polars as pl

ENDERECO_DADOS = './../DADOS/'
#obtendo dados
try:
    inicio = datetime.now()
    print('Carregando os dados ...')

    #Tempo total 0:00:19.18s (Pandas)
    #df_janeiro = pd.read_csv(
      #  ENDERECO_DADOS + '202601_NovoBolsaFamilia.csv', sep=';', encoding='iso-8859-1')
    

    #Polars
    df_janeiro = pl.read_csv(
        ENDERECO_DADOS + '202601_NovoBolsaFamilia.csv', separator=';', encoding='iso-8859-1')
    
    #Tempo total 0:00:06 (Polars)
    print(df_janeiro.head())
    #print(df_janeiro.columns.to_list())  #Este comando refere-se a Todas as colunas -  no Pandas
    #print(df_janeiro.columns) #Este comando refere-se a Todas as colunas -  no Polars
    
    fim = datetime.now()
    print(f'Tempo total {fim - inicio}')

except Exception as e:
    print(f'Erro ao obter dados {e}')