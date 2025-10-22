import os
import importlib
import pandas as pd
import math
import spacy
from spacy.cli import download

download("en_core_web_sm")
nlp = spacy.load("en_core_web_sm")

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODULE_DIR = os.path.join(BASE_DIR, "core", "modules")

# --- Load factors from CSV ---
def load_factors(mode: str):
    csv_file = os.path.join(DATA_DIR, f"{mode}_factors.csv")
    if not os.path.exists(csv_file):
        raise FileNotFoundError(f"Factor CSV not found for mode: {mode}")
    return pd.read_csv(csv_file)

# --- Dynamic module import ---
def dynamic_import(module_path: str):
    try:
        return importlib.import_module(module_path)
    except ModuleNotFoundError:
        return None

# --- Calculate score ---
def calculate_factor_score(value, suggested, weight):
    if suggested in [0, None] or math.isnan(suggested):
        return 0
    deviation = abs(value - suggested) / suggested
    score = max(0, (1 - deviation)) * weight * 20
    return round(score, 2)

# --- Analyze content ---
def analyze(content: str, mode: str = "text"):
    df = load_factors(mode)
    results = []
    total_weight = df["weight"].sum()
    weighted_score_sum = 0

    for _, row in df.iterrows():
        factor_id = str(row["id"]).zfill(3)
        module_name = f"core.modules.{mode}_mode.factor_{factor_id}"
        module = dynamic_import(module_name)

        if module and hasattr(module, "check"):
            try:
                result = module.check(content)
                value = result.get("value", 0)
                if value is None or (isinstance(value, float) and math.isnan(value)):
                    value = 0

                suggested = row.get("suggestion_value", 0)
                if suggested is None or (isinstance(suggested, float) and math.isnan(suggested)):
                    suggested = 0

                score = calculate_factor_score(value, suggested, row["weight"])
                weighted_score_sum += score

                suggestion_over = row.get("suggestion_text_if_over", "")
                suggestion_below = row.get("suggestion_text_if_below", "")

                results.append({
                    "id": row["id"],
                    "factor": result.get("factor", row.get("name", "")),
                    "value": value,
                    "weight": row.get("weight", 0),
                    "suggestion_value": suggested,
                    "score": score,
                    "suggestion_over": suggestion_over,
                    "suggestion_below": suggestion_below,
                })
            except Exception as e:
                results.append({
                    "id": row["id"],
                    "factor": row.get("name", ""),
                    "value": 0,
                    "weight": row.get("weight", 0),
                    "suggestion_value": row.get("suggestion_value", 0),
                    "score": 0,
                    "suggestion": "",
                    "error": str(e)
                })

    total_score = round((weighted_score_sum / (total_weight * 20)) * 100, 2)
    return {
        "mode": mode,
        "total_score": total_score,
        "results": results
    }

# --- Flask bridge ---
def run_analysis(content=None, html=None, mode="text"):
    target = html if mode == "url" else content
    if not target:
        return [{"error": "No content provided for analysis"}]

    result = analyze(target, mode=mode)
    output = []

    for r in result["results"]:
        # Determine suggestion text
        suggestion_text = ""
        val = r.get("value") or 0
        sugg = r.get("suggestion_value") or 0

        if val > sugg:
            suggestion_text = r.get("suggestion_over", "")
        elif val < sugg:
            suggestion_text = r.get("suggestion_below", "")

        output.append({
            "id": r["id"],
            "factor": r.get("factor", ""),
            "value": val,
            "weight": r.get("weight", 0),
            "score": r.get("score", 0),
            "suggestion_value": sugg,
            "suggestion": suggestion_text,
            "error": r.get("error")
        })

    return output

# --- Standalone test ---
if __name__ == "__main__":
    sample_text = "AI optimization enhances content readability and engagement."
    report = analyze(sample_text, mode="text")
    print(f"Total Score: {report['total_score']}")
    for r in report["results"]:
        print(r)
