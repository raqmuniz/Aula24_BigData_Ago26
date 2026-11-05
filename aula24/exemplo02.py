import pandas as pd
import polars as pl
from datetime import datetime

ENDERECO_DADOS = './../DADOS/'

try:
    inicio = datetime.now()
    print('Obtendo dados de Janeiro, Fevereiro e março')
    lista_arquivos = ['202601_NovoBolsaFamilia.csv', '202602_NovoBolsaFamilia.csv', '202603_NovoBolsaFamilia.csv']

    df_bolsa_familia = None

    for arquivo in lista_arquivos:
        df = pd.read_csv(
        ENDERECO_DADOS + arquivo, sep=';', encoding='iso-8859-1')

        #print(df)

        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            df_bolsa_familia = pd.concat([df_bolsa_familia, df])
            
        del df  #deleta o dataframe temporário 'df'

    print(df_bolsa_familia)
    
    

    

    
    fim = datetime.now()
    print(f'Tempo total {fim - inicio}')

except Exception as e:
    print(f'Erro ao obter dados {e}')