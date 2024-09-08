import pandas as pd
import os

def load_excel_files(folder_path):
    """Carga todos los archivos .xlsx en el directorio especificado."""
    files = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]
    data_frames = []
    for file in files:
        df = pd.read_excel(os.path.join(folder_path, file))
        data_frames.append(df)
    return pd.concat(data_frames, ignore_index=True)
