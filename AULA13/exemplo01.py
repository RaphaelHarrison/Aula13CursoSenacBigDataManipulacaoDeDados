import pandas as pd

# Polars é uma biblioteca que trabalha com Multithread. Por isso, recomenda-se para trabalhos em larga escala. 
# A tendência é que seja bem mais rápido que o pandas, pois o processamento de dados é feito em paralelo.
# https:/polars.rs
import polars as pl
from datetime import datetime # biblioteca que trabalha com tempo


# Lendo Bolsa Familia
try:
    ENDERECO_DADOS = r'../Dados/'
    
    hora_inicial = datetime.now()
    print("Carregando...")
    
    # Pandas 0:00:19.78
    # df_janeiro = pd.read_csv(ENDERECO_DADOS + "202601_NovoBolsaFamilia.csv", sep=";", encoding="iso-8859-1")
    
    # Pandas 0:00:07.38
    df_janeiro = pl.read_csv(ENDERECO_DADOS + "202601_NovoBolsaFamilia.csv", separator=";", encoding="iso-8859-1")
    
    print(df_janeiro.head())
    print(df_janeiro.columns) # Mostra o Nome das colunas
    print(df_janeiro.shape) # Quantidade de Linhas e Colunas 
    
    hora_final = datetime.now()
    
    print(f"Tempo de Execução: {hora_final - hora_inicial}")
    
except Exception as e:
    print(f"Erro ao processar as informações: {e}")