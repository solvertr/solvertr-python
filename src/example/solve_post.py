"""
Example: Solve Turnstile via POST /v1/turnstile/solve (JSON body, X-API-Key header).
Run from repo root (github/python):  python src/examples/solve_post.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from client import SolvertrClient
from config import BASE_URL, API_KEY

EXAMPLE_URL = "https://demo.turnstile.workers.dev"
EXAMPLE_SITEKEY = "0x4AAAAAAAOQsVb_cjyMKnh"


def main():
    client = SolvertrClient(BASE_URL, API_KEY)

    print("--- POST solve (JSON) ---")
    try:
        result = client.solve(EXAMPLE_URL, EXAMPLE_SITEKEY, use_get=False)
        print(result)
        if isinstance(result, dict) and result.get("success"):
            print("Token (first 60 chars):", (result.get("token") or "")[:60] + "...")
            print("Balance after:", result.get("balance"))
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
