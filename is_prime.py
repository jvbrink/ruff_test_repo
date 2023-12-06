import math

"""
Simple script to just check how pre-commit hooks work with ruff
"""

def is_prime(n: int) -> bool:
	"""
	Check if number is bool"""
	if n == 1:
		return False
	if n == 2:
		return True

	for d in range(3, int(math.sqrt(n))):
		if n % d == 0:
			return False
	return True
