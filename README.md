# Content SEO Check | Core Engine

🧠 **Content SEO Check Core Engine** is a Python backend for analyzing content using **Hybrid Engine Optimization (SEO + GEO)**.  
It supports two modes:  
1. **Text Mode** – analyze text content  
2. **URL Mode** – analyze webpage HTML  

Each mode uses **factor modules**, where each module represents a single analysis factor. The engine dynamically imports these modules and runs them on input content or webpages.

---

#### Project Structure Rules
```
content-seo-check-core-engine/          # Root directory of the Core Engine
├── core/                               # Main engine code
│   ├── __init__.py                      # Makes 'core' a Python package
│   ├── analyzer.py                      # Main dynamic analysis engine, loads factor modules
│   └── modules/                         # Folder containing all analysis factor modules
│       ├── __init__.py                  # Makes 'modules' a Python package
│       ├── text_mode/                   # Factors for analyzing raw text content
│       │   ├── __init__.py              # Python package initializer
│       │   ├── factor_001.py            # Example factor module
│       │   └── ...                       # Additional text-mode factors
│       └── url_mode/                    # Factors for analyzing webpage HTML
│           ├── __init__.py              # Python package initializer
│           ├── factor_001.py            # Example factor module
│           └── ...                       # Additional URL-mode factors
├── data/                                # CSV definitions for factors
│   ├── text_factors.csv                 # Factor definitions for text-mode analysis
│   └── url_factors.csv                  # Factor definitions for URL-mode analysis
├── requirements.txt                      # Python dependencies for the project
└── README.md                             # Project documentation

```

---

#### Features
---
- Dynamically loads **factor modules** for analysis  
- Supports **200+ factors** for SEO + GEO auditing  
- Two analysis modes:
  - **Text Mode** – process raw text input
  - **URL Mode** – process webpage HTML
- Returns structured results (JSON/dictionary)  
- Modular architecture for easy extension  

---

## Installation
---
```bash
git clone https://github.com/gustradev/content-seo-check-core-engine.git
cd content-seo-check-core-engine

# Optional: create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

That's an excellent project structure! To ensure your requirements.txt is complete for all the developed "Text Mode" factors (F015 through F050), and to follow modern Python practice, I'll update it to include the specific packages and the crucial data file dependencies.

Here is the updated and consolidated requirements.txt:

Plaintext

# Web scraping & HTML parsing
beautifulsoup4==4.12.2
lxml==4.9.3

# HTTP requests
requests==2.31.0

# Frameworks and API
flask
flask-cors
fastapi
uvicorn
gunicorn
pydantic

# --- Data Handling & Core Analysis ---
pandas
numpy

# --- Text Analysis & NLP ---
# NLTK base library (used for tokenization, stopwords, etc.)
nltk==3.8.1
# SpaCy base library (used for F015)
spacy
# The specific SpaCy English model data package
en-core-web-sm
# For Keyword Distribution (F035) and other numeric proxies
numpy # Already listed above, but crucial here
# For robust spell checking (recommended for F041, though currently proxied)
pyspellchecker

# Environment variable management
python-dotenv==1.0.0

# Optional: Pretty-print JSON results (for development)
rich==13.5.2
⚠️ Action Required Post-Installation
The most critical step for the engine's NLP factors (F015, F029, F031, F045, etc.) to function is ensuring the necessary data files are downloaded and linked.

After running pip install -r requirements.txt, your users must run these commands:

1. SpaCy Model Installation
This command downloads the large English model file required by factor_015.py:

Bash

python -m spacy download en_core_web_sm
2. NLTK Data Downloads
These commands download the necessary tokenization, punctuation, and stopwords data for multiple readability and keyword factors:

Bash

# Downloads sentence tokenizer data (required for F029, F031, F044, F050)
python -c "import nltk; nltk.download('punkt')"

# Downloads the English stopwords list (required for F037, F045)
python -c "import nltk; nltk.download('stopwords')"
```

## Usage
```python
from core.analyzer import run_analysis

# Text Mode
text_content = "This is an example content to analyze."
results = run_analysis(content=text_content, mode="text")

# URL Mode
html_content = "<html><body>Example page</body></html>"
results = run_analysis(html=html_content, mode="url")

# Each result is a list of factor dictionaries
for factor in results:
    print(f"{factor['factor']}: {factor['score']}")
```

### Adding New Factors
- Create a new Python file in the appropriate folder (`text_mode` or `url_mode`)  
- Define a `check()` function that accepts content (text) or html (webpage)  
- Return a dictionary:
```python
{
    "factor": "Factor Name",
    "score": <calculated_value>
}
```
- `run_analysis()` automatically detects and runs new modules.

---

# Future Plans
---
- Expand to 200+ factor modules
- Store factor definitions in a database for dynamic updates
- Fully integrate with frontend (content-seo-check-fe)
- Add advanced scoring: readability, semantic analysis, keyword density, link authority

---

## Author
Ida Bagus Wisnu Suputra – gustradev.com/wisnusuputra

## License
ISC
---
