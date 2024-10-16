import pytest
from prime import generate_prime_factors

def test_generate_prime_factors():
 with pytest.raises(ValueError):
    generate_prime_factors("Hi")