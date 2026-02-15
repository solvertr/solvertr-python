"""
Example: Get usage stats via GET /v1/usage-stats?days=7.
Run from repo root (github/python):  python src/examples/usage_stats.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from client import SolvertrClient
from config import BASE_URL, API_KEY


def main():
    client = SolvertrClient(BASE_URL, API_KEY)
    print("--- Usage stats (last 7 days) ---")
    try:
        data = client.usage_stats(days=7)
        print(json.dumps(data, indent=2, default=str))
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
