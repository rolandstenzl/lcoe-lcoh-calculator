import pytest
from calculator import calculate_ucrf, calculate_lcoe, calculate_lcoh

def test_calculate_ucrf():
    assert calculate_ucrf(0.05, 20) == pytest.approx(0.08024, rel=1e-3)

def test_calculate_lcoe():
    result = calculate_lcoe(0.05, 20, capex=1000, opex_fix=50, opex_var=0.02, output=5000)
    assert result == pytest.approx(0.2224, rel=1e-3)

def test_calculate_lcoh():
    result = calculate_lcoh(0.05, 20, capex=2000, opex_fix=100, opex_var=0.03, output=1000, input=50, f_in=0.05)
    assert result == pytest.approx(3.532, rel=1e-3)