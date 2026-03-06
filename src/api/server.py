"""FastAPI inference server for AvarNLP translation."""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="AvarNLP", description="Avar-Turkish Translation API", version="0.1.0")

VALID_DIRECTIONS = {"av-tr", "tr-av"}


class TranslateRequest(BaseModel):
    text: str
    direction: str  # "av-tr" or "tr-av"


class TranslateResponse(BaseModel):
    translation: str
    direction: str
    model: str = "nllb-avar-v0.1"


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": False}


@app.post("/translate", response_model=TranslateResponse)
def translate(req: TranslateRequest):
    if req.direction not in VALID_DIRECTIONS:
        raise HTTPException(status_code=400, detail=f"Invalid direction. Use: {VALID_DIRECTIONS}")

    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    # Placeholder — will use real model after training
    translation = f"[TODO: translate '{req.text}']"

    return TranslateResponse(translation=translation, direction=req.direction)
