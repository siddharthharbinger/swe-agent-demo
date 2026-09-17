import sys
from calc import calculate_offset

if __name__ == '__main__':
    print("Executing reproduction script...")
    result = calculate_offset(10, 5)
    if result != 15:
        sys.stderr.write(
            f"Reproduction verified: calculate_offset(10, 5) returned {result}, expected 15\n"
        )
        sys.exit(1)
    print("OK: calculate_offset(10, 5) == 15")
    sys.exit(0)
