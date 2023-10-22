from transformers import ElectraForSequenceClassification, ElectraTokenizer, pipeline

class PredictionPipeline:
    def __init__(self, model_path, tokenizer_path):
        self.model = ElectraForSequenceClassification.from_pretrained(model_path)
        self.tokenizer = ElectraTokenizer.from_pretrained(tokenizer_path)

        self.label_mapping = {  # let´s define the mapping as we did before
            2: "positive",
            1: "negative",
            0: "neutral"
        }

    def predict_with_pipeline(self, texts):
        classification_pipeline = pipeline(
            "text-classification",
            model=self.model,
            tokenizer=self.tokenizer
        )
        raw_results = classification_pipeline(texts)
        # Mapping
        for result in raw_results:
            result['label'] = self.label_mapping[int(result['label'].split("_")[-1])]
        return raw_results