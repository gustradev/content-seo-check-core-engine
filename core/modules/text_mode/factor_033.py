# core/modules/text_mode/factor_033.py

# Plagiarism is the inverse of originality.
def check(content: str) -> dict:
    """
    Measures internal plagiarism by checking the ratio of duplicate sentences.
    Higher value (closer to 1.0) means higher internal redundancy/plagiarism.
    """
    from core.modules.text_mode import factor_032 
    
    # Value is 1.0 - Originality Score (Max Plagiarism is 1.0 or 100%)
    originality_score = factor_032.check(content).get("value", 0.0)
    value = 1.0 - originality_score

    return {
        "factor": "Plagiarism Ratio (Internal)",
        "value": round(value, 2)
    }