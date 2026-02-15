"""
Solvertr API client.
Uses X-API-Key header for authentication; returns raw API responses.
"""
import requests


class SolvertrClient:
    """Client for Solvertr Turnstile API."""

    def __init__(self, base_url: str, api_key: str, timeout: int = 60):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout
        self._headers = {"X-API-Key": api_key}

    def solve(
        self,
        url: str,
        sitekey: str,
        action: str | None = None,
        cdata: str | None = None,
        plain_text: bool = False,
        use_get: bool = False,
    ):
        """
        Request a Turnstile solution.

        :param url: Page URL where the widget is shown
        :param sitekey: Turnstile site key
        :param action: Optional action value
        :param cdata: Optional cdata value
        :param plain_text: If True, return only the token string (same as format=txt)
        :param use_get: If True use GET with query params; otherwise POST with JSON body
        :return: JSON dict (success, token, requestId, balance, responseTime) or plain token string
        """
        endpoint = f"{self.base_url}/v1/turnstile/solve"
        if use_get:
            params = {"url": url, "sitekey": sitekey, "apikey": self.api_key}
            if action is not None:
                params["action"] = action
            if cdata is not None:
                params["cdata"] = cdata
            if plain_text:
                params["format"] = "txt"
            resp = requests.get(
                endpoint,
                params=params,
                timeout=self.timeout,
            )
        else:
            payload = {"url": url, "sitekey": sitekey}
            if action is not None:
                payload["action"] = action
            if cdata is not None:
                payload["cdata"] = cdata
            if plain_text:
                payload["format"] = "txt"
            resp = requests.post(
                endpoint,
                json=payload,
                headers={**self._headers, "Content-Type": "application/json"},
                timeout=self.timeout,
            )
        resp.raise_for_status()
        if plain_text:
            return resp.text
        return resp.json()

    def balance(self):
        """
        Get current token balance.

        :return: JSON dict with balance, customerId, isActive
        """
        resp = requests.get(
            f"{self.base_url}/v1/balance",
            params={"apikey": self.api_key},
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return resp.json()

    def usage_stats(self, days: int = 7):
        """
        Get usage statistics for the last N days.

        :param days: Number of days (default 7)
        :return: JSON with period, dailyStats, summary, currentBalance, allTimeStats
        """
        resp = requests.get(
            f"{self.base_url}/v1/usage-stats",
            params={"apikey": self.api_key, "days": days},
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return resp.json()

    def rate_limit_status(self):
        """
        Get current rate limit status.

        :return: JSON with success, customerId, email, rateLimit, timestamp
        """
        resp = requests.get(
            f"{self.base_url}/v1/rate-limit-status",
            headers=self._headers,
            timeout=self.timeout,
        )
        resp.raise_for_status()
        return resp.json()
