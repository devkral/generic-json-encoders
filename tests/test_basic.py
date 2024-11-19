from decimal import Decimal

import pytest
from generic_json_encoders import json_encode, simplify


@pytest.mark.parametrize(
    "inp,result", [(Decimal("0.343430000000988"), b'"0.343430000000988"')]
)
def test_json_encode(inp, result):
    assert json_encode(inp) == result


@pytest.mark.parametrize(
    "inp,result", [(Decimal("0.343430000000988"), "0.343430000000988")]
)
def test_json_simplify(inp, result):
    assert simplify(inp) == result
