def check(content: str):
    paragraphs = [p for p in content.split("\n") if p.strip()]
    return {
        "factor": "Paragraph Count",
        "value": len(paragraphs)
    }
