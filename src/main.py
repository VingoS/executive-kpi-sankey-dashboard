# src/main.py
from pathlib import Path
from sankey_builder import build_sankey
from data_loader import load_financial_data

# -------------------------------------------------------------------------
# Dados estáticos (requisitos da sprint)
# -------------------------------------------------------------------------
csv_file = Path("data") / "sample_dre.csv"

financials = load_financial_data(csv_file)

receita_bruta = financials["receita_bruta"]
deducoes = financials["deducoes"]
custos = financials["custos"]
despesas_operacionais = financials["despesas_operacionais"]
resultado_financeiro = financials["resultado_financeiro"]

# -------------------------------------------------------------------------
# Cálculo dos indicadores derivados
# -------------------------------------------------------------------------
receita_liquida = receita_bruta - deducoes
margem_bruta = receita_liquida - custos
ebitda = margem_bruta - despesas_operacionais
lucro_liquido = ebitda - resultado_financeiro

# -------------------------------------------------------------------------
# Preparação dos nós e fluxos do Sankey
# -------------------------------------------------------------------------
# Ordem dos nós (importante para índices)
labels = [
    "Receita Bruta",
    "Deduções",
    "Receita Líquida",
    "Custos",
    "Margem Bruta",
    "Despesas Operacionais",
    "EBITDA",
    "Resultado Financeiro",
    "Lucro Líquido",
]

# Mapeamento de links (fonte -> alvo) conforme a árvore descrita
sources = [
    0,  # Receita Bruta -> Deduções
    0,  # Receita Bruta -> Receita Líquida
    2,  # Receita Líquida -> Custos
    2,  # Receita Líquida -> Margem Bruta
    4,  # Margem Bruta -> Despesas Operacionais
    4,  # Margem Bruta -> EBITDA
    6,  # EBITDA -> Resultado Financeiro
    6,  # EBITDA -> Lucro Líquido
]

targets = [
    1,  # Deduções
    2,  # Receita Líquida
    3,  # Custos
    4,  # Margem Bruta
    5,  # Despesas Operacionais
    6,  # EBITDA
    7,  # Resultado Financeiro
    8,  # Lucro Líquido
]

# Valores associados a cada link
values = [
    deducoes,               # Receita Bruta -> Deduções
    receita_liquida,        # Receita Bruta -> Receita Líquida
    custos,                 # Receita Líquida -> Custos
    margem_bruta,           # Receita Líquida -> Margem Bruta
    despesas_operacionais,  # Margem Bruta -> Despesas Operacionais
    ebitda,                 # Margem Bruta -> EBITDA
    resultado_financeiro,   # EBITDA -> Resultado Financeiro
    lucro_liquido,          # EBITDA -> Lucro Líquido
]

# -------------------------------------------------------------------------
# Geração do gráfico
# -------------------------------------------------------------------------
fig = build_sankey(labels, sources, targets, values, title="Executive KPI Sankey")

# -------------------------------------------------------------------------
# Exportação
# -------------------------------------------------------------------------
output_path = Path("output") / "sankey.html"
output_path.parent.mkdir(parents=True, exist_ok=True)
fig.write_html(str(output_path))

print(f"Sankey salvo em {output_path}")