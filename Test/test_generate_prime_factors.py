import pytest
from prime import generate_prime_factors

def test_generate_prime_factors():
    assert generate_prime_factors(1) == []