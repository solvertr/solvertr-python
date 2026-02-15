"""
Example: Full flow — solve, then optional balance/usage check with basic error handling.
Run from repo root (github/python):  python src/examples/full_flow.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from client import SolvertrClient
from config import BASE_URL, API_KEY

import requests

EXAMPLE_URL = "https://demo.turnstile.workers.dev"
EXAMPLE_SITEKEY = "0x4AAAAAAAOQsVb_cjyMKnh"


def main():
    client = SolvertrClient(BASE_URL, API_KEY)

    # Optional: check balance first
    try:
        bal = client.balance()
        print("Current balance:", bal.get("balance"))
        if bal.get("balance", 0) <= 0:
            print("Insufficient balance. Refill tokens in the dashboard.")
            return
    except requests.HTTPError as e:
        if e.response is not None:
            body = e.response.json() if e.response.headers.get("content-type", "").startswith("application/json") else {}
            code = body.get("code", "")
            if e.response.status_code == 401:
                print("Invalid or missing API key (MISSING_API_KEY / INVALID_API_KEY).")
            elif e.response.status_code == 402:
                print("Insufficient balance (INSUFFICIENT_BALANCE).")
            else:
                print("Balance check failed:", body.get("error", e))
        else:
            print("Balance check failed:", e)
        return
    except Exception as e:
        print("Balance check failed:", e)
        return

    # Solve
    print("\n--- Requesting solve ---")
    try:
        result = client.solve(EXAMPLE_URL, EXAMPLE_SITEKEY, use_get=False)
        if isinstance(result, dict):
            if result.get("success"):
                print("Token received (first 50 chars):", (result.get("token") or "")[:50] + "...")
                print("New balance:", result.get("balance"))
                print("Response time (ms):", result.get("responseTime"))
            else:
                print("Solve failed:", result.get("error", result))
        else:
            print("Token:", result[:50] + "..." if len(result) > 50 else result)
    except requests.HTTPError as e:
        if e.response is not None:
            body = e.response.json() if e.response.headers.get("content-type", "").startswith("application/json") else {}
            code = body.get("code", "")
            if e.response.status_code == 429:
                print("Rate limit exceeded (RATE_LIMIT_EXCEEDED). Retry after the given period.")
            elif e.response.status_code == 504:
                print("Timeout (TIMEOUT). Site or sitekey may be invalid.")
            elif e.response.status_code == 503 and code == "QUEUE_FULL":
                print("Queue full. Retry later (retryAfter in response).")
            else:
                print("Solve failed:", body.get("error", body))
        else:
            print("Solve failed:", e)
    except requests.Timeout:
        print("Request timeout (TIMEOUT).")
    except Exception as e:
        print("Error:", e)

    # Optional: rate limit status
    print("\n--- Rate limit status ---")
    try:
        rl = client.rate_limit_status()
        print("Remaining (this window):", rl.get("rateLimit", {}).get("remaining"))
        print("Limit:", rl.get("rateLimit", {}).get("limit"))
    except Exception as e:
        print("Rate limit status error:", e)


if __name__ == "__main__":
    main()
