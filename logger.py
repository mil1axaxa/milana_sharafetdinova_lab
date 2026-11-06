from __future__ import annotations
from datetime import datetime

def log_error(message: str) -> None:
    """Записать ошибку в лог-файл с указанием времени."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("input_errors.log", "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")
