import os
import logging
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def main():
    load_dotenv()
    
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = os.getenv('DB_PORT')  
    DB_NAME = os.getenv('DB_NAME')
    
    if not DB_USER or not DB_PASSWORD:
        logging.warning("As credenciais do banco não foram encontradas no arquivo .env.")
        return

    engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
    
    tabelas = ['characters', 'locations', 'episodes']
    
    for nome_tabela in tabelas:
        nome_arquivo = f'{nome_tabela}.csv'
        
        if os.path.exists(nome_arquivo):
            logging.info(f"Lendo dados de {nome_arquivo}...")
            df = pd.read_csv(nome_arquivo)
            
            logging.info(f"Carregando dados na tabela: {nome_tabela} do PostgreSQL...")
            df.to_sql(nome_tabela, engine, if_exists='replace', index=False)
            logging.info(f"Tabela '{nome_tabela}' alimentada com sucesso!")
        else:
            logging.warning(f"Arquivo {nome_arquivo} não encontrado. Execute o Extract.py primeiro.")

if __name__ == "__main__":
    main()
