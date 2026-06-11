import requests
import pandas as pd
import logging

# Configuração básica do logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def extrair_dados_api(url_base):
    resultados = []
    proxima_url = url_base
    
    logging.info(f"Iniciando extração de: {url_base}")
    
    while proxima_url:
        response = requests.get(proxima_url)
        response.raise_for_status() 
        data = response.json()
        
        resultados.extend(data['results'])
        proxima_url = data['info']['next'] 
        
    logging.info(f"Extração concluída para {url_base}. Total de registros: {len(resultados)}")
    return resultados

def main():
    endpoints = {
        'characters': 'https://rickandmortyapi.com/api/character',
        'locations': 'https://rickandmortyapi.com/api/location',
        'episodes': 'https://rickandmortyapi.com/api/episode'
    }
    
    for nome_tabela, url in endpoints.items():
        dados_json = extrair_dados_api(url)
        df = pd.json_normalize(dados_json)
        
        # Converte listas e dicionários aninhados para string
        for col in df.columns:
            if df[col].apply(lambda x: isinstance(x, (list, dict))).any():
                df[col] = df[col].astype(str)
                
        # 3. Salva localmente em CSV para ser lido pelo load.py
        nome_arquivo = f'{nome_tabela}.csv'
        logging.info(f"Salvando dados em: {nome_arquivo}...")
        df.to_csv(nome_arquivo, index=False)
        logging.info(f"Arquivo '{nome_arquivo}' gerado com sucesso!")

if __name__ == "__main__":
    main()
