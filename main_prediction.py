from scripts.prediction_pipeline import PredictionPipeline

tokenizer_path = "../src/tokenizer"
best_model_path = "./results/checkpoint-1317"

prediction_pipeline = PredictionPipeline(best_model_path, tokenizer_path)

