from pathlib import Path

BASE_DIR = Path("C:/Users/hp/Desktop/Study Pilot AI")

def join(relative_path: str) -> Path:
    return BASE_DIR / relative_path
