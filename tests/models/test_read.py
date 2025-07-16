import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import pytest
from codes.models import Sweet

def test_repr():
    sweet = Sweet(name='Repr Sweet', price=50, quantity=2)
    assert repr(sweet) == '<Sweet Repr Sweet>' 