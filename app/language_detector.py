"""Language detection utilities for the FastAPI application."""
from __future__ import annotations

import re
from typing import Dict, Pattern


class LanguageDetector:
    """Detect the probable language of a text using simple regex rules."""

    def __init__(self) -> None:
        # Compile regular expressions once so lookups stay fast.
        self._language_patterns: Dict[str, Pattern[str]] = {
            "japanese": re.compile(r"[\u3040-\u30ff\u4e00-\u9faf]"),
            "english": re.compile(r"[A-Za-z]"),
            "number": re.compile(r"[0-9]"),
        }

    def detect_language(self, text: str) -> str:
        """Return the first matching language name or 'unknown' if nothing matches."""
        for language, pattern in self._language_patterns.items():
            if pattern.search(text):
                return language
        return "unknown"
