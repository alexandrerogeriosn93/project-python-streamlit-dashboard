import json
import pandas as pd

try:
    with open("data/vendas.json", "r") as file:
        data = json.load(file)
    data_frame = pd.DataFrame.from_dict(data)
    print(data_frame)
except FileNotFoundError:
    print("Erro: O arquivo 'vendas.json' não foi encontrado.")
except json.JSONDecodeError:
    print("Erro: O arquivo não é um JSON válido.")
except Exception as e:
    print(f"Erro inesperado: {e}")
