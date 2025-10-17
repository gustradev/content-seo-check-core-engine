# Content SEO Check | Core Engine

🧠 **Content SEO Check Core Engine** is a Python backend for analyzing content using **Hybrid Engine Optimization (SEO + GEO)**.  
It supports two modes:  
1. **Text Mode** – analyze text content  
2. **URL Mode** – analyze webpage HTML  

Each mode uses **factor modules**, where each module represents a single analysis factor. The engine dynamically imports these modules and runs them on input content or webpages.

---

### Project Structure
---
content-seo-check-core-engine/
├── core/
│ ├── init.py
│ ├── analyzer.py # Main dynamic analysis engine
│ └── modules/
│ ├── init.py
│ ├── text_mode/
│ │ ├── init.py
│ │ ├── factor_001.py
│ │ └── ...
│ └── url_mode/
│ ├── init.py
│ ├── factor_001.py
│ └── ...
├── data/
│ ├── text_factors.csv # Definitions for text-mode factors
│ └── url_factors.csv # Definitions for URL-mode factors
├── requirements.txt
└── README.md
---
---

## Features

- Dynamically loads **factor modules** for analysis  
- Supports **200+ factors** for SEO + GEO auditing  
- Two analysis modes:
  - **Text Mode** – process raw text input
  - **URL Mode** – process webpage HTML
- Returns structured results (JSON/dictionary)  
- Modular architecture for easy extension  

---

## Installation

```bash
git clone https://github.com/gustradev/content-seo-check-core-engine.git
cd content-seo-check-core-engine

# Optional: create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
Usage
python
Copy code
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
Adding New Factors
Create a new Python file in the appropriate folder (text_mode or url_mode)

Define a check() function that accepts content (text) or html (webpage)

Return a dictionary:

python
Copy code
{
    "factor": "Factor Name",
    "score": <calculated_value>
}
run_analysis() automatically detects and runs new modules.

Future Plans
Expand to 200+ factor modules

Store factor definitions in a database for dynamic updates

Fully integrate with frontend (content-seo-check-fe)

Add advanced scoring: readability, semantic analysis, keyword density, link authority

Author
Ida Bagus Wisnu Suputra – gustradev.com/wisnusuputra

License
ISC

