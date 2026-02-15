"""
Example: Solve Turnstile via GET /v1/turnstile/solve (query params).
Run from repo root (github/python):  python src/examples/solve_get.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from client import SolvertrClient
from config import BASE_URL, API_KEY

# Example site (Cloudflare demo)
EXAMPLE_URL = "https://demo.turnstile.workers.dev"
EXAMPLE_SITEKEY = "0x4AAAAAAAOQsVb_cjyMKnh"


def main():
    client = SolvertrClient(BASE_URL, API_KEY)

    # 1) JSON response
    print("--- GET solve (JSON response) ---")
    try:
        result = client.solve(EXAMPLE_URL, EXAMPLE_SITEKEY, use_get=True)
        print(result)
        if isinstance(result, dict) and result.get("success"):
            print("Token (first 60 chars):", (result.get("token") or "")[:60] + "...")
    except Exception as e:
        print("Error:", e)

    # 2) Plain text token only
    print("\n--- GET solve (plain text token) ---")
    try:
        token = client.solve(
            EXAMPLE_URL, EXAMPLE_SITEKEY, use_get=True, plain_text=True
        )
        print("Token:", token[:60] + "..." if len(token) > 60 else token)
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
