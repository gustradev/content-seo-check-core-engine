import importlib
import pkgutil
from pathlib import Path

def run_analysis(content=None, html=None, mode="text"):
    results = []

    if mode == "text" and content:
        package = "core.modules.text_mode"
        path = str(Path(__file__).parent / "modules" / "text_mode")
        for _, mod_name, _ in pkgutil.iter_modules([path]):
            mod = importlib.import_module(f"{package}.{mod_name}")
            results.append(mod.check(content))
    
    elif mode == "url" and html:
        package = "core.modules.url_mode"
        path = str(Path(__file__).parent / "modules" / "url_mode")
        for _, mod_name, _ in pkgutil.iter_modules([path]):
            mod = importlib.import_module(f"{package}.{mod_name}")
            results.append(mod.check(html))
    
    else:
        raise ValueError("Invalid mode or missing input for analysis")
    
    return results


if __name__ == "__main__":
    print("🚀 Running Content SEO Check Core Engine Demo...")
    sample_text = "This is a quick test to verify that the content-seo-check-core-engine works."
    try:
        results = run_analysis(content=sample_text, mode="text")
        print("✅ Analysis completed successfully:")
        for res in results:
            print(res)
    except Exception as e:
        print("❌ Error:", e)
