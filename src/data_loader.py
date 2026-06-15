import pandas as pd
from pathlib import Path


def load_financial_data(csv_path):
    path = Path(csv_path)

    df = pd.read_csv(path)

    row = df.iloc[0]

    return {
        "receita_bruta": float(row["receita_bruta"]),
        "deducoes": float(row["deducoes"]),
        "custos": float(row["custos"]),
        "despesas_operacionais": float(row["despesas_operacionais"]),
        "resultado_financeiro": float(row["resultado_financeiro"]),
    }