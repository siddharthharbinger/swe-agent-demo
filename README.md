# SWE Agent Demo Repository

Demo repository for testing the **AI Software Engineering Agent Platform**.

## Files & Known Defects

### 1. Defect in `calc.py` (For Autonomous Bug-Fix Agent)
- In `calc.py`, `calculate_offset(base, delta)` contains an intentional bug: it computes `base - delta` instead of `base + delta`.
- **Reproduction Command**: `python repro.py` or `python -m unittest test_calc.py`
- Fails with exit code 1.

### 2. PR Review Demo (Pull Request #1)
- Introduces `expression_parser.py` with an insecure `eval()` call (Bandit B307).
