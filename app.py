from fastapi import FastAPI, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from scripts.prediction_pipeline import PredictionPipeline

app = FastAPI()

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML template support
templates = Jinja2Templates(directory="templates")

# Initialize the prediction pipeline
MODEL_PATH = "scripts/results/checkpoint-1317"
TOKENIZER_PATH = "src/tokenizer"
prediction_pipeline = PredictionPipeline(MODEL_PATH, TOKENIZER_PATH)

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

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

