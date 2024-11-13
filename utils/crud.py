import pandas as pd
import os
import re

csv_file = 'dados_pessoas.csv'

def salvar_dados(nome, cpf, rg):
    df = pd.DataFrame({'Nome Completo': [nome], 'CPF': [cpf], 'RG': [rg]})
    if os.path.exists(csv_file):
        df_existente = pd.read_csv(csv_file)
        df = pd.concat([df_existente, df], ignore_index=True)
    df.to_csv(csv_file, index=False)

def formatar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) == 11:
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    else:
        return cpf
