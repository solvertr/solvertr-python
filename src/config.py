"""
Solvertr API configuration.
Reads BASE_URL and API_KEY from environment; defaults for local/testing.
"""
import os

BASE_URL = os.environ.get("SOLVERTR_BASE_URL", "https://api.solver.tr").rstrip("/")
API_KEY = os.environ.get("SOLVERTR_API_KEY", "YOUR_API_KEY")
