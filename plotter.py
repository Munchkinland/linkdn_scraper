import plotly.express as px
import pandas as pd

class PlotlyVisualizer:
    def __init__(self, df):
        self.df = df

    def plot_sentiments(self):
        # Añadir una columna para clasificar por sentimiento
        self.df['sentiment_class'] = self.df['Sentiment'].map({
            'Positivo': 'Positivo',
            'Negativo': 'Negativo',
            'Neutro': 'Neutro'
        })

        # Crear un gráfico de barras usando plotly express
        fig = px.bar(
            self.df,
            x='sentiment_class',  # Columna de sentimientos
            y=self.df.index,  # El índice de los posts
            color='sentiment_class',  # Colorear según el sentimiento
            hover_data=['Post Text'],  # Mostrar el texto del post al pasar el puntero
            labels={'sentiment_class': 'Sentimiento', 'y': 'Post'},
            color_discrete_map={'Positivo': 'blue', 'Negativo': 'red', 'Neutro': 'gray'}
        )

        # Ajustes para una mejor visualización
        fig.update_layout(
            title="Análisis de Sentimientos por Post",
            xaxis_title="Sentimiento",
            yaxis_title="Índice del Post",
            showlegend=False,  # Ocultar la leyenda
            hovermode="closest"  # Actualizar el hover para que cambie según el puntero
        )

        # Mostrar el gráfico
        fig.show()

