import pandas as pd
import polars as pl
from datetime import datetime 


ENDERECO_DADOS = r"../Dados/"

try: 
    print("Obtendo dados....")
    
    inicio = datetime.now()
    
    lista_arquivos = ["202601_NovoBolsaFamilia.csv", "202602_NovoBolsaFamilia.csv","202603_NovoBolsaFamilia.csv","202604_NovoBolsaFamilia.csv","202605_NovoBolsaFamilia.csv"]
    
    df_bolsa_familia = None
    
    for arquivo in lista_arquivos:
        print(f"\nProcessando o arquivo {arquivo}")
        
        # Pandas 0:01:08(Com 2 arquivos)
        # Pandas 0:05:15(Com 5 arquivos)
        # df = pd.read_csv(ENDERECO_DADOS + arquivo, sep=";", encoding="iso-8859-1")
        
        # Polars 0:00:17.64(Com 2 arquivos)
        # Polars 0:00:38(Com 5 arquivos)
        df = pl.read_csv(ENDERECO_DADOS + arquivo, separator=";", encoding="iso-8859-1")
        print(df.head())
        
        if df_bolsa_familia is None:
            df_bolsa_familia = df
        else:
            df_bolsa_familia = pl.concat([df_bolsa_familia, df])
        
        del df
    
    print(df_bolsa_familia.head())
    print(df_bolsa_familia.shape)
            
    
    final = datetime.now()

    print(f"Tempo de Execução: {final - inicio}")
except Exception as e:
    print(f"Erro ao realiar leitura dos meses: {e}")