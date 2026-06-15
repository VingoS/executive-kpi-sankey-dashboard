# src/sankey_builder.py
import plotly.graph_objects as go

def build_sankey(labels, sources, targets, values, title="Sankey Diagram"):
    """
    Cria um gráfico Sankey usando Plotly.

    Parameters
    ----------
    labels : list of str
        Nomes dos nós do Sankey.
    sources : list of int
        Índices dos nós de origem de cada link.
    targets : list of int
        Índices dos nós de destino de cada link.
    values : list of float
        Valores (fluxos) associados a cada link.
    title : str, optional
        Título exibido no gráfico.

    Returns
    -------
    plotly.graph_objects.Figure
        Figura Sankey pronta para ser salva ou exibida.
    """
    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    line=dict(color="black", width=0.5),
                    label=labels,
                ),
                link=dict(source=sources, target=targets, value=values),
            )
        ]
    )
    fig.update_layout(title_text=title, font_size=12)
    return fig