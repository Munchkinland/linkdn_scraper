import os
import pandas as pd
from sentiment_analysis import SentimentAnalyzer
from plotter import PlotlyVisualizer

def load_texts_from_excel(folder_path):
    texts = []
    file_paths = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".xlsx"):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_excel(file_path)
            texts.extend(df['Post Text'].tolist())
            file_paths.extend([file_path] * len(df))  # Track the file path for each text
    return texts, file_paths

def save_results_to_excel(df, file_paths):
    for i, file_path in enumerate(file_paths):
        # Load the original dataframe
        original_df = pd.read_excel(file_path)
        
        # Add the sentiment column to the dataframe
        original_df['Sentiment'] = df['Sentiment']
        
        # Save the updated dataframe to a new file
        new_file_path = file_path.replace('.xlsx', '_with_sentiments.xlsx')
        original_df.to_excel(new_file_path, index=False)
        print(f"Saved results to {new_file_path}")

def main():
    folder_path = 'data'
    
    # Cargar los textos
    texts, file_paths = load_texts_from_excel(folder_path)
    
    # Analizar sentimientos
    analyzer = SentimentAnalyzer()
    sentiments = analyzer.analyze_sentiments(texts)
    
    # Crear DataFrame con los resultados
    df = analyzer.create_dataframe(texts, sentiments)
    
    # Guardar resultados en archivos Excel
    save_results_to_excel(df, file_paths)
    
    # Visualizar los resultados
    visualizer = PlotlyVisualizer(df)
    visualizer.plot_sentiments()
    
    # Obtener el modelo empleado
    model = analyzer.select_model(df['Sentiment'].mode()[0])
    
    # Imprimir resumen
    print("Proceso finalizado.")
    print(f"Total de posts procesados: {len(texts)}")
    print(f"Modelo empleado: {model.model}")
    
if __name__ == "__main__":
    main()
