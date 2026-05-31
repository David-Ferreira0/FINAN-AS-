import os
import pandas as pd 

def carregar_dados():
    pasta = 'dados_brutos'
    arquivos_csv = [f for f in os.listdir(pasta) if f.endswith('.csv')]

    if not arquivos_csv:
        raise FileNotFoundError("Nenhum arquivo encontrado dentro da pasta '{pasta}'. Por favor, cole seu extrato lá")

    caminho_arquivo = os.path.join(pasta, arquivos_csv[0])
    print(f" Lendo o arquivo: {caminho_arquivo}")

    df = pd.read_csv(caminho_arquivo, sep=',', encoding='utf-8-sig')

    colunas_necessarias = ['Data', 'Descrição','Valor']

    for col in colunas_necessarias:
        if col not in df.columns:
            raise KeyError(f"A coluna '{col}' não foi encontrada no seu arquivo. As colunas existentes são: {list(df.columns)}")

    df = df[colunas_necessarias]

    if df['Valor'].dtype == '0':
        df['Valor'] = df['Valor'].astype(str).str.replace('R$','', regex=False)
        df['Valor'] = df['Valor'].str.strip()

        df['Valor'] = df['Valor'].str.replace('.','',regex=False)
        df['Valor'] = df['Valor'].str.replace(',','.',regex=False)

    df['Valor'] = pd.to_numeric(df['Valor'],errors='coerce')

    df ['Data'] = pd.to_datetime(df['Data'],dayfirst=True,errors='coerce')

    df = df.dropna(subset=['Data','Valor'])

    df = df.sort_values(by='Data')

    return df

if __name__ == "__main__":
    try:
        df_real = carregar_dados()
        print("\nSeus dados foram carregados e limpos com sucesso!")
        print(f"Total de transações encontradas: {len(df_real)}")
        print("\nAqui estão as primeiras linhas do seu extrato tratado:")
        print(df_real.head())
    except Exception as e:
        print(f"\n Ocorreu um erro: {e}")

