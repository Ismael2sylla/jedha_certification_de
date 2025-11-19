from pathlib import Path
import json, uuid, hashlib
def ensure_dir(p: str): Path(p).mkdir(parents=True, exist_ok=True)
def new_batch_id() -> str: import uuid as _u; return str(_u.uuid4())
def save_json(path: str, obj: dict):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f: json.dump(obj, f, ensure_ascii=False, indent=2)
def load_json(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f: return json.load(f)
def sha256_hex(value: str) -> str: return hashlib.sha256(value.encode("utf-8")).hexdigest()
