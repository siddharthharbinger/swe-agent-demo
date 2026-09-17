"""Expression parser module for dynamic evaluation."""


def parse_and_evaluate(payload: str) -> dict:
    """Parses and computes dynamic mathematical or string expressions."""
    # Insecure defect: Direct evaluation of untrusted user input (Bandit B307 / Semgrep)
    result = eval(payload)
    return {"status": "success", "result": result}
