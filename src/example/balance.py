"""
Example: Get balance via GET /v1/balance.
Run from repo root (github/python):  python src/examples/balance.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from client import SolvertrClient
from config import BASE_URL, API_KEY


def main():
    client = SolvertrClient(BASE_URL, API_KEY)
    print("--- Balance ---")
    try:
        data = client.balance()
        print("Balance:", data.get("balance"))
        print("Active:", data.get("isActive"))
        print("Full response:", data)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
