from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
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

        # --- Run Core Analyzer ---
        results = run_analysis(content=content, html=html, mode=mode)

        # --- Handle empty or failed results gracefully ---
        if not results or (isinstance(results, list) and "error" in results[0]):
            return jsonify({
                "error": "Analyzer returned no valid results.",
                "details": results
            }), 500

        # --- Aggregate basic metrics ---
        avg_score = sum(r.get("score", 0) for r in results if isinstance(r, dict)) / max(len(results), 1)
        # Some modules may not have readability → skip average_readability
        avg_readability = (
            sum(r.get("readability", 0) for r in results if r.get("readability") is not None)
            / max(len([r for r in results if r.get("readability") is not None]), 1)
        )

        # --- Build JSON response ---
        response = {
            "version": "core-v1.0",
            "mode": mode,
            "factors_analyzed": len(results),
            "semantic_score": round(avg_score, 2),
            "readability": round(avg_readability, 2),
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
