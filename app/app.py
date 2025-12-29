"""FastAPI application exposing the LanguageDetector service."""
from fastapi import FastAPI
from pydantic import BaseModel, Field

from app.language_detector import LanguageDetector

app = FastAPI(title="Basic Language Detector API", version="1.0.0")

detector = LanguageDetector()


class LanguageRequest(BaseModel):
    """Schema describing the expected request payload."""

    query: str = Field(..., min_length=1, description="User provided query text")


class LanguageResponse(BaseModel):
    """Schema describing the language detection result."""

    query: str
    language: str


@app.post("/language", response_model=LanguageResponse)
async def detect_language(payload: LanguageRequest) -> LanguageResponse:
    """Detect the probable language of the provided query."""
    # The detector uses regex-based checks to guess the language label.
    language = detector.detect_language(payload.query)
    return LanguageResponse(query=payload.query, language=language)
