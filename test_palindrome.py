"""
Tests the palindrome module
"""
import pytest
from palindrome import *
def test_is_palindrome():
    assert is_palindrome() is True