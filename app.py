from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import spacy
nlp = spacy.load("en_core_web_sm")

from core.analyzer import run_analysis

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# --- Health Check ---
@app.route("/")
def health_check():
    return jsonify({
        "status": "ok",
        "engine": "Content Hybrid Core Engine",
        "version": "1.0.0"
    })


# --- Main Analyzer Endpoint ---
@app.route("/analyze", methods=["POST"])
def analyze_content():
    try:
        data = request.get_json(force=True)
        content = data.get("content")
        url = data.get("url")

        # Determine mode
        mode = "url" if url else "text"
        html = None

        # If analyzing URL, fetch HTML
        if mode == "url":
            try:
                resp = requests.get(url, timeout=10, headers={"User-Agent": "ContentHybridBot/1.0"})
                resp.raise_for_status()
                html = resp.text
            except Exception as e:
                return jsonify({
                    "error": "Failed to fetch URL content.",
                    "details": str(e)
                }), 400

        # Run core analyzer
        results = run_analysis(content=content, html=html, mode=mode)

        # Aggregate base metrics
        avg_score = sum(r.get("score", 0) for r in results) / max(len(results), 1)

        # Build response
        response = {
            "version": "core-v1.0",
            "mode": mode,
            "factors_analyzed": len(results),
            "semantic_score": round(avg_score, 3),
            "results": results
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({
            "error": "Internal analysis error.",
            "details": str(e)
        }), 500


# --- Run Server ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
