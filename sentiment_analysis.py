import transformers
from langdetect import detect
import pandas as pd

class SentimentAnalyzer:
    def __init__(self):
        # Modelos para diferentes idiomas
        self.models = {
            'en': transformers.pipeline('sentiment-analysis', model='distilbert/distilbert-base-uncased-finetuned-sst-2-english'),
            'es': transformers.pipeline('sentiment-analysis', model='cardiffnlp/twitter-roberta-base-sentiment-latest'),
            'multilingual': transformers.pipeline('sentiment-analysis', model='bert-base-multilingual-cased')
        }

    def detect_language(self, text):
        try:
            lang = detect(text)
        except Exception as e:
            print(f"Error detecting language: {e}")
            lang = 'unknown'
        return lang

    def select_model(self, language):
        if language == 'en':
            return self.models['en']
        elif language == 'es':
            return self.models['es']
        else:
            return self.models['multilingual']
        
        print(f"Selected model for language '{language}': {model.model}") # Imprimir modelo seleccionado
        return mode

    def map_sentiment(self, label):
        # Mapea las etiquetas de los modelos a 'Positivo', 'Negativo' o 'Neutro'
        if label.lower() in ['positive', '5 stars', '4 stars']:
            return 'Positivo'
        elif label.lower() in ['negative', '1 star', '2 stars']:
            return 'Negativo'
        else:
            return 'Neutro'

    def analyze_sentiment(self, text):
        language = self.detect_language(text)
        model = self.select_model(language)
        if model:
            result = model(text)
            if isinstance(result, list) and len(result) > 0:
                sentiment = self.map_sentiment(result[0]['label'])
                score = result[0]['score']
                return sentiment, score
            else:
                return 'Neutro', 0.0
        else:
            return 'Neutro', 0.0

    def analyze_sentiments(self, texts):
        return [self.analyze_sentiment(text) for text in texts]

    def create_dataframe(self, texts, sentiments):
        sentiment_labels = [result[0] for result in sentiments]  # Etiquetas de sentimientos
        sentiment_scores = [result[1] for result in sentiments]  # Puntajes de sentimientos
        return pd.DataFrame({
            'Post Text': texts,
            'Sentiment': sentiment_labels,
            'Score': sentiment_scores
        })
