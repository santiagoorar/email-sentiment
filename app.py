from fastapi import FastAPI, HTTPException
from scripts.prediction_pipeline import PredictionPipeline

app = FastAPI()

# First, let´s initialize the prediction pipeline
MODEL_PATH = "scripts/results/checkpoint-1317"
TOKENIZER_PATH = "src/tokenizer"
prediction_pipeline = PredictionPipeline(MODEL_PATH, TOKENIZER_PATH)

@app.post("/predict/")
async def predict_sentiment(text: str):
    try:
        result = prediction_pipeline.predict_with_pipeline([text])
        return {"sentiment": result[0]['label'], "confidence": result[0]['score']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
